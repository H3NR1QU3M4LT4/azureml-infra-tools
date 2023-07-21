from setuptools import setup, find_packages

setup(
    name="azureml-infra-tools",
    version="0.1.0",
    packages=find_packages(),
    url="https://github.com/H3NR1QU3M4LT4/azureml-infra-tools.git",
    author="Henrique Malta",
    author_email="vlezyitalia@gmail.com",
    description="azureml-infra-tools is a Python package providing high-level APIs for Azure Machine Learning. "
                "It simplifies setup of Azure ML infrastructures, manages datasets, and streamlines authentication. "
                "Designed for AI researchers, data scientists, and ML engineers, it boosts productivity and "
                "accelerates Azure ML projects.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "python-dotenv",
        "azure-ai-ml",
        "azure-identity"
    ],
)
