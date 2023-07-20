""" Set up the environment to run the pipeline
"""

import os

from azure.ai.ml.entities import Data, AmlCompute, Environment
from dotenv import load_dotenv

from azuremlutils.cluster import AzureCluster
from azuremlutils.credential import AzureCredential
from azuremlutils.data import AzureData
from azuremlutils.environment import AzureEnvironment

load_dotenv()


def setup_infrastructure(cfg, original_dir: str) -> tuple[AzureCredential, Data, AmlCompute, Environment]:
    """Set up the environment to run the pipeline
    :param cfg: configuration file
    :param original_dir: (str) original directory
    :return: azure_credential, text_bert_intentions, cpu_cluster, pipeline_env
    """
    # Get a handle to the workspace
    azure_credential = AzureCredential(os.environ.get("SUBSCRIPTION_ID"),
                                       os.environ.get("RESOURCE_GROUP_NAME"),
                                       os.environ.get("WORKSPACE_NAME"))

    # Upload the dataset to Azure ML Studio
    text_bert_intentions: Data = AzureData(azure_credential, cfg.data.processed_data_path,
                                           cfg.dataset.name, cfg.dataset.description).upload_data()

    # Create the cluster
    cpu_cluster: AmlCompute = AzureCluster(azure_credential, cfg.cluster.name, cfg.cluster.type, cfg.cluster.size,
                                           cfg.cluster.min_instances, cfg.cluster.max_instances,
                                           cfg.cluster.idle_time_before_scale_down, cfg.cluster.tier).create_cluster()

    # Create the environment
    pipeline_env: Environment = AzureEnvironment(azure_credential, cfg.environment.name,
                                                 f"{original_dir}/{cfg.environment.dependencies_dir}",
                                                 cfg.environment.version, cfg.environment.tags,
                                                 cfg.environment.description).create_environment()

    return azure_credential, text_bert_intentions, cpu_cluster, pipeline_env
