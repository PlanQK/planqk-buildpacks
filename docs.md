## Development time 

*since we're using paketo buildpacks, the pack CLI is required
* **[pack CLI](https://buildpacks.io/docs/tools/pack/)**: Windows users might use Scoop for installation  
* create a builder
* * in a builder.toml all buildpacks and stacks neccessary for the builder must be defined.
* * [builder.toml docs](https://buildpacks.io/docs/reference/config/builder-config/)
* * run the pack build command to create a builder 
```bash 
pack builder create <image-name> --config <builder-config-path> [flags]
```
* * now you have an OCI image pack could use as builder 
```bash 
pack build test_img --path apps/test-app --builder <your_builder>
```
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