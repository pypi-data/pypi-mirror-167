# standard imports
import platform
import subprocess
import sys

# third-party imprts
import distro
from eyantra_autoeval.utils.common import is_docker, run_shell_command
from rich import print


def evaluate():
    result = {}

    distribution = {
        "machine": platform.machine(),
        "release": platform.release(),
        "system": platform.system(),
        "version": distro.version(best=True),
        "name": distro.name(),
    }
    result["distro"] = distribution

    result["virtualized"] = "hypervisor" in run_shell_command("cat /proc/cpuinfo")

    result["dockerized"] = is_docker()

    result["apt"] = {}
    result["apt"]["packages"] = {}
    packages = (
        subprocess.run(
            "apt list --installed | awk '{print $1 $2}' | awk -F'\/now' '{print $1 \" \" $2}'",
            capture_output=True,
            shell=True,
        )
        .stdout.decode()
        .split("\n")
    )
    packages = packages[1:-1]
    packages = [p.split() for p in packages]
    result["apt"]["packages"]["installed"] = packages

    packages = run_shell_command("pip3 freeze").split("\n")
    packages = [p.split("==") for p in packages]

    result["pip3"] = {}
    result["pip3"]["packages"] = {}
    result["pip3"]["packages"]["installed"] = packages

    result["ros"] = {}
    result["ros"]["version"] = run_shell_command("rosversion -d")
    result["ros"]["packages"] = {}
    packages = run_shell_command("rosversion -a").split("\n")
    packages = [p.split(": ") for p in packages]
    result["ros"]["packages"]["installed"] = run_shell_command("rosversion -a").split(
        "\n"
    )

    result["gazebo"] = {}
    result["gazebo"]["version"] = subprocess.run(
        "gazebo --version | grep 'Gazebo' | awk '{print $NF}'",
        capture_output=True,
        shell=True,
    ).stdout.decode()

    result["python"] = {}
    result["python"]["version"] = {}
    result["python"]["version"]["major"] = sys.version_info.major
    result["python"]["version"]["minor"] = sys.version_info.minor
    result["python"]["version"]["micro"] = sys.version_info.micro

    result["gdal"] = {}
    result["gdal"]["version"] = run_shell_command("gdalinfo --version")

    print(result)
