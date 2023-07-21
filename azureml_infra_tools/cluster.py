""" Cluster Class to create Azure Machine Learning Studio cluster
"""
from azure.ai.ml.entities import AmlCompute

from azureml_infra_tools.credential import AzureCredential


class AzureCluster:
    """Create the cluster
    :param azure_credential: (AzureCredential) azureml_infra_tools credential
    :param compute_name: (str) compute name
    :param compute_type: (str) compute type
    :param size: size
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
            print(
                f"You already have a cluster named {self.compute_name}, we'll reuse it as is."
            )

            return cpu_cluster

        except Exception:
            print("Creating a new cpu compute target...")
            cpu_cluster = AmlCompute(
                name=self.compute_name,
                type=self.compute_type,
                size=self.size,
                min_instances=self.min_instances,
                max_instances=self.max_instances,
                idle_time_before_scale_down=self.idle_time_before_scale_down,
                tier=self.tier,
            )
            print(
                f"AMLCompute with name {cpu_cluster.name} will be created, with compute size "
                f"{cpu_cluster.size}")
            self.azure_credential.ml_client.compute.begin_create_or_update(
                cpu_cluster)

            print(
                "Azure Machine Learning Compute cluster created successfully!")

            return cpu_cluster
