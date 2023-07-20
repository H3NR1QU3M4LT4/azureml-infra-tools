# azuremlutils
azuremlutils is a Python utility package aimed at simplifying and streamlining workflows on Azure Machine Learning 
(Azure ML). It provides a set of high-level APIs that make it easy to set up Azure ML infrastructure such as clusters 
and environments, authenticate with Azure ML, and manage datasets. This package is designed with a focus on 
user-friendliness and efficiency, allowing users to achieve complex Azure ML tasks with minimal code. Whether you are 
an AI researcher, a data scientist, or a machine learning engineer, azuremlutils can help you seamlessly leverage the 
power of Azure ML and accelerate your machine learning projects.

## Installation

You can install the `azuremlutils` package via pip:

```shell
pip install azuremlutils
```

Or via poetry:

```shell
poetry add azuremlutils
```

## Usage
Here is a simple example of how to use azuremlutils:

```python
from azuremlutils import setup_infrastructure

# Your original directory and configuration
original_dir = <Your Original Directory>
cfg = <Your Configuration>

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