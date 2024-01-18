# PlanQK Job Template Buildpack


The Buildpack allows PlanQK coding projects to be packaged into Docker images to run on the PlanQK Platform.
This buildpack must be present in a Builder together with the Python Buildpack.
In this case the Buildpack/python from Paketo was used.


## Configuraton

Environment variable | Description 
  -----------------  | -----------
$BP_GITLAB_TOKEN     | Sets a Gitlab token so that the required repsitory can be downloaded



## Behavior

This buildpack will participate if all of the following conditions are met:

* The root directory contains a planqk.json
<!---
* The root directory contains a requirements.txt OR environment.yml
--->


Every project that is to run on the PlanQK Platform must be provided with a program.py.
A run method must be implemented in this program.py.
A wrapper is therefore required to start the runtime.
This wrapper is called "job-template" on the PlanQk Platform and will start the run method.
This Buildpack was created to integrate the job-template into the build process of the Builder.

The Buildpack will do the following:  

The detect phase checks whether the project contains a planqk.json in the root directory.
If no planqk.json is present, the build process is terminated with the error message: "Could not find 'planqk.json' file".
Otherwise the build process is started.
The build process starts by reading the environment variable for a Gitlab token. 
Then a layer is created and the job-template repository is copied into this layer with the help of the token.
The $ENTRY_POINT and the $PYTHONPATH are then exposed.
```bash
# expose environment variables
mkdir -p ${serverless_template_layer}/env.launch
echo -n "src.program:run" > "${serverless_template_layer}/env.launch/ENTRY_POINT"
echo -n ":$serverless_template_layer/job-template" > "${serverless_template_layer}/env.launch/PYTHONPATH.append"

```
Finally, the start command is defined.
```bash
# set default start command
cat <<EOF > "${CNB_LAYERS_DIR}/launch.toml"
[[processes]]
type = "web"
command = ["python", "-m", "app"]
default = true
EOF

```

With these settings, the Buildpack/Procfile package can no longer be supported. 
This would overwrite the variables stored in the build script.


## Builpack packaging

```bash
pack buildpack package planqk-buildpack-job-template --config ./package.toml
```



## integration in a Builder

To integrate the Buildpack into a Builder, it must be added to the builder.toml.
The example is based on a locally saved Buildpack. 


```bash
# builder.toml

[[buildpacks]]
uri = "docker://gcr.io/paketo-buildpacks/python:2.14.0"
version = "2.14.0"

[[buildpacks]]
uri = path/to_the_local_job_template_buildpack.toml


[[order]]
    [[order.group]]
    id = "paketo-buildpacks/python"

    [[order.group]]
    id = "planqk-buildpacks/job-template"

```
This example shows a builder.toml from which a Builder is generated consisting of the Python Buildpack and a costum Buildpack.  
  
Note for Windows users:  
be sure to use double "\\" in the uri 


