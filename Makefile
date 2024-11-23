# Define the image name
IMAGE_NAME = de_dockerdemo_2
DOCKER_ID_USER = cinnamondanish

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME):latest .

# Run the Docker container
run:
	docker run -p 5005:5000 $(IMAGE_NAME)

# Remove the Docker image
# Stop and remove all containers associated with the image, then delete the image
clean:
	-docker ps -a -q --filter ancestor=$(IMAGE_NAME) | xargs -r docker stop
	-docker ps -a -q --filter ancestor=$(IMAGE_NAME) | xargs -r docker rm
	-docker images -q $(IMAGE_NAME) | xargs -r docker rmi -f

image_show:
	docker images

container_show:
	docker ps

push:
	docker login
	docker tag $(IMAGE_NAME) $(DOCKER_ID_USER)/$(IMAGE_NAME)
	docker push $(DOCKER_ID_USER)/$(IMAGE_NAME):latest

login:
	docker login -u ${DOCKER_ID_USER}