Test out the new binstar Build 
================================

**Warning:** There are only binstar-build conda packages for osx-64 and linux-64
This will not work on windows

**Warning:** If you get an error message like

    [BinstarError] Invalid queue build-binstar-continuum
    
Then you need to ask a binstar admin to add you to the `build-binstar-continuum` user
group
 
# Submitting your build to the queue

## Install binstar-build

    conda install -c binstar binstar-build

**Make sure** that you are on binstar-build version 0.7.1
 
    $ binstar-build -V
    binstar-build Command line client (version 0.7.0)
    
## Submit a build

```sh
binstar-build -s alpha submit \
    https://github.com/srossross/testci \
    --test-only 
    --queue build-binstar-continuum 
```

A breakdown of the submit command:
 
## The .binstar.yml file

The build script and platforms are controlled with a  [.binstar.yml](https://github.com/srossross/testci/blob/master/.binstar.yml) file,
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


### https://github.com/srossross/testci

Submit a build from the `srossross/testci` repository 

You can also build from a subdirectory and/or a branch of the repo 

    https://github.com/USERNAME/REPO#BRANCHNAME --sub-dir SUB_DIRECTORY
    
The following command is also valid:

```sh
binstar-build -s alpha submit \
    https://github.com/srossross/testci#test_sub_dir \
    --sub-dir recipe_dir
    --test-only 
    --queue build-binstar-continuum 
```



 *  **Warning:** `SUB_DIRECTORY` Must be a valid directory within your repo and `SUB_DIRECTORY`
Must contain a valid `.binstar.yml` file 
 *  **Warning:** only github.com urls are supported.
 
### --test-only

This tells the binstar build worker that this is just a test and it should not upload
any files to binstar.
 
### --queue build-binstar-continuum

This tells binstar what queue you want to use.  

The format is:

    build-QUEUE_OWNER-QUEUE_NAME

