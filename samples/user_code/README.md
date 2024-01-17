# PlanQK User Code Sample

## Prerequisites

- [Docker](https://docs.docker.com/get-docker)
- [pack](https://buildpacks.io/docs/tools/pack)
- Builder [`planqk-base`](../../planqk-base) must exist
- Buildpack [`planqk-buildpack-job-template`](../../planqk-buildpack-job-template) must exist

## Packaging

```bash
pack build testapp --builder planqk-base --buildpack planqk-buildpack-job-template
```
