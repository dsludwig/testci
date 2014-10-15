Test out the new binstar Build with Docker
===========================================


The New binstar docker worker runs your linux-64 builds in docker containers. You can upload your own docker container to [docker hub](https://hub.docker.com) and use it for the base image to your your builds.

Why docker builds?

 1. Customize your build box. [doc](#use-your-own-docker-container)
 2. Test your builds locally. With docker it is easy to reproduce the build locally
 3. Test in isolation. Each test start from the original container state. Your new builds will not be affected by past builds.
 

**Warning:** If you get an error message like

    [BinstarError] Invalid queue build-binstar-docker
    
Then you need to ask a binstar admin to add you to the `build-binstar-docker` user
group
 
# Submitting your build to the queue

## Install binstar-build

    conda install -c binstar binstar-build

**Make sure** that you are on binstar-build version >=0.8
 
    $ binstar-build -V
    binstar-build Command line client (version 0.8.3)
    
## Submit a build

```sh
binstar-build -s alpha submit \
    https://github.com/binstar/testci \
    --test-only \
    --sub-dir docker_test \
    --queue build-binstar-docker
```

A breakdown of the submit command:
 
## The .binstar.yml file

The build script and platforms are controlled with a  [.binstar.yml](https://github.com/Binstar/testci/blob/master/docker_test/.binstar.yml) file,
Check out the in-line comments for what the submit command is doing behind the scenes.

### -s alpha

This tells the binstar-build command line to use the [alpha binstar site](http://alpha.binstar.org)
 
To make this your default, run 

    binstar config --set default_site alpha
    
**Note: ** if you set alpha as your default site you can always 
use the [main binstar site](http://binstar.org) with:
 
    binstar-build -s binstar ...
    
or

    binstar -s binstar ...


### https://github.com/binstar/testci --sub-dir docker_test

Submit a build from the `binstar/testci` repository, the build will clone the repository and imidiatly cd into the docker_test directory

 *  **Warning:** only github.com urls are supported.
 
### --test-only

This tells the binstar build worker that this is just a test and it should not upload
any files to binstar.
 
### --queue build-binstar-docker

This tells binstar what queue you want to use.  The `build-binstar-docker` queue contains workers that know about docker.

The format is:

    build-QUEUE_OWNER-QUEUE_NAME

# Use your own docker container

 1. Go to the [docker hub](https://hub.docker.com) and sign up for a new account.
 1. Create a new image from the binstar/linux-64 image. 
     1. Create a `Dockerfile`: 
        ```
        FROM binstar/linux-64
        
        MAINTAINER You <your@email>
        
        RUN install my base software
        ...
        ```
     1. Build your image: `docker build .`
     1. Tag your image: `docker build <IMAGE-ID> docker-account/image-name`
     1. Push your image to docker hub: `docker push docker-account/image-name`
 1. Use your image in your next build by editing your
    [.binstar.yml](https://github.com/Binstar/testci/blob/master/docker_test/.binstar.yml) file. Set the a yaml tag `docker_image` to `docker-account/image-name`
 1. Now submit your job


