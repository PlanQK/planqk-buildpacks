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
```
