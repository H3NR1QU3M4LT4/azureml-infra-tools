""" Azure Credential Class to authenticate with Azure Machine Learning Studio
"""
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential


class AzureCredential:
    """Azure Credential Class
    @param subscription_id: (str) Azure subscription ID
    @param resource_group_name: (str) Azure resource group name
    @param workspace_name: (str) Azure Machine Learning workspace name
    """

    def __init__(self, subscription_id: str = None,
                 resource_group_name: str = None,
                 workspace_name: str = None):
        self.credential = DefaultAzureCredential()
        self.ml_client = MLClient(
            credential=self.credential,
            subscription_id=subscription_id,
            resource_group_name=resource_group_name,
            workspace_name=workspace_name,
        )
