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

Windows/Mac/Linux:
 
- **Please make sure you have the latest version of Anaconda installed https://www.anaconda.com/distribution/#download-section**
- **Install the following libraries**
 - ***pip install --upgrade azureml-sdk[explain,automl]***
 - ***pip install azureml-widgets***

For Windows users (additional steps below):

- **Install git https://github.com/git-for-windows/git/releases/download/v2.21.0.windows.1/Git-2.21.0-64-bit.exe**
- **Install wget http://downloads.sourceforge.net/gnuwin32/wget-1.11.4-1-setup.exe**
- **Make sure to add wget to your Path environment variables**

For Mac users (additional steps below):

- **Install wget: brew update && brew install wget** 

## Redeem your Azure account promo code

The steps below outline how you can redeem your promo code and create your new Azure account. However, if you already have an Azure account please feel free to use that as that is the preferred option. Alternatively, follow the steps below to create a new one using the promo codes we have provided you. Note, the accounts with the promo code will expire after 7 days and they come with a $50 limit.

1. You need to have an .outlook or .live account. Please create one if you don't have it.
2. Then follow the instructions here to redeem your promo code and create your Azure account: https://www.microsoftazurepass.com/Home/HowTo


## Create Azure Machine Learning service workspace

Once you have access to an Azrue account follow the steps below to create an Azure Machine Learning workspace.

1. In your Azure portal, click **Create a resource**
2. In the **Search the Marketplace** textbox, type: ***Machine Learning*** and select **Machine Learning service workspace** from the drop down list.
3. In the next screen click the button **Create**
4. You only need to fill Workspace name, Resource group, and Location.
5. For **Workspace name** give it a name (e.g. MLOpsYourName)
6. For **Resource group** give it a name (e.g. MLOpsYourNameRGR)
7. For **Location** please select: West Europe




