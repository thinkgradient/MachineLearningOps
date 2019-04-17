# Introduction to Machine Learnin Operationalization using Azure Machine Learning Services
This series of labs introduces core features of Azure Machine Learning (AML) service and demonstrates how AML service can be used to orchestrate machine learning workflows. The labs walk you through the key phases of a machine learning workflow: from data preparation, through model selection and tuning, to model operationalization. It concludes with a lab on Automated Machine Learning. There is an optional Model Interpretability lab which you can run through as well.



## Lab environment set up

The Azure Machine Learning service is platform agnostic. The only requirements for your development environment are Python 3, Conda (for isolated environments), and a configuration file that contains your Azure Machine Learning workspace information.

The following development environments are supported: 
- **Azure Notebooks**
- **The Data Science Virtual Machine**
- **Jupyter Notebooks**
- **Visual Studio Code**
- **Visual Studio**
- **PyCharm**
- **Azure Databricks**

However, for the purpose of this lab we will set up your lab environment in your local machine (PC or Laptop). These are the pre-requisites in terms of software and libraries in order to execute each of these labs:

Windows/Mac/Linux 
 **Please make sure you have the latest version of Anaconda installed https://www.anaconda.com/distribution/#download-section**
 **Install the following libraries**
 ***pip install --upgrade azureml-sdk[explain,automl]***
 ***pip install azureml-widgets***
 


### To provision Azure Data Science Virtual Machine

1. Follow the instructions at

https://ms.portal.azure.com/#create/microsoft-ads.linux-data-science-vm-ubuntulinuxdsvmubuntu


1. After the DSVM is provisioned connect to the pre-installed Jupyter server at:

`https://<your IP address or DNS>:8000`
  
1. In Jupyter open a terminal and clone this repository under the `notebooks` folder.
```
cd notebooks
git clone https://github.com/jakazmie/MTC_AzureAILabs.git
```

1. If you need to update the DSVM to install/update Python libraries - E.g. Azure ML SDK.
```
sudo -i
source activate py36
# update packages
exit
```


1. Follow the instructor who will walk you through the labs.

