""" Environment class to create the environment

Main functionalities:
The AzureEnvironment class is responsible for creating and managing custom environments in Azure Machine Learning.
It takes in various parameters such as Azure credentials, custom environment name, dependencies directory, version,
tags, and description to create a new environment or reuse an existing one. The main functionality of this class is to
create an environment object and register it to the Azure workspace.

Methods:
- __init__: Initializes the AzureEnvironment object with the given parameters.
- create_environment: Creates a new environment object or reuses an existing one with the given parameters. It returns
the environment object.

Fields:
- azure_credential: Azure credentials required to access the Azure Machine Learning workspace.
- custom_env_name: Name of the custom environment to be created or reused.
- dependencies_dir: Directory containing the dependencies required for the environment.
- version: Version of the environment.
- tags: Tags to be associated with the environment.
- description: Description of the environment.
"""

from azure.ai.ml.entities import Environment, BuildContext
import logging

from azureml_infra_tools.credential import AzureCredential


class AzureEnvironment:
    """Create the environment
    :param azure_credential: azureml_infra_tools credential
    :param custom_env_name: custom environment name
    :param dependencies_dir: dependencies directory
    :param version: version
    :param tags: tags
    :param description: description
    """
    def __init__(self, azure_credential: AzureCredential, custom_env_name: str, dependencies_dir: str, version: str,
                 tags: dict, description: str):
        self.azure_credential = azure_credential
        self.custom_env_name = custom_env_name
        self.dependencies_dir = dependencies_dir
        self.version = version
        self.tags = tags
        self.description = description

    def create_environment(self) -> Environment:
        """Create the environment
        :return: pipeline_job_env
        """
        try:
            pipeline_job_env = self.azure_credential.ml_client.environments.get(name=self.custom_env_name,
                                                                                version=self.version)
            logging.info(f"You already have an environment named {pipeline_job_env.name}, with the version"
                         f"{pipeline_job_env.version} we'll reuse it as is.")
            return pipeline_job_env
        except Exception:
            logging.info("Creating a new environment...")
            pipeline_job_env = Environment(
                build=BuildContext(path="src/dependencies/"),
                name=f"{self.custom_env_name}",
                description=self.description,
                tags=self.tags,
                version=self.version,
            )
            pipeline_job_env = self.azure_credential.ml_client.environments.create_or_update(pipeline_job_env)

            logging.info(
                f"Environment with name {pipeline_job_env.name} is registered to workspace, "
                f"the environment version is {pipeline_job_env.version}"
            )

            return pipeline_job_env
