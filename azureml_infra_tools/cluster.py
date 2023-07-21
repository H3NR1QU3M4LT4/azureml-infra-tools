""" Cluster Class to create Azure Machine Learning Studio cluster
Main functionalities:
The AzureCluster class is designed to create and manage an Azure Machine Learning compute cluster. It takes in an
AzureCredential object, compute name, compute type, size, minimum and maximum instances, idle time before scale down,
and tier as parameters to create a new cluster or reuse an existing one.

Methods:
- __init__: Initializes the AzureCluster object with the given parameters.
- create_cluster: Creates a new compute cluster or reuses an existing one with the given parameters.

Fields:
- azure_credential: An AzureCredential object used for authentication.
- compute_name: The name of the compute cluster.
- compute_type: The type of the compute cluster.
- size: The size of the compute cluster.
- min_instances: The minimum number of instances for the compute cluster.
- max_instances: The maximum number of instances for the compute cluster.
- idle_time_before_scale_down: The idle time before scaling down the compute cluster.
- tier: The tier of the compute cluster.
"""

from azure.ai.ml.entities import AmlCompute
import logging

from azureml_infra_tools.credential import AzureCredential


class AzureCluster:
    """Create the cluster
    :param azure_credential: (AzureCredential) azureml_infra_tools credential
    :param compute_name: (str) compute name
    :param compute_type: (str) compute type
    :param size: size of the compute cluster
    :param min_instances: min instances
    :param max_instances: max instances
    :param idle_time_before_scale_down: idle time before scale down
    :param tier: tier
    """

    def __init__(self, azure_credential: AzureCredential, compute_name: str,
                 compute_type: str, size: str, min_instances: int,
                 max_instances: int, idle_time_before_scale_down: int,
                 tier: str):
        self.azure_credential = azure_credential
        self.compute_name = compute_name
        self.compute_type = compute_type
        self.size = size
        self.min_instances = min_instances
        self.max_instances = max_instances
        self.idle_time_before_scale_down = idle_time_before_scale_down
        self.tier = tier

    def create_cluster(self) -> AmlCompute:
        """Create the cluster
        :return: cpu_cluster
        """
        try:
            cpu_cluster = self.azure_credential.ml_client.compute.get(
                self.compute_name)
            logging.info(
                f"You already have a cluster named {self.compute_name}, we'll reuse it as is."
            )

            return cpu_cluster

        except Exception:
            logging.info("Creating a new cpu compute target...")
            cpu_cluster = AmlCompute(
                name=self.compute_name,
                type=self.compute_type,
                size=self.size,
                min_instances=self.min_instances,
                max_instances=self.max_instances,
                idle_time_before_scale_down=self.idle_time_before_scale_down,
                tier=self.tier,
            )
            logging.info(
                f"AMLCompute with name {cpu_cluster.name} will be created, with compute size "
                f"{cpu_cluster.size}")
            self.azure_credential.ml_client.compute.begin_create_or_update(
                cpu_cluster)

            logging.info(
                "Azure Machine Learning Compute cluster created successfully!")

            return cpu_cluster
