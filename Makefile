build:
	sudo docker build --platform linux/arm64 -f ./docker/Dockerfile-screen1 -t afiguinha/jetson-screen1 . && sudo docker push afiguinha/jetson-screen1

run:
	sudo docker run -it --ipc=host --runtime=nvidia --device=/dev/video0:/dev/video0 --privileged -e DISPLAY=$(DISPLAY) -v /tmp/.X11-unix:/tmp/.X11-unix afiguinha/jetson-screen1
