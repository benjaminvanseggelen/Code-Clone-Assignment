# Code clone assignment 2IMP25
Repository for the code clone assignment, containing a Docker project that clones the relevant version of jQuery, and sets up a working copy of JsInspect. Forked from the provided template repository.

This repository is publicly available [here](https://github.com/benjaminvanseggelen/Code-Clone-Assignment).

# Dockerfile

The docker file sets up a docker image where three things 
are prepared:
- JsInspect is installed, such that you can run it from the 
command line.
- Cloc is installed.
- All versions of jQuery specified in `jquery_releases.csv` are 
cloned and downloaded to `/usr/jquery-data`.

When running the container a bash shell is opened such that you
can manually execute commands to run JsInspect and cloc. 

## Using this image

Build using `docker build -t 2imp25-code-clones .`

Then run using 
`docker run -it --rm -v "$PWD/out:/out" -v "$PWD/test-data:/usr/test-data" -v "$PWD/scripts:/usr/scripts" 2imp25-code-clones`. 
We again mount an out directory linked to the host file system
such that you can copy out files from the container. 

When the container is running you can execute bash commands
as if it is a virtual machine.

