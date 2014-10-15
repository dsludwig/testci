Test out the new binstar Build with Docker
===========================================

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
    --test-only
    --sub-dir docker_test
    --queue build-binstar-docker
```

A breakdown of the submit command:
 
## The .binstar.yml file

The build script and platforms are controlled with a  [.binstar.yml](https://github.com/binstar/testci/blob/master/.binstar.yml) file,
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

