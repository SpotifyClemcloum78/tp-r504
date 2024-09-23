IMAGE_NAME="im-tp4"
DOCKERFILE_PATH="Dockerfile1"

echo "Construction de l'image Docker avec le nom: $IMAGE_NAME"
docker build -t $IMAGE_NAME -f $DOCKERFILE_PATH .
exit 0


