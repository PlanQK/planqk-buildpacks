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


## Development time 

*since we're using paketo buildpacks, the pack CLI is required
* **[pack CLI](https://buildpacks.io/docs/tools/pack/)**: Windows users might use Scoop for installation  
* Job_template_wrapper:  There must be a "job template" wrapper on the server that records the user code  
This wrapper must run very securely  
* a script must be written to enable the processes described in the runtime  
```bash

# Directory of the Usercode
USERCODE_DIR="/path/to/usercode"

# Directory for the Wrapper output
OUTPUT_DIR="/path/to/output"

# Name of the Docker Image
DOCKER_IMAGE_NAME="my_wrapper_image"

# Destination directory for the Usercode in the Wrapper
USERCODE_DESTINATION="$OUTPUT_DIR/app/user_code"

# Step 1: Copy the Wrapper code
cp -r ./wrapper/* $OUTPUT_DIR/

# Step 2: Create the directory for the Usercode in the Wrapper destination
mkdir -p $USERCODE_DESTINATION

# Step 3: Copy the specific Usercode to the Wrapper destination
cp -r $USERCODE_DIR/* $USERCODE_DESTINATION/

# Step 4: Change to the output directory
cd $OUTPUT_DIR

# Step 5: Optional - Perform specific configuration steps
# You can add more configurations, set environment variables, etc. here.

# Step 6: Use pack to build the Docker Image
pack build $DOCKER_IMAGE_NAME --builder <YOUR_BUILDER>

# Step 7: Optional - Publish the Docker Image (e.g., on Docker Hub)
# pack push $DOCKER_IMAGE_NAME

# Step 8: Optional - Start the container (if necessary)
# docker run -d $DOCKER_IMAGE_NAME

# Step 9: Optional - Clean up temporary files if needed
# rm -rf $OUTPUT_DIR

echo "Wrapper script completed!"
```

## run time 

First, the user code must be combined with the wrapper  
saving the result as a combined wrapper
this "combined" wrapper can then be built into an image using the pack command  
after creating the image, the combined wrapper must be deleted again
* Docker run:
```bash
PROJECT_ROOT=(`pwd`) 
docker run -it \
  -e BASE64_ENCODED=false \
  -v $PROJECT_ROOT/user-code-template/input/data.json:/var/input/data/data.json \
  -v $PROJECT_ROOT/user-code-template/input/params.json:/var/input/params/params.json \
```
docker image and container should be removed afterward

planqk 

## what should the cluster do

* tbh I have no clue yet

## What you need to do

* A Procfile with the following minimum text: web: python (your_python_app.py)

This project supports several Python package services. PIP, miniconda and Poetry.

* PIP: create a valid requirements.txt at the of yout app. Source code triggers the pip installation process by the buildpack. The buildpack will install the application packages and make it available to the app.
* Miniconda: Miniconda is a package management and environment management system supported by the Python buildpack. The buildpack will create or update a conda environment from an environment.yml file or a package-list.txt file located at the root of the app source code.
Configuring a version of miniconda is not supported!
* Poetry: Poetry is a tool to manage both third-party application dependencies and virtual environments. Including a pyproject.toml file at the root of your app source code triggers the poetry installation process. The buildpack will invoke poetry to install the application dependencies defined in pyproject.toml and set up a virtual environment.
* For more information read: **[The Documentation](https://paketo.io/docs/howto/python/)**

