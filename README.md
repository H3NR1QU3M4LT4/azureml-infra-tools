# azureml-infra-tools

`azureml-infra-tools` is a Python utility package designed to simplify and streamline your Azure Machine Learning (Azure ML) 
workflows. Our goal is to provide a set of high-level APIs that help set up Azure ML infrastructure, manage 
authentication, and handle datasets in an intuitive and user-friendly manner. 

Whether you are an AI researcher, a data scientist, or a machine learning engineer, `azuremlutils` can help you 
seamlessly leverage the power of Azure ML and accelerate your machine learning projects.

You can check the project in [GitHub page](https://github.com/H3NR1QU3M4LT4/azuremlutils).
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
Here is a simple example of how to use azureml-infra-tools:

```python
from azureml_infra_tools import setup_infrastructure

# Your original directory and configuration
original_dir = < Your
Original
Directory >
cfg = < Your
Hydra
Configuration >

# Setting up the infrastructure
azure_credential, data, compute, env = setup_infrastructure(cfg, original_dir)
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
