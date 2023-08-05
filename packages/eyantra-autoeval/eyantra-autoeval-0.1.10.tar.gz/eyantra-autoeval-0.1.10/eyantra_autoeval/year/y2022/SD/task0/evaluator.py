# standard imports
import platform
import subprocess
import sys

# third-party imprts
import distro
from eyantra_autoeval.utils.common import is_docker, run_shell_command
from rich.console import Console
from rich import print


def evaluate():
    result = {}
    console = Console()
    with console.status("[bold green]Gathering data...") as status:
        console.log(f"[green]Gathering system information [/green]")
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

        console.log(f"[green]Gathering aptitude packages information [/green]")
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
        packages = [p.split()[0:2] for p in packages]
        result["apt"]["packages"]["installed"] = packages

        console.log(f"[green]Gathering pip packages information [/green]")
        packages = run_shell_command("pip3 freeze").split("\n")
        packages = [p.split("==") for p in packages]

        result["pip3"] = {}
        result["pip3"]["packages"] = {}
        result["pip3"]["packages"]["installed"] = packages

        console.log(f"[green]Gathering ROS packages information [/green]")
        result["ros"] = {}
        result["ros"]["version"] = run_shell_command("rosversion -d")
        result["ros"]["packages"] = {}
        packages = run_shell_command("rosversion -a").split("\n")
        packages = [p.split(": ") for p in packages]
        result["ros"]["packages"]["installed"] = packages

        console.log(f"[green]Gathering gazebo information [/green]")
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

        console.log(f"[green]Gathering python information [/green]")
        result["python"] = {}
        result["python"][
            "version"
        ] = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"

        console.log(f"[green]Gathering GDAL information [/green]")
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

        console.log(f'[bold][red]Done!')

    return result
