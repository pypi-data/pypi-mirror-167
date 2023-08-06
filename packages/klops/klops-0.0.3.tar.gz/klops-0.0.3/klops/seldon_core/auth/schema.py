"""
Kubernetes authentication Basic Schema module.
"""
from abc import ABC, abstractmethod


class AbstractKubernetesAuth(ABC):
    """
    Abstract Class for Kubernetes get authentication
    """

    def __init__(self, **kwargs) -> None:
        self.kwargs = kwargs

    @abstractmethod
    def get_token(self) -> str:
        """_summary_
        Get token string from platforms.
        Returns:
            str: _description_ A string of Authorization token.
        """

    @abstractmethod
    def get_custer_endpoint(self) -> str:
        """_summary_
        Get cluster host URI endpoint from platfroms.
        Returns:
            str: _description_ A string of host URI endpoint.
        """
