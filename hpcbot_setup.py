#!/usr/bin/env python3
import os
import subprocess
import platform
import shutil

def check_root():
    """Check if the script is run as root."""
    return os.geteuid() == 0

def check_os():
    """Check the OS version and type."""
    try:
        with open('/etc/os-release') as f:
            lines = f.readlines()
        os_info = {}
        for line in lines:
            key, value = line.strip().split('=')
            os_info[key] = value.strip('"')
        return os_info['ID'].lower(), os_info['VERSION_ID']
    except FileNotFoundError:
        return None, None

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
        print("This script must be run as root.")
        exit(1)

    os_type, os_version = check_os()
    if os_type == "ubuntu":
        commands = [
            "apt-get update",
            "apt-get install -y python3-pip",
            "pip install openai==0.28"
        ]
    elif os_type in ["rhel", "centos"]:
        commands = [
            "yum update -y",
            "yum install -y python3-pip",
            "pip3 install openai==0.28"
        ]
    else:
        print(f"Unsupported OS: {os_type}")
        exit(1)

    execute_commands(commands)
    
    # Copy the script itself to /usr/local/bin
    script_path = os.path.abspath(__file__)
    copy_to_bin(script_path)
    
    print("Commands executed successfully.")
    print("You can now run the script by typing 'hpcbot' in the terminal.")