"""_summary_
Main module for versioning Control.
"""

import pickle
from typing import Any, Dict, List, Union

import dvc
import numpy as np
import pandas as pd

from klops.config import LOGGER
from klops.versioning.helper import shell_executor


class Versioning:
    """_summary_
    Versioning control for klops. Based on DVC.
    """

    def init(self) -> None:
        """_summary_ Initiate DVC

        Initiate the DVC when it's not found.
        """
        shell_executor("dvc init")

    def add_remote(self, name: str, remote_url: str) -> None:
        """_summary_
        Add remote repository. Could be local, or remote storage such as GCP bucket or AWS s3.
        Args:
            remote_url (str): _description_
        """
        shell_executor(f"dvc remote add -d {name} {remote_url}")

    def add(self, file_or_path: str) -> None:
        """_summary_
        Track the file / path into DVC.
        Args:
            file_or_path (str): _description_ File or path tobe added.
        """
        shell_executor(f"dvc add {file_or_path}")

    def push(self) -> None:
        """_summary_
        Push every tracked changes into dvc.
        """
        shell_executor("dvc push")

    def pull(self) -> None:
        """_summary_
        Pull the commited data.
        """
        shell_executor("dvc pull")

    def repro(self) -> None:
        """_summary_
        Reproduce the DVC pipeline.
        """
        shell_executor("dvc repro")

    def run(self,
            entry_point: str,
            name: str = None,
            dependencies: List = [],
            outputs: List = []) -> None:
        """_summary_
        Run the defined DVC pipeline.
        Args:
            entry_point (str): _description_ The main program to be executed.
            name (str, optional): _description_. Defaults to None. The Pipeline name.
            dependencies (List, optional): _description_. Defaults to []. List of dependencies. The same as `-d` options in dvc command.
            outputs (List, optional): _description_. Defaults to []. List of the outputs, The same as `-o` options in dvc command.
        """
        deps = ""
        outs = ""
        name = "" if name is None else f" -n {name}"
        for dep in dependencies:
            deps = deps + "-d " + dep

        for out in outputs:
            outs = outs + "-o " + out

        shell_executor(f"dvc run{name} {deps} {outs} {entry_point}")

    def read_binary(self, file_name: str) -> Any:
        """_summary_
        Read the binary file such as .pkl, .joblib, etc. stored in the DVC storage / repository.
        Args:
            file_name (str): _description_ The file name. Including its path.

        Returns:
            Any: _description_ Object pointer instances.
        """
        try:
            model = pickle.loads(dvc.api.read(file_name, mode='rb'))
            return model
        except dvc.exceptions.FileMissingError as file_missing:
            LOGGER.error(str(file_missing))
        except dvc.exceptions.PathMissingError as path_missing:
            LOGGER.error(str(path_missing))

    def read_dataset(self, file_name: str) -> Any:
        """_summary_
        Read dataset from DVC artifact storage.
        Args:
            file_name (str): _description_ The file name. Including it's path.

        Returns:
            Any: _description_ The dataset buffer. Need to parse.
        """
        try:
            with dvc.api.open(file_name) as file_buffer:
                return file_buffer
        except dvc.exceptions.FileMissingError as file_missing:
            LOGGER.error(str(file_missing))
        except dvc.exceptions.PathMissingError as path_missing:
            LOGGER.error(str(path_missing))
