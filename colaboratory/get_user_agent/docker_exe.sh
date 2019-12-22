image_name=get_user_agent

# docker rmi $image_name
# docker build -t $image_name -f Dockerfile .
docker run --rm -it \
           -p 5901:5901 \
           -v $PWD:/headless/Desktop/my_dir $image_name
# docker rmi $image_name
