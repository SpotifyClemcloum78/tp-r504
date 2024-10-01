#!/bin/bash

docker build -t im-nginx-lb .

mkdir -p shared1 shared2

echo '<h1>Hello 1</h1>' > shared1/index.html
echo '<h1>Hello 2</h1>' > shared2/index.html

docker run -d --name nginx1 -p 81:80 -v "$(pwd)/shared1:/usr/share/nginx/html" nginx:latest
docker run -d --name nginx2 -p 82:80 -v "$(pwd)/shared2:/usr/share/nginx/html" nginx:latest

docker run -d --name nginx-lb -p 83:80 im-nginx-lb

count1=0
count2=0
for i in {1..500}
do
response=$(curl -s http://localhost:83)
echo "Réponse $i : $response"
if [[ "$response" == *"Hello 1"* ]]; then
((count1++))
elif [[ "$response" == *"Hello 2"* ]]; then
((count2++))
fi
done
echo "Nombre de réponses de 'Hello 1': $count1"
echo "Nombre de réponses de 'Hello 2': $count2"
echo "Tout marche"

