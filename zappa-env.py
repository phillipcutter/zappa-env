import sys
import subprocess
from pathlib import Path

home_virtualenv_folder = ".virtualenvs"
home = str(Path.home())

virtual_env_folder = f"{home}/{home_virtualenv_folder}"


def main():
    args = sys.argv
    if len(args) == 1:
        print("Please specify the name of a virtualenv after the "
              "zappa-env command")
        return
    elif len(args) == 2:
        print("Please specify a zappa command to be ran after loading "
              "zappa from the specified virtualenv")
        return
    virtual_env = args[1]
    other_commands = args[2:]

    subprocess_cmd(
        "source $(which virtualenvwrapper.sh); "
        f"workon {virtual_env}; "
        "echo \"Using virtualenv: $VIRTUAL_ENV to run Zappa command\"; "
        "zappa " + " ".join(other_commands))


def subprocess_cmd(command):
    process = subprocess.Popen(
        command, shell=True, executable="/bin/bash")
    process.communicate()


if __name__ == "__main__":
    main()
