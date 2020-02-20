image_host=xxx
image_name=${image_host}/get_user_agent
lib_image_name=get_user_agent_lib

# docker rmi $image_name
# docker build -t $lib_image_name -f Dockerfile_lib .
# docker build -t $image_name -f Dockerfile .
docker run --rm -it \
           -p 6080:80 \
           -p 5900:5900 \
           -p 8080:8080 \
           -v $PWD:/root/get_user_agent \
           $image_name
# docker rmi $image_name
