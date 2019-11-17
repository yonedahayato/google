# docker build -t exec_gcolab_lib -f ./Dockerfile_lib .
docker build -t exec_gcolab .
docker run \
  -v $PWD/log:/home/colaboratory/log \
  -v /Users/yonedahayato/Library/Application\ Support/Google/Chrome:/home/colaboratory/userdata \
  -p 9222:9222 \
  -it --rm exec_gcolab /bin/bash
# docker run -v $PWD/log:/home/colaboratory/log -it --rm exec_gcolab python3 exec_gcolab.py
docker rmi exec_gcolab
