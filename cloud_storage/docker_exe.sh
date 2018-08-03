#!/bin/bash

# build dockerfile library
# docker build -t google_cloud_storage_lib -f dockerfile/Dockerfile_lib .

# build dockerfile
docker build -t google_cloud_storage -f dockerfile/Dockerfile .

# log directory
if [ ! -d "log" ]; then
  mkdir log
fi

# environment
SCRIPT_DIR=$(cd $(dirname $0); pwd)
LOG_DIR=$SCRIPT_DIR/log
export LOG_DIR=$LOG_DIR

# upload
# docker run -it --rm google_cloud_storage python uploader.py
docker-compose up

# remove docker image
# docker rmi google_cloud_storage_lib
docker rmi google_cloud_storage
docker-compose down -v
