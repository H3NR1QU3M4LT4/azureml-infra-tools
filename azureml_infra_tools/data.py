""" Azure Data Class to upload data to Azure Machine Learning Studio

Main functionalities:
The AzureData class is designed to upload data to Azure Machine Learning Studio. It takes an AzureCredential object as
input to authenticate with the Azure Machine Learning Studio. The class allows users to upload data to the studio and
reuse existing datasets if they already exist.

Methods:
- __init__(self, azure_credential: AzureCredential, data_path: str, data_name: str, data_description: str, data_version:
str): Initializes the AzureData object with the given parameters.
- upload_data(self) -> Data: Uploads data to Azure Machine Learning Studio and returns the Azure Data object.

Fields:
- azure_credential: An AzureCredential object used to authenticate with Azure Machine Learning Studio.
- data_path: The path to the data to be uploaded.
- data_name: The name of the dataset.
- data_description: A description of the dataset.
- data_version: The version of the dataset.
"""

from azure.ai.ml.constants import AssetTypes
from azure.ai.ml.entities import Data
import logging

from azureml_infra_tools.credential import AzureCredential


class AzureData:
    """Azure Data Class
    @param azure_credential: (AzureCredential) An AzureCredential object used to authenticate with Azure Machine
    Learning Studio.
    @param data_path: (str) The path to the data to be uploaded.
    @param data_name: (str) The name of the dataset.
    @param data_description: (str) A description of the dataset.
    @param data_version: (str) The version of the dataset.
    """
    data_version: str

    def __init__(self, azure_credential: AzureCredential, data_path: str, data_name: str,
                 data_description: str, data_version: str):
        self.azure_credential = azure_credential
        self.data_path = data_path
        self.data_name = data_name
        self.data_description = data_description
        self.data_version = data_version

    def upload_data(self) -> Data:
        """Upload data to Azure Machine Learning Studio
        @return: Azure Data
        """
        try:
            azure_data = self.azure_credential.ml_client.data.get(name=self.data_name, version=self.data_version)
            logging.info(f"You already have a dataset named {self.data_name}, with the version "
                         f"{self.data_version} we'll reuse it as is.")
            return azure_data
        except Exception:
            logging.info("Uploading data to Azure Machine Learning Studio...")
            azure_data = Data(
                name=self.data_name,
                version=self.data_version,
                description=self.data_description,
                path=self.data_path,
                type=AssetTypes.URI_FILE,
            )
            self.azure_credential.ml_client.data.create_or_update(azure_data)
            logging.info("Data uploaded successfully!")

            return azure_data
