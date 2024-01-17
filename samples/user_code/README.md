# PlanQK User Code Sample

## Prerequisites

- [Docker](https://docs.docker.com/get-docker)
- [pack](https://buildpacks.io/docs/tools/pack)
- Builder [`planqk-base`](../../planqk-base) must exist
- Buildpack [`planqk-buildpack-job-template`](../../planqk-buildpack-job-template) must exist

## Packaging

```bash
pack build testapp --builder planqk-base --buildpack planqk-buildpack-job-template --env BP_GITLAB_TOKEN=<your token value>

# or
pack build testapp --builder planqk-base --buildpack ../../job-template-buildpack --env BP_GITLAB_TOKEN=<your token value>

# or run it together with the Python buildpack
pack build testapp --builder planqk-base --buildpack docker://gcr.io/paketo-buildpacks/python:2.14.0 --buildpack ../../job-template-buildpack --env BP_GITLAB_TOKEN=<your token value>
```

## Running

```bash
docker run -it --rm testapp

# or

docker run -it --rm --entrypoint launcher testapp bash
```
