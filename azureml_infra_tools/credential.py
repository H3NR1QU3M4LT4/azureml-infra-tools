""" Azure Credential Class to authenticate with Azure Machine Learning Studio

Main functionalities:
The AzureCredential class provides authentication credentials for accessing Azure Machine Learning services. It uses the
DefaultAzureCredential class to obtain the necessary credentials and the MLClient class to create a client object that
can be used to interact with the Azure Machine Learning workspace specified by the subscription ID, resource group name,
and workspace name provided as parameters to the constructor. The class also includes a method to check the connection
to the workspace.

Methods:
- __init__: initializes the AzureCredential object and authenticates to the Azure Machine Learning workspace using the
provided credentials.
- check_connection: checks the connection to the Azure Machine Learning workspace and returns a list of workspace
objects.

Fields:
- credential: an instance of the DefaultAzureCredential class used to obtain the necessary credentials.
- ml_client: an instance of the MLClient class used to interact with the Azure Machine Learning workspace.
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
            logging.info('AzureCredential: Successfully authenticated to Azure Machine Learning workspace')
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
