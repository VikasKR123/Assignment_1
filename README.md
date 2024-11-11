# Task:
### "Create your own Python module for any application (e.g., a calculator). Create a wheel package of this module, install the module, and test it. When installing the wheel package, it should also automatically install its dependencies."

# Overview of the Application:
To achieve the above task, I selected a toxic comment classification application. This application takes input from the user and classifies the comment as either toxic or non-toxic. If a comment is toxic, it further classifies it into categories like threat, insult, or other types.

# Steps:
Project Setup: I created a folder containing all the necessary code for toxic comment classification, including the model file and an __init__.py file to ensure the project is recognizable by find_packages() (which will be specified in setup.py).

Setup File: I defined a setup.py file outside the project directory. This file facilitates creating and distributing the Python package.

# Workflow (How it Works Internally):
> When I run python3 setup.py sdist bdist_wheel, the first step is that Python reads setup.py, which contains the setuptools function. This function provides essential metadata, listing all necessary packages, subpackages, and version requirements for the project. The function reads this configuration to set up the package environment for distribution.

> The sdist command stands for "source distribution." In this step, setuptools gathers all the required files in the project, including __init__.py, source code files (.py), and additional files like the stored model. This ensures that all resources required for the package are included in the distribution. find_packages() in setup.py scans project directories for folders with __init__.py, identifying them as packages and including them in the distribution.

> The bdist_wheel command triggers the "binary distribution" phase, where the package is compiled into a wheel file. Wheels are the preferred format for Python package installations as they do not require compilation on the user's system, making installations faster and more efficient.

> After executing this command, two types of files are created in the dist/ directory: a .tar.gz file (source distribution) and a .whl file (wheel distribution). Once created, the package can be installed using pip install from the dist directory. After installation, the package is ready to use anywhere on the system.


![Screenshot from 2024-11-10 09-57-44](https://github.com/user-attachments/assets/75021e9c-8ada-4489-965a-de351b470c1a)


![as1](https://github.com/user-attachments/assets/a5818346-91bb-4533-a72f-5207b3af9f50)

