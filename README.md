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

* **[Builder](https://buildpacks.io/docs/concepts/components/builder)**: A container image that contains buildpacks and detection order in which builds are executed.
* **[Buildpack](https://buildpacks.io/docs/concepts/components/buildpack)**: An executable that "inspects your app source code and formulates a plan to build and run your application".
* **Buildpack Group**: Several buildpacks which together provide support for a
specific language or framework.
* **[Run Image](https://buildpacks.io/docs/concepts/components/stack)**: The container image that serves as the base for the built application.
