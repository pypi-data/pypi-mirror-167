# standard imports
import platform
import subprocess
import sys
import time

# third-party imprts
import distro
from eyantra_autoeval.utils.common import is_docker, run_shell_command
from rich import print


def evaluate():
    start_time = time.time()
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
            "apt list --installed",
            capture_output=True,
            shell=True,
        )
        .stdout.decode()
        .split("\n")
    )
    packages = packages[1:-1]
    packages = [p.split()[1:-1] for p in packages]
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
    result["ros"]["packages"]["installed"] = packages

    result["gazebo"] = {}
    result["gazebo"]["version"] = (
        subprocess.run(
            "gazebo --version | grep 'Gazebo' | awk '{print $NF}'",
            capture_output=True,
            shell=True,
        )
        .stdout.decode()
        .strip()
    )

    result["python"] = {}
    result["python"][
        "version"
    ] = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"

    result["gdal"] = {}
    result["gdal"]["version"] = (
        subprocess.run(
            "gdalinfo --version | awk '{print $2}' | sed 's/\,//'",
            capture_output=True,
            shell=True,
        )
        .stdout.decode()
        .strip()
    )

    end_time = time.time()
    result["meta"]["evaluation_time"] = end_time - start_time
    print(result)
