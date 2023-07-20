""" Azure Data Class to upload data to Azure Machine Learning Studio
"""
from azure.ai.ml.constants import AssetTypes
from azure.ai.ml.entities import Data

from azuremlutils.credential import AzureCredential


# import time


class AzureData:
    """Azure Data Class
    @param azure_credential: Azure Machine Learning client
    @param data_path: (str) Path to data
    @param dataset_name: (str) Name of dataset
    @param dataset_description: (str) Description of dataset
    @param data_version: (str) Version of dataset
    """
    data_version: str

    def __init__(self, azure_credential: AzureCredential, data_path: str, dataset_name: str,
                 dataset_description: str):
        self.azure_credential = azure_credential
        self.data_path = data_path
        self.dataset_name = dataset_name
        self.dataset_description = dataset_description
        # self.data_version = time.strftime("%Y.%m.%d.%H-%M-%S", time.gmtime())
        self.data_version = "2023.07.11.14-33-41"

    def upload_data(self) -> Data:
        """Upload data to Azure Machine Learning Studio
        @return: Azure Data
        """
        try:
            azure_data = self.azure_credential.ml_client.data.get(name=self.dataset_name, version="2023.07.11.14-33-41")
            print(f"You already have a dataset named {self.dataset_name}, with the version "
                  f"{self.data_version} we'll reuse it as is.")
            return azure_data
        except Exception:
            print("Uploading data to Azure Machine Learning Studio...")
            azure_data = Data(
                name=self.dataset_name,
                version=self.data_version,
                description=self.dataset_description,
                path=self.data_path,
                type=AssetTypes.URI_FILE,
            )
            self.azure_credential.ml_client.data.create_or_update(azure_data)
            print("Data uploaded successfully!")

            return azure_data