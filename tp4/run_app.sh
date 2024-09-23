IMAGE_NAME="im-tp4"
CONTAINER_NAME="tp4-app"
NETWORK_NAME="net-tp4"
HOST_PORT=5000
CONTAINER_PORT=5000

if ! docker network ls | grep -q "$NETWORK_NAME"; then
    echo "Le réseau $NETWORK_NAME n'existe pas, création du réseau..."
    docker network create $NETWORK_NAME
else
    echo "Le réseau $NETWORK_NAME existe déjà."
fi

echo "Lancement du conteneur $CONTAINER_NAME à partir de l'image $IMAGE_NAME..."
docker run -d --name $CONTAINER_NAME \
    --network $NETWORK_NAME \
    -p $HOST_PORT:$CONTAINER_PORT \
    $IMAGE_NAME

if [ $? -eq 0 ]; then
    echo "Le conteneur $CONTAINER_NAME a été lancé avec succès et est accessible sur le port $HOST_PORT."
else
    echo "Erreur lors du lancement du conteneur $CONTAINER_NAME."
    exit 1
fi
