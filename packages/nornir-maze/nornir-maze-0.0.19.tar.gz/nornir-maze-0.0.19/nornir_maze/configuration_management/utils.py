#!/usr/bin/env python3
"""
This helper file contains general functions and tasks related to Nornir.

The functions are ordered as followed:
- Helper Functions
- Nornir print functions
- Nornir Helper Tasks
"""

import os
import sys
import time
import subprocess  # nosec
import re
import argparse
from alive_progress import alive_bar
from nornir_jinja2.plugins.tasks import template_file
from nornir.core.task import Result
from nornir_netmiko.tasks import netmiko_file_transfer
from ..utils import (
    print_task_title,
    print_task_name,
    task_host,
    task_info,
    task_error,
    CustomArgParse,
    CustomArgParseWidthFormatter,
    compute_md5,
)


__author__ = "Willi Kubny"
__maintainer__ = "Willi Kubny"
__version__ = "1.0"
__license__ = "MIT"
__email__ = "willi.kubny@kyndryl.com"
__status__ = "Production"


#### Helper Functions ########################################################################################


def track_upgrade_process(nr_obj):
    """
    This function creates a dictionary with the installation process status of each host and runs the custom
    Nornir task fping_task in a range loop. In each loop the software installation status will be updated and
    printed to std-out. There are three expected status which each host will go through the installation
    process. These status are "Installing software", "Rebooting device" and the final status will be "Upgrade
    finish". When all hosts are upgraded successful the script exits the range loop and prints the result to
    std-out. In case the software upgrade is not successful after the range loop is finish, an info message
    will be printed and exit the script.
    """
    # Printout sleep and refresh values
    refresh_timer = 60
    max_refresh = 40
    elapsed_time = 0
    ansi_yellow = "\033[4m\033[1;33m"
    ansi_red = "\033[4m\033[0;31m"
    ansi_green = "\033[4m\033[0;32m"
    ansi_reset = "\033[0m"

    # Dict to track the host software upgrade status
    update_status = {}
    for host in nr_obj.inventory.hosts:
        update_status[host] = "Installing software"

    for _ in range(max_refresh):
        # Run the custom Nornir task fping_task
        task = nr_obj.run(task=fping_task, on_failed=True)

        # fmt: off
        subprocess.run(["clear"], check=True)  # nosec
        # fmt: on

        print_task_title("RESTCONF software upgrade in progress")
        task_text = "Fping track software upgrade process"
        print_task_name(task_text)

        # Update the host software upgrade status and print the result
        for host in task:
            # host fping task result
            fping = task[host].result["output"].rstrip()

            # Initial status -> Host is alive and is installing the software
            if "alive" in fping and "Installing software" in update_status[host]:
                update_status[host] = f"{ansi_yellow}Installing software{ansi_reset}"
            # Second status -> Host is not alive and is rebooting
            if "alive" not in fping and "Installing software" in update_status[host]:
                update_status[host] = f"{ansi_red}Reboot device{ansi_reset}"
            if "alive" not in fping and "Rebooting device" in update_status[host]:
                pass
            # Third status -> host is rebooted with new software release
            if "alive" in fping and "Reboot device" in update_status[host]:
                update_status[host] = f"{ansi_green}Upgrade finish{ansi_reset}"

            # Print the host software upgrade status result
            print(task_host(host=host, changed="False"))
            print(f"Status: {update_status[host]} (fping: {fping})")

        print("\n")

        # Check if all hosts have upgraded successfull
        if not all(f"{ansi_green}Upgrade finish{ansi_reset}" in value for value in update_status.values()):
            # Continue the range loop to track to software upgrade status
            print(
                "\033[1m\u001b[31m"
                f"The fping task result will refresh in {refresh_timer}s ...\n"
                f"Elapsed waiting time: {elapsed_time}/{max_refresh * refresh_timer}s"
                "\033[0m"
            )
            elapsed_time += refresh_timer
            time.sleep(refresh_timer)

        else:
            # Print result and exit the range loop
            print(
                "\033[1m\u001b[32m"
                f"Elapsed waiting time: {elapsed_time}/{max_refresh * refresh_timer}s\n"
                "Wait 120s until the device NGINX RESTCONF server is ready"
                "\033[0m"
            )
            # Sleep for some seconds until the device NGINX RESTCONF server is ready
            time.sleep(120)
            break

    # If the range loop reached the end -> Software upgrade not successful
    else:
        print(
            "\n\033[1m\u001b[31m"
            f"Total software upgrade waiting time of {max_refresh * refresh_timer}s exceeded"
            "\033[0m"
        )


def index_of_first_number(string):
    """
    Return the index of the first number in a string
    """
    # pylint: disable=invalid-name
    for i, c in enumerate(string):
        if c.isdigit():
            index = i
            break

    return index


def extract_interface_number(string):
    """
    Removes the interface name and returns only the interface number
    """
    try:
        index = index_of_first_number(string)
        interface_number = string[index:]

    except UnboundLocalError:
        interface_number = string

    return interface_number


def extract_interface_name(string):
    """
    Removes the interface number and returns only the interface name
    """
    try:
        index = index_of_first_number(string)
        interface_name = string[:index]

    except UnboundLocalError:
        interface_name = string

    return interface_name


def complete_interface_name(interface_string):
    """
    This function takes a string with an interface name only or a full interface with its number and returns
    the full interface name but without the number:
    Gi -> GigabitEthernet
    Tw -> TwentyFiveGigE
    etc.
    """
    # pylint: disable=no-else-return, unidiomatic-typecheck

    error_msg = "Variable interface_string"

    if type(interface_string) is str:
        # Extract the interface name / delete the interface number
        interface_name = extract_interface_name(interface_string)
        # Define the name of the interface
        if interface_name.startswith("Eth"):
            interface_name = "Ethernet"
        elif interface_name.startswith("Fa"):
            interface_name = "FastEthernet"
        elif interface_name.startswith("Gi"):
            interface_name = "GigabitEthernet"
        elif interface_name.startswith("Te"):
            interface_name = "TenGigabitEthernet"
        elif interface_name.startswith("Tw"):
            interface_name = "TwentyFiveGigE"
        elif interface_name.startswith("Hu"):
            interface_name = "HundredGigE"
        else:
            raise ValueError(f"{error_msg} value is not a known interface name")

        return interface_name

    else:
        raise TypeError(f"{error_msg} is not a type string")


def init_args(argparse_prog_name):
    """
    This function initialze all arguments which are needed for further script execution. The default arguments
    will be supressed. Returned will be a tuple with a use_nornir variable which is a boolian to indicate if
    Nornir should be used for dynamically information gathering or not.
    """
    task_text = "ARGPARSE verify arguments"
    print_task_name(text=task_text)

    # Define the arguments which needs to be given to the script execution
    argparser = CustomArgParse(
        prog=argparse_prog_name,
        description="Filter the Nornir inventory based on a tag or a host",
        epilog="Only one of the mandatory arguments can be specified.",
        argument_default=argparse.SUPPRESS,
        formatter_class=CustomArgParseWidthFormatter,
    )

    # Create a mutually exclusive group. Argparse will make sure that only one of the arguments in the group
    # was present on the command line
    arg_group = argparser.add_mutually_exclusive_group(required=True)

    # Add arg_group parser arguments
    arg_group.add_argument(
        "--tag", type=str, metavar="<TAG>", help="inventory filter for a single Nornir tag"
    )
    arg_group.add_argument(
        "--hosts", type=str, metavar="<HOST-NAMES>", help="inventory filter for comma seperated Nornir hosts"
    )

    # Add the optional verbose argument
    argparser.add_argument(
        "-v", "--verbose", action="store_true", default=False, help="show extensive result details"
    )

    # Add the optional rebuild argument
    argparser.add_argument(
        "-r",
        "--rebuild",
        action="store_true",
        default=False,
        help="rebuild the config from day0 (default: golden-config)",
    )

    # Verify the provided arguments and print the custom argparse error message in case any error or wrong
    # arguments are present and exit the script
    args = argparser.parse_args()

    return args


def create_single_interface_list(interface_list):
    """
    This function takes a list of interfaces that are like the cisco interface range command and makes a list
    of full interface names for each interface:
    Gi1/0/1 -> GigabitEthernet1/0/1
    Gi1/0/1 - 10 -> GigabitEthernet1/0/1, GigabitEthernet1/0/2, etc.
    Gi1/0/1 - Gi1/0/10 -> GigabitEthernet1/0/1, GigabitEthernet1/0/2, etc.
    """
    # Define a list to return at the end of the function
    single_interface_list = []

    # Create the full interface name
    for interface in interface_list:
        # Create the full name of the interface, eg. Gi -> GigabitEthernet
        interface_name = complete_interface_name(interface)

        # If the list element is a interface range fullfil every single interface
        if "-" in interface:
            # Create a list with the two interfaces for the range
            interface_range = interface.replace(" ", "")
            interface_range = interface.split("-")

            # Regex pattern to match only the last number after the /
            pattern = r"(\d+)(?!.*\d)"

            # 1. Match the interface number prefix without the last number
            interface_prefix = extract_interface_number(interface_range[0])
            interface_prefix = re.sub(pattern, "", interface_prefix)

            # 2. Match the number after the last / in the interface number
            last_interface_numbers = []
            for interface in interface_range:
                # Extract only the interface number
                interface_number = extract_interface_number(interface)
                last_interface_number = re.findall(pattern, interface_number)
                last_interface_numbers.append(last_interface_number[0])

            # Define integers for the first and the last number of the range
            range_first_number = int(last_interface_numbers[0])
            range_last_number = int(last_interface_numbers[1])
            # Iterate over the range and construct each single interface
            while range_first_number <= range_last_number:
                single_interface = interface_name + interface_prefix + str(range_first_number)
                single_interface = single_interface.replace(" ", "")
                single_interface_list.append(single_interface)
                range_first_number += 1

        # If the list element is a single interface add it to the list to return
        else:
            interface_number = extract_interface_number(interface)
            single_interface = interface_name + interface_number
            single_interface_list.append(single_interface)

    return single_interface_list


#### Nornir Helper Tasks #####################################################################################


def create_tpl_int_list(task):
    """
    This function loops over all host inventory keys and append the key which start with tpl_int to the list
    of interface groups and returns a Nornir AggregatedResult Object
    """
    tpl_int_list = []
    for key in task.host.keys():
        if key.startswith("tpl_int"):
            tpl_int_list.append(key)

    return tpl_int_list


def template_file_custom(task, task_msg, path, template):
    """
    This custom Nornir task generates a configuration from a Jinja2 template based on a path and a template
    filename. The path and the template filename needs to be Nornir inventory keys which holds the needed
    information as value.
    """
    try:
        path = task.host[path]
        template = task.host[template]

    except KeyError as error:
        # Jinja2 Nornir inventory key not found. Key which specify the path and the file don't exist
        error_msg = (
            f"{task_error(text=task_msg, changed='False')}\n"
            + f"'nornir.core.inventory.Host object' has no attribute {error}"
        )

        # Return the Nornir result as error -> interface can not be configured
        return Result(host=task.host, result=error_msg, failed=True)

    # Run the Nornir Task template_file
    j2_tpl_result = task.run(task=template_file, template=template, path=path, on_failed=True)

    return Result(host=task.host, result=j2_tpl_result)


def verify_source_file_task(task):
    """
    This custom Nornir task gets the desired software file path from the Nornir inventory, verifies the file
    exists and computes the md5 hash. The result is a dictionary with infos about the source and the
    destination file which can be used for further processing.
    """
    task_text = "NORNIR verify source file"

    try:
        # Get the version string and source file from the Nornir inventory
        software_version = task.host["software"]["version"]
        source_file = task.host["software"]["file"]
    except KeyError as error:
        # KeyError exception handles not existing host inventory data keys
        result = (
            f"{task_error(text=task_text, changed='False')}\n"
            + f"'Key task.host[{error}] not found' -> NornirResponse: <Success: False>"
        )
        # Return the Nornir result as error
        return Result(host=task.host, result=result, failed=True)

    # Verify that the software file exists
    if not os.path.exists(source_file):
        result = (
            f"{task_error(text=task_text, changed='False')}\n"
            + f"'File {source_file} not found' -> OSResponse: <Success: False>\n"
        )
        # Return the Nornir result as error
        return Result(host=task.host, result=result, failed=True)

    # Compute the original md5 hash value
    source_md5 = compute_md5(source_file)
    # Get the filesize and format to GB
    # pylint: disable=consider-using-f-string
    file_size = "%.2f" % (os.path.getsize(source_file) / (1024 * 1024 * 1024))
    # Extract only the filename and prepare the destination path
    dest_file = os.path.basename(source_file)

    result_info = (
        f"{task_info(text=task_text, changed='False')}\n"
        + f"'{task_text}' -> OSResponse: <Success: True>\n"
        + f"\n-> Desired version: {software_version}\n"
        + f"-> Source file: {source_file}\n"
        + f"-> Source MD5-Hash: {source_md5}"
    )

    result = {
        "result_info": result_info,
        "software_version": software_version,
        "source_file": source_file,
        "source_md5": source_md5,
        "file_size": file_size,
        "dest_file": dest_file,
    }

    # Return the Nornir result as success
    return Result(host=task.host, result=result)


def upload_file_task(task, verify_source_result):
    """
    This custom Nornir task takes the result of the function verify_source_result as an argument and runs the
    task netmiko_file_transfer to upload the software file to each host. The standard task result is returned.
    """

    source_file = verify_source_result[str(task.host)].result["source_file"]
    dest_file = verify_source_result[str(task.host)].result["dest_file"]

    with alive_bar(spinner="waves2", unknown="waves2"):
        # Run the standard Nornir task netmiko_file_transfer
        result = task.run(
            task=netmiko_file_transfer, source_file=source_file, dest_file=dest_file, direction="put"
        )

    return Result(host=task.host, result=result)


def fping_task(task):
    """
    This custom Nornir task runs the linux command fping to the host IP-address. The returned result is a
    dictionary with the fping output and the retruncode.
    """

    # fmt: off
    fping = subprocess.run( # nosec
        ["fping", "-A", "-d", task.host.hostname,], check=False, capture_output=True
    )
    # fmt: on

    result = {"returncode": fping.returncode, "output": fping.stdout.decode("utf-8")}

    return Result(host=task.host, result=result)


#### Nornir Helper tasks in regular Function #################################################################


def verify_source_file(nr_obj):
    """
    This function runs the custom Nornir task verify_source_file_task to get the desired software file path
    from the Nornir inventory, verifies the file exists and computes the md5 hash. The result will be printed
    to std-out in custom Nornir style and a dictionary with infos about the source and the destination file
    is returned which can be used for further processing. In case of a source file verification error a info
    message will be printed and the script terminates.
    """
    print_task_name("NORNIR Verify source file")

    # Run the custom Nornir task verify_source_file_task
    task_result = nr_obj.run(task=verify_source_file_task)

    # Print the task results
    for host in task_result:
        print(task_host(host=host, changed="False"))

        # If the task fails and a exceptions is the result
        if isinstance(task_result[host].result, str):
            print(task_result[host].result)
        # Else print the result_info from the custom returned dict
        else:
            print(task_result[host].result["result_info"])

    # If one or more host inside the task has failed -> Exit the script
    if task_result.failed:
        print("\n")
        print(task_error(text="Verify source file", changed="False"))
        print("\U0001f4a5 ALERT: NORNIR SOURCE FILE VERIFICATION FAILED! \U0001f4a5")
        print(
            "\n\033[1m\u001b[31m"
            "-> Analyse the Nornir output for failed task results\n"
            "-> May apply Nornir inventory changes and run the script again\n"
            "\033[0m"
        )
        sys.exit()

    return task_result


def upload_file(nr_obj, verify_source_result):
    """
    This function takes the result of the function verify_source_result as an argument and runs fist the
    custom Nornir task upload_file_task to upload the software file to the switch. If the software upload is
    not successful for all hosts, a info message will be printed and the scripts terminates.
    """

    task_text = "NETMIKO upload file"
    print_task_name(task_text)

    # Print some info for each host
    for host in verify_source_result:
        dest_file = verify_source_result[host].result["dest_file"]
        file_size = verify_source_result[host].result["file_size"]
        print(task_host(host=host, changed="False"))
        print(task_info(text=task_text, changed="False"))
        print(f"Copy {dest_file} ({file_size} GB) to flash:")

    # Run the custom Nornir task upload_file_task
    print("\n")
    upload_result = nr_obj.run(task=upload_file_task, verify_source_result=verify_source_result)

    # If upload_file_task failed -> Print results and exit the script
    if upload_result.failed:
        # Print the task results
        for host in upload_result:
            print(task_host(host=host, changed="False"))

            # If the task fails and a exceptions is the result
            if isinstance(upload_result[host].result, str):
                print(upload_result[host].result)
            else:
                for result in upload_result[host].result:
                    print(result)

        print("\n")
        print(task_error(text=task_text, changed="False"))
        print("\U0001f4a5 ALERT: NETMIKO FILE UPLOAD FAILED! \U0001f4a5")
        print(
            "\n\033[1m\u001b[31m"
            "-> Analyse the Nornir output for failed task results\n"
            "-> May apply Nornir inventory changes and run the script again\n"
            "\033[0m"
        )
        sys.exit()
