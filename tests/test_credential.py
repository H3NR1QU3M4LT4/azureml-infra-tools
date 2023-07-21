import pytest
import os

from azureml_infra_tools.credential import AzureCredential


class TestAzureCredential:
    #  Tests that AzureCredential successfully authenticates with valid credentials
    def test_valid_credentials(self):
        azure_cred = AzureCredential(os.environ.get("SUBSCRIPTION_ID"),
                                     os.environ.get("RESOURCE_GROUP_NAME"),
                                     os.environ.get("WORKSPACE_NAME"))
        assert len(azure_cred.check_connection()) != 0

    #  Tests that AzureCredential raises ValueError when subscription_id is missing
    def test_missing_subscription_id(self):
        with pytest.raises(ValueError):
            AzureCredential(resource_group_name='resource_group_name', workspace_name='workspace_name')

    #  Tests that AzureCredential raises ValueError when resource_group_name is missing
    def test_missing_resource_group_name(self):
        with pytest.raises(ValueError):
            AzureCredential(subscription_id='subscription_id', workspace_name='workspace_name')

    #  Tests that AzureCredential raises ValueError when workspace_name is missing
    def test_missing_workspace_name(self):
        with pytest.raises(ValueError):
            AzureCredential(subscription_id='subscription_id', resource_group_name='resource_group_name')

    #  Tests that AzureCredential raises ValueError when invalid credentials are provided
    def test_invalid_credentials(self, mocker):
        mocker.patch('azure.ai.ml.MLClient.workspaces', side_effect=Exception)
        with pytest.raises(ValueError):
            AzureCredential('subscription_id', 'resource_group_name', 'workspace_name')

    #  Tests that check_connection returns a list of workspace objects
    def test_check_connection(self):
        azure_cred = AzureCredential(os.environ.get("SUBSCRIPTION_ID"),
                                     os.environ.get("RESOURCE_GROUP_NAME"),
                                     os.environ.get("WORKSPACE_NAME"))
        assert len(azure_cred.check_connection()) == 1
