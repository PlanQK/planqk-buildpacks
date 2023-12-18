## Basic Concepts

* A builder. A builder consists of a stack and one or more groups of buildpacks.
* A stack is a base build and run image.
* A buildpack is an OCI image with at least two binaries, detect and build.
* The lifecycle. The lifecycle responsible for running all of the builders.


## Development and Prerequisites

* since we're using paketo buildpacks, the pack CLI is required
* **[pack CLI](https://buildpacks.io/docs/tools/pack/)**:   
* create a builder
  * in a builder.toml all buildpacks and stacks neccessary for the builder must be defined.
  * [builder.toml docs](https://buildpacks.io/docs/reference/config/builder-config/)
  * navigate to the target folder containing the buildpack.toml ./planqk-base
  * make sure docker engine is running
  *  run the pack builder create command to create a builder 
  ```bash 
  pack builder create planqk-base-builder --config .\builder.toml
  ```
  * now you have an OCI image pack could use as builder 
  ```bash 
  pack build test_img --path /planqk-buildpacks/conda/sample --builder planqk-base-builder
  ```
  * you can run this test_img via:
  ```bash
    docker run -it -e PORT=8080 -p 8080:8080 test_img
  ```
  * now run localhost:8080 on your browser
* create the base image that starts the user code. hereinafter referred to ass wrapper 
* the wrapper must contain a Procfile
  * Procfile takes key value pairs
  * it must contain the following line
  ```bash
  web : python -m app.py
  ```




## PlanQK Platform

* the user code must be combined with the wrapper
  *[wrapper location:](https://gitlab.com/StoneOne/planqk/serverless-template/-/tree/main/job-template?ref_type=heads)
  * User code must copied to following path:

  ```bash
  \serverless-template\job-template\app\user_code
  ``` 
  *  saving the result as a combined wrapper
  * this "combined" wrapper can then be built into an OCI image using the pack build command from the job-template level
  ```bash
  pack build user-job --builder planqk-base-builder
  ```
* after creating the image, the combined wrapper must be deleted again


## Kubernetes (Docker Runtime)



* Docker run:
```bash
PROJECT_ROOT=(`pwd`) 
docker run -it \
  -e BASE64_ENCODED=false \
  -v $PROJECT_ROOT/user-code-template/input/data.json:/var/input/data/data.json \
  -v $PROJECT_ROOT/user-code-template/input/params.json:/var/input/params/params.json \
```
docker image and container should be removed afterward