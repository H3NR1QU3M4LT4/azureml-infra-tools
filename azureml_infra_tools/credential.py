""" Azure Credential Class to authenticate with Azure Machine Learning Studio
"""
import logging
from azure.ai.ml import MLClient

from azure.identity import DefaultAzureCredential


def _validate_input(subscription_id, resource_group_name, workspace_name):
    if not subscription_id or subscription_id == '':
        raise ValueError('subscription_id is required')
    if not resource_group_name or resource_group_name == '':
        raise ValueError('resource_group_name is required')
    if not workspace_name or subscription_id == '':
        raise ValueError('workspace_name is required')


class AzureCredential:
    """Azure Credential Class
    The AzureCredential class is designed to provide authentication credentials for accessing Azure Machine Learning
    services. It uses the DefaultAzureCredential class from the 'azure.identity' module to obtain the necessary
    credentials. The MLClient class from the azure.ai.ml module is then used to create a client object that can be
    used to interact with the Azure Machine Learning workspace specified by the subscription ID, resource group name,
    and workspace name provided as parameters to the constructor.
    @param subscription_id: (str) Azure subscription ID
    @param resource_group_name: (str) Azure resource group name
    @param workspace_name: (str) Azure Machine Learning workspace name
    """

    def __init__(self, subscription_id: str = None,
                 resource_group_name: str = None,
                 workspace_name: str = None):
        self.credential = DefaultAzureCredential()
        _validate_input(subscription_id, resource_group_name, workspace_name)
        try:
            self.ml_client = MLClient(
                credential=self.credential,
                subscription_id=subscription_id,
                resource_group_name=resource_group_name,
                workspace_name=workspace_name,
            )
            logging.debug('AzureCredential: Successfully authenticated to Azure Machine Learning workspace')
        except Exception as e:
            logging.exception('AzureCredential: Failed to authenticate to Azure Machine Learning workspace', e)
            raise ValueError('Invalid Azure credentials')

        if self.check_connection() is None:
            logging.exception('AzureCredential: Failed to authenticate to Azure Machine Learning workspace')
            raise ValueError('Invalid Azure credentials')

    def check_connection(self):
        """Checks the connection to the Azure Machine Learning workspace.
        @return: a list of workspace objects
        """
        try:
            workspaces = self.ml_client.workspaces.list()
            workspace_list = list(workspaces)
            if not workspace_list:
                return None
            return workspace_list
        except Exception:
            return None
