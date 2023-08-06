"""_summary_
"""
import subprocess

from klops.config import LOGGER


def shell_executor(command: str) -> subprocess.CompletedProcess:
    """_summary_
    Command line executor wrapper.
    Args:
        command (str): _description_ The shell command string.

    Returns:
        subprocess.CompletedProcess: _description_
    """
    try:
        return subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as called_error:
        LOGGER.error(str(called_error))
    except subprocess.SubprocessError as sub_error:
        LOGGER.error(str(sub_error))
    