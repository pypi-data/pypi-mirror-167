"""
Deployment Module for Seldon Core.
"""
import json
import pathlib
from typing import Dict
import yaml

from kubernetes import client

from klops.seldon_core.auth.schema import AbstractKubernetesAuth
from klops.seldon_core.exception import SeldonDeploymentException


class SeldonDeployment:
    """_summary_
    CRUD Kubernetes operation class implementation for Seldon ML Deployment.
    """

    api: client.CustomObjectsApi = None

    def __init__(self,
                 authentication: AbstractKubernetesAuth,
                 namespace: str) -> None:
        """_summary_
        The contructor for SeldonDeployment class.
        Args:
            authentication (AbstractKubernetesAuth): _description_
                The authentication instances. Currently only supports for local cluster or GKE.
            namespace (str): _description_ The kubernetes namespace deployment target.
        """
        self.authentication = authentication
        self.namespace = namespace
        self.connect_to_cluster()

    def connect_to_cluster(self) -> None:
        """_summary_
        Connect to the kubernetes cluster given from the constructor arguments.
        """
        configuration = client.Configuration()
        configuration.host = self.authentication.get_custer_endpoint()
        configuration.verify_ssl = False
        configuration.api_key['authorization'] = "Bearer " + \
            self.authentication.get_token()

        api_client = client.ApiClient(configuration=configuration)
        self.api = client.CustomObjectsApi(api_client=api_client)

    def load_deployment_configuration(self, file_name: str):
        """_summary_
        Load the deployment configuration file into a Python dictionary.

        Args:
            file_name (str): _description_ The deployment file name.
                It can be Yaml file (.yml or .yaml) or JSON file.

        Returns:
            deployment_config (dict): _description_ Seldon Deployment configuration dictionary.

        Raises:
            ValueError: _description_ When the file type are not yaml or json.
            JSONDecodeError: _description_ When the JSON file contains wrong format.
            YAMLError: _description_ When the Yaml contains wrong format.
        """
        deployment_config = {}

        with open(file_name, "rb") as file:
            extension = pathlib.Path(file_name).suffix
            if extension == ".json":
                deployment_config = json.load(file)
            elif extension in [".yaml", ".yml"]:
                deployment_config = yaml.safe_load(file)
            else:
                raise ValueError("Invalid file type.")
        return deployment_config

    def deploy(self, deployment_config: Dict) -> Dict:
        """_description_
        Deploy the ML Model

        Args:
            deployment_config (Union[object, Dict]): _description_
                Deployment Configuration Object.

        Returns:
            deployment_result (Dict): _description_ The deployment result metadata in a dictionary.

        Raises:
            SeldonDeploymentException: _description_ Raised when the deployment failed.
        """
        deployment_name = deployment_config["metadata"]["name"]

        deployment_existence = self.check_deployment_exist(
            deployment_name=deployment_name)
        if not deployment_existence:

            deployment_result = self.api.create_namespaced_custom_object(
                group="machinelearning.seldon.io",
                version="v1alpha2",
                plural="seldondeployments",
                body=deployment_config,
                namespace=self.namespace)
        else:
            deployment_result = self.api.patch_namespaced_custom_object(
                group="machinelearning.seldon.io",
                version="v1alpha2",
                name=deployment_name,
                plural="seldondeployments",
                body=deployment_config,
                namespace=self.namespace)
        return deployment_result

    def check_deployment_exist(self, deployment_name: str) -> bool:
        """ _summary_
        Check the deployment already exists.

        Args:
            deployment_name (str): _description_ The deployment name, Example: iris-model

        Returns:
            bool: _description_ The deployment existence.

        Raises:
            AttributeError: _description_ Raised when the key doesn't exists.
            NoneTypeException: _description_ Raised when wrong compared with None Object.
        """
        deployment_names = []
        response = self.api.list_namespaced_custom_object(
            group="machinelearning.seldon.io",
            version="v1alpha2",
            plural="seldondeployments",
            namespace=self.namespace)
        for item in response["items"]:
            deployment_names.append(item["metadata"]["name"])
        return deployment_name in deployment_names

    def delete_by_deployment_config(self, deployment_config: Dict) -> bool:
        """_summary_
        Delete the deployment by its configuration.

        Args:
            deployment_config (Union[object, Dict]): _description_ \
                Deployment Configuration Object.

        Returns:
            bool: _description_ Boolean result of deployment deletion.

        Raises:
            SeldonDeploymentException: _description_ Raised when the deployment failed.
        """
        return self.delete(deployment_config["metadata"]["name"])

    def delete(self, deployment_name: str) -> bool:
        """_summary_
        Deploy the ML Model

        Args:
            deployment_name (Union[object, Dict]): _description_ Deployment name.

        Returns:
            bool: _description_ Boolean result of deployment deletion.

        Raises:
            SeldonDeploymentException: _description_ Raised when the deployment failed.
        """
        try:
            deployment_existence = self.check_deployment_exist(
                deployment_name=deployment_name)
            if not deployment_existence:
                return False
            else:
                deletion_result = self.api.delete_namespaced_custom_object(
                    group="machinelearning.seldon.io",
                    version="v1alpha2",
                    name=deployment_name,
                    plural="seldondeployments",
                    namespace=self.namespace)
                if deletion_result:
                    return True
        except SeldonDeploymentException as deployment_exception:
            print("Deployment deletion failed,", str(deployment_exception))
            return False
