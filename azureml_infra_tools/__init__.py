""" Set up the environment to run the pipeline

Objective:
The function 'setup_infrastructure' sets up the environment to run the pipeline by creating the necessary infrastructure
components such as Azure credentials, data, compute cluster, and environment.

Inputs:
- cfg: hydra configuration file
- original_dir: the original directory

Flow:
1. The function creates an AzureCredential object using the provided subscription ID, resource group name, and workspace
name.
2. It uploads the dataset to Azure ML Studio using the AzureData class.
3. It creates the compute cluster using the AzureCluster class.
4. It creates the environment using the AzureEnvironment class.
5. It returns the AzureCredential, Data, AmlCompute, and Environment objects.

Outputs:
- azure_credential: AzureCredential object used to authenticate with Azure Machine Learning Studio.
- text_bert_intentions: Data object representing the uploaded dataset.
- cpu_cluster: AmlCompute object representing the created compute cluster.
- pipeline_env: Environment object representing the created environment.

Additional aspects:
- The function uses the hydra configuration file to get the necessary parameters for creating the infrastructure
components.
- The function uses the original directory to get the path to the dependencies directory for creating the environment.
"""

import os

from azure.ai.ml.entities import Data, AmlCompute, Environment
from dotenv import load_dotenv

from azureml_infra_tools.cluster import AzureCluster
from azureml_infra_tools.credential import AzureCredential
from azureml_infra_tools.data import AzureData
from azureml_infra_tools.environment import AzureEnvironment


load_dotenv()


def setup_infrastructure(cfg, original_dir: str) -> tuple[AzureCredential, Data, AmlCompute, Environment]:
    """Set up the environment to run the pipeline
    :param cfg: hydra configuration file
    :param original_dir: (str) original directory
    :return: azure_credential, text_bert_intentions, cpu_cluster, pipeline_env
    """
    # Get a handle to the workspace
    azure_credential = AzureCredential(subscription_id=os.environ.get("SUBSCRIPTION_ID"),
                                       resource_group_name=os.environ.get("RESOURCE_GROUP_NAME"),
                                       workspace_name=os.environ.get("WORKSPACE_NAME"))

    # Upload the data to Azure ML Studio
    data_asset: Data = AzureData(azure_credential=azure_credential,
                                 data_path=cfg.data.data_path,
                                 data_name=cfg.data.name,
                                 data_description=cfg.data.description,
                                 data_version=cfg.data.version).upload_data()

    # Create the cluster
    cpu_cluster: AmlCompute = AzureCluster(azure_credential,
                                           cfg.cluster.name,
                                           cfg.cluster.type,
                                           cfg.cluster.size,
                                           cfg.cluster.min_instances,
                                           cfg.cluster.max_instances,
                                           cfg.cluster.idle_time_before_scale_down,
                                           cfg.cluster.tier).create_cluster()

    # Create the environment
    pipeline_env: Environment = AzureEnvironment(azure_credential,
                                                 cfg.environment.name,
                                                 f"{original_dir}/{cfg.environment.dependencies_dir}",
                                                 cfg.environment.version,
                                                 cfg.environment.tags,
                                                 cfg.environment.description).create_environment()

    return azure_credential, data_asset, cpu_cluster, pipeline_env
