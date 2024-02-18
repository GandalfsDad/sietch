"""Environment creation functions"""

import subprocess
from os.path import join

from ..directory import get_environment_dir


def create_environment(environment_name: str) -> None:
    """Create a new environment"""
    environment_path = get_environment_dir(environment_name)

    subprocess.run(["python", "-m", "venv", environment_path], check=True)


def remove_environment(environment_name: str) -> None:
    """Remove an environment"""
    environment_path = get_environment_dir(environment_name)

    subprocess.run(["rm", "-rf", environment_path], check=True)


def prepare_activate_environment(environment_name: str) -> None:
    """Prepare the environment for activation"""

    environment_path = get_environment_dir(environment_name)
    activate_path = join(environment_path, "bin", "activate")

    return subprocess.run(f"echo 'source {activate_path}'", check=True, shell=True)
