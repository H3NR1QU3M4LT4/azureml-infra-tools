# azureml-infra-tools

`azureml-infra-tools` is a Python utility package designed to simplify and streamline your Azure Machine Learning (Azure 
ML) workflows. Our goal is to provide a set of high-level APIs that help set up Azure ML infrastructure, manage 
authentication, and handle datasets in an intuitive and user-friendly manner. 

Whether you are an AI researcher, a data scientist, or a machine learning engineer, `azureml-infra-tools` can help you 
seamlessly leverage the power of Azure ML and accelerate your machine learning projects.

You can check the project in [GitHub page](https://github.com/H3NR1QU3M4LT4/azureml-infra-tools).
Also, you can find more information about Azure ML [here](https://azure.microsoft.com/en-us/services/machine-learning/).


## Installation

You can install the `azureml-infra-tools` package via pip:

```shell
pip install azureml-infra-tools
```

Or via poetry:

```shell
poetry add azureml-infra-tools
```


## Usage


### Simple usage

Here is a simple example of how to use azureml-infra-tools:

```python
from azureml_infra_tools import setup_infrastructure
import hydra
from omegaconf import DictConfig

@hydra.main(version_base="1.2", config_path="conf", config_name="config")
def main(cfg: DictConfig):
    """ Main function to run the pipeline
    @param cfg: hydra configuration file
    """
    # get original directory of the root of the project
    original_dir = hydra.utils.get_original_cwd()

    # create o setup with environment to run pipeline, client, cluster and data
    azure_credential, data_asset, cpu_cluster, pipeline_env = setup_infrastructure(cfg, original_dir)
```

Example of hydra configuration file:

```yaml
data:
  name: rpa-chatbot-assistant-intentions-csv
  description: RPA Chatbot Assistant Intentions
  version: 0.1.0
  data_path: data/processed/data.csv

cluster:
  name: rpachat-cluster-m60
  type: amlcompute
  size: Standard_NV6
  min_instances: 0
  max_instances: 18
  idle_time_before_scale_down: 180
  tier: Dedicated

environment:
  name: rpachat-custom-env
  dependencies_dir: src/dependencies
  version: 1.2.0
  tags: { "datasets": "2.13.1", "transformers": "4.30.2", "torch": "2.0.1" }
  description: Custom environment for RPA Chatbot Assistant Intentions pipeline
```


### Advanced usage

Here is an advanced example of how to use azureml-infra-tools:

```python
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
```

NOTE: In both cases you need to create a .env file with SUBSCRIPTION_ID, RESOURCE_GROUP_NAME and WORKSPACE_NAME. 
Then gather the information from the .env file and pass it to the AzureCredential class as follows: 

```python
import os
from dotenv import load_dotenv

load_dotenv()

os.environ.get("SUBSCRIPTION_ID")
os.environ.get("RESOURCE_GROUP_NAME")
os.environ.get("WORKSPACE_NAME")
```

Please note that you need to provide your own directory and configuration parameters.


# Contributing

We appreciate all contributions. If you're planning to contribute back bug-fixes, please create an issue describing the 
bug. If you plan to contribute new features, utility functions, or extensions, please first open an issue and discuss 
the feature with us.


# License

This project is licensed under the MIT License - see the LICENSE.md file for details.

Please modify the contents to better match your project requirements and details. For instance, you might want to add 
more usage examples, a section about the project's dependencies, instructions for how to run tests, etc.


# Versioning

The versioning system that we use is known as semantic versioning (SemVer). It's a versioning scheme for software 
that aims to convey meaning about the underlying changes in a release.

In general, SemVer's structure is MAJOR.MINOR.PATCH, where:

* MAJOR version increments indicate incompatible API changes.
* MINOR version increments indicate the addition of functionality in a backwards-compatible manner.
* PATCH version increments indicate backwards-compatible bug fixes.
For the versions available, see the tags on this repository.


# Contact
For more information on this project, you can visit the project's [GitHub page](https://github.com/H3NR1QU3M4LT4/azureml-infra-tools).
