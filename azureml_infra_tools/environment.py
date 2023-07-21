""" Environment class to create the environment
"""
from azure.ai.ml.entities import Environment, BuildContext


class AzureEnvironment:
    """Create the environment
    :param azure_credential: azureml_infra_tools credential
    :param custom_env_name: custom environment name
    :param dependencies_dir: dependencies directory
    :param version: version
    :param tags: tags
    :param description: description
    """
    def __init__(self, azure_credential, custom_env_name, dependencies_dir, version,
                 tags, description):
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
            print(f"You already have an environment named {pipeline_job_env.name}, with the version "
                  f"{pipeline_job_env.version} we'll reuse it as is.")
            return pipeline_job_env
        except Exception:
            print("Creating a new environment...")
            pipeline_job_env = Environment(
                build=BuildContext(path="src/dependencies/"),
                name=f"{self.custom_env_name}",
                description=self.description,
                tags=self.tags,
                version=self.version,
            )
            pipeline_job_env = self.azure_credential.ml_client.environments.create_or_update(pipeline_job_env)

            print(
                f"Environment with name {pipeline_job_env.name} is registered to workspace, "
                f"the environment version is {pipeline_job_env.version}"
            )

            return pipeline_job_env
