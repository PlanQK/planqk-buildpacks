# PlanQK's buildpacks

This repository contains a set of builders and buildpacks designed to run managed services on PlanQK.
They are 100% compatible with [Cloud Native Buildpacks](https://buildpacks.io/).

## Additional tooling

The PlanQK's buildpacks project provides builder images suitable for use with
[pack](https://github.com/buildpacks/pack),
[kpack](https://github.com/pivotal/kpack),
[tekton](https://github.com/tektoncd/catalog/tree/HEAD/task/buildpacks/0.1),
[skaffold](https://github.com/GoogleContainerTools/skaffold/tree/HEAD/examples/buildpacks),
and other tools that support the Buildpacks v3 specification.

## Learn more about Cloud Native Buildpacks

This project implements the Cloud Native Buildpacks specification. 
To read more, see Cloud Native Buildpacks project
[documentation](https://buildpacks.io/docs/concepts).

For those new to buildpacks, these concepts are good starting points:

* **[Very quick Overview](https://stackoverflow.com/questions/70990289/are-cloud-native-buildpacks-just-an-automatic-way-to-perform-a-multi-stage-conta/71001310#71001310)**: There are a few concepts to keep in mind
* **[Builder](https://buildpacks.io/docs/concepts/components/builder)**: A container image that contains buildpacks and detection order in which builds are executed.
* **[Buildpack](https://buildpacks.io/docs/concepts/components/buildpack)**: An executable that "inspects your app source code and formulates a plan to build and run your application".
* **Buildpack Group**: Several buildpacks which together provide support for a
specific language or framework.
* **[Run Image](https://buildpacks.io/docs/concepts/components/stack)**: The container image that serves as the base for the built application.

## What you need to do

* A Procfile with the following minimum text: web: python (your_python_app.py)

This project supports several Python package services. PIP, miniconda and Poetry.

* PIP: create a valid requirements.txt at the of yout app. Source code triggers the pip installation process by the buildpack. The buildpack will install the application packages and make it available to the app.
* Miniconda: Miniconda is a package management and environment management system supported by the Python buildpack. The buildpack will create or update a conda environment from an environment.yml file or a package-list.txt file located at the root of the app source code.
Configuring a version of miniconda is not supported!
* Poetry: Poetry is a tool to manage both third-party application dependencies and virtual environments. Including a pyproject.toml file at the root of your app source code triggers the poetry installation process. The buildpack will invoke poetry to install the application dependencies defined in pyproject.toml and set up a virtual environment.
* For more information read: **[The Documentation](https://paketo.io/docs/howto/python/)**

