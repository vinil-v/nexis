#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# nexis_setup.py
"""
Nexis is an innovative CLI-based tool designed to address the challenges faced by HPC and AI engineers. 
By leveraging the power of AI, Nexis transforms the traditional CLI experience into an intelligent and interactive support system that provides real-time assistance to users.
This script installs the required dependencies and copies the main script to /usr/local/bin so that it can be run from anywhere in the terminal.
"""
#Author : Vinil Vadakkepurakkal
#Date   : 2024-08-07

import os
import subprocess
import platform
import shutil
import sys

def check_root():
    """Check if the script is run as root."""
    return os.geteuid() == 0

def check_python_version():
    """Check if the default python3 version is 3.8 or higher."""
    try:
        #adjusting for older python versions
        result = subprocess.run(['python3', '--version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        version_str = result.stdout.strip() or result.stderr.strip()
        version_str = version_str.split()[1]
        #result = subprocess.run(['python3', '--version'], capture_output=True, text=True)
        #version_str = result.stdout.strip().split()[1]
        major, minor, _ = version_str.split('.')
        if (int(major), int(minor)) < (3, 8):
            print("Python 3.8 or higher is required.")
            print("Please install Python 3.8 or higher. You can download it from https://www.python.org/downloads/")
            print("Or, if you have multiple Python versions installed, you can try running this script and nexis script with `python3.8`.")
            sys.exit(1)
    except Exception as e:
        print(f"An error occurred while checking the python3 version: {e}")
        sys.exit(1)
        
def get_python_version():
    """Get the current Python version."""
    version_info = platform.python_version_tuple()
    return tuple(map(int, version_info[:3]))

def check_os():
    """Check the OS version and type."""
    try:
        with open('/etc/os-release') as f:
            lines = f.readlines()
        os_info = {}
        for line in lines:
            line = line.strip()
            if '=' in line:
                key, value = line.split('=', 1)  # Split only on the first '='
                os_info[key] = value.strip('"')
        return os_info.get('ID', '').lower(), os_info.get('VERSION_ID', '')
    except FileNotFoundError:
        print("Error: /etc/os-release file not found.")
        exit(1)
    except Exception as e:
        print(f"Error occurred while reading /etc/os-release: {e}")
        exit(1)

def execute_commands(commands):
    """Execute a list of shell commands."""
    for command in commands:
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Command '{command}' failed with error: {e}")
            exit(1)

def copy_to_bin(file_path):
    """Copy the file to /usr/local/bin and make it executable."""
    if not check_root():
        print("This operation requires root privileges.")
        exit(1)

    dest_path = os.path.join('/usr/local/bin', os.path.basename(file_path))
    try:
        shutil.copy(file_path, dest_path)
        os.chmod(dest_path, 0o755)  # Make the file executable
        print(f"Copied {file_path} to {dest_path} and set it as executable.")
    except IOError as e:
        print(f"Failed to copy {file_path} to {dest_path}: {e}")
        exit(1)

if __name__ == "__main__":
    

    if not check_root():
        print("This script must be run with root privileges.")
        exit(1)
 #    Main function to execute the script logic.
    python_version = get_python_version()

    # Check Python version and run the version check function if less than 3.8
    if python_version < (3, 8):
        check_python_version()

    # Check the OS and run the appropriate commands
    os_type, os_version = check_os()
    if os_type == "ubuntu":
        commands = [
            "sudo apt-get update",
            "sudo apt-get install -y python3-pip",
            "sudo pip install openai==0.28"
        ]
    elif os_type in ["rhel", "centos", "almalinux"]:
        commands = [
            "sudo yum clean all",
            "sudo yum install -y python38-pip",
            "sudo pip3.8 install --user openai==0.28"
        ]
    else:
        print(f"Unsupported OS: {os_type}")
        exit(1)

    execute_commands(commands)

    # Copy the script itself to /usr/local/bin
    script_path = os.path.abspath("nexis")
    copy_to_bin(script_path)

    print("All is well - Setup completed!.")
    print("You can now run the script by typing 'nexis' in the terminal.")