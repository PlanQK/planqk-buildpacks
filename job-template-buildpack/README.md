# PlanQK Job Template Buildpack

The Planqk Job template Buildpack is a Anaqor Buildpack that turns User servives into executable images for the planqk platform.
This buildpack must be present in a builder together with the Python buildpack.

## Behavior

This buildpack will participate if all of the following conditions are met:

* The root directory contains a planqk.json
<!---
* The root directory contains a requirements.txt OR environment.yml
--->
Te Buildpack will do the following:

The buildpack integrates the user service into the job template and installs the necessary requirements from a requirements.txt file.


## local testing

```bash
pack buildpack package planqk-buildpack-job-template --config ./package.toml
```



## integration in a Builder


## Configuraton

Environment variable | Description 
  -----------------  | -----------
$BP_GITLAB_TOKEN     | Sets a Gitlab token so that the required repsitory can be downloaded

