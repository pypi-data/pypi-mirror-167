"""
Google Kubernetes Engine (GKE) Module for Authentication Implementation
"""

from google.auth import compute_engine, transport
from google.cloud.container_v1 import ClusterManagerClient

from klops.seldon_core.auth.schema import AbstractKubernetesAuth


class GKEAuthentication(AbstractKubernetesAuth):
    """
    Google Kubernetes Engine (GKE) Class Implementation for Kubernetes authentication.
    """

    def get_custer_endpoint(self) -> str:
        """
        Get GKE Cluster host URI endpoint
        Returns:
            A String of GKE Cluster host URI endpoint.
        """
        cluster_manager_client = ClusterManagerClient()
        cluster = cluster_manager_client.get_cluster(
            name=f'projects/{self.kwargs["project_id"]}/locations/{self.kwargs["zone"]}/clusters/{self.kwargs["cluster_id"]}')

        return f"https://{cluster.endpoint}:443"

    def get_token(self) -> str:
        """
        Get GKE Bearer Token String.
        Returns:
            A String of GKE Bearer Token String.
        """
        credentials = compute_engine.Credentials()
        credentials.refresh(transport.requests.Request())
        return credentials.token


__all__ = ["GKEAuthentication"]
