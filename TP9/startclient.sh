IMAGE_NAME="client"
DOCKERFILE_PATH="Dockerfile"

echo "Construction de l'image Docker avec le nom: $IMAGE_NAME"
docker build -t $IMAGE_NAME -f $DOCKERFILE_PATH .
exit 0


