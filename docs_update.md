# Why Buildpacks

Status qou was that:

users of the platform can have their projects processed as Docker images. This currently requires a Conda environment and an environment.yml as well as a Dockerfile. To enable more flexibility, pip and poetry will also be supported. In addition, the process can be serialized and simplified with buildpacks. The users then no longer need a docker file and can continue to use their resources for our platform.

All the user has to do is upload a zip file with their code to the platform. The rest happens in the background for the user. 

To execute a user job, the project is copied into a serverless user template. The template contains a run method and all necessary implementations to process the data of the job. This is necessary to create as few barriers as possible for the user and to minimize sources of error.  
The build process is always started from the job template level. This directory then becomes the first app level in the docker image.  


```bash
serverless-template/
├── job-template/
│   ├── app/
│   │    ├──user-code
│   ├── tests/
│   └── ...
├── dockerfile-template/
│   │   └── ...
└── ...

 ```
However, the use of buildpacks results in changes. The requirements were previously stored in the user-code directory. These must now be saved at the job-template directory. Instead of the Dockerfile, a Procfile is now required to start the app. When building the container, the docker engine only looks at the first level of the image. Procfile and all requirements must be saved here. It is no longer possible to have a requirements.txt and an environment.yml in the directory.  This is because the buildpack will always use pip first. If a conda environment is desired, no requirements.txt must be present. 


With the buildpacks, we can set up the platform more broadly. They are variable and can be extended to languages other than Python if required. They reduce barriers and enable faster and direct access to quantum computing without having to deal with Docker.

# Creating and using a Python builder - an example

Cloud native buildpacks provide their own CLI. This can be obtained from their website (insert link).  
The pack CLI, the planqk CLI  and Docker are required for the example process. 

 * create the builder
 * use the builder on the test image to test the image
 * docker run befehl
 * go to local host



# starting a job with buildpacks

* load your project to the job template - app/user-code. planqk init nachlesen
* go to job template layer
* check for requirements.txt OR environment.yml at the job template layer 
* check for procfile
* start building process


* problems : As the build process is started at job-template level, the requirements must also be saved there. However, these come from the user code and must then be moved from there. This makes an additional implementation necessary.


* docker run, path for json must be correct!