#!/usr/bin/env bash
set -e


echo "Deleting old images"
docker system prune -f 2>/dev/null; true

echo "Updating Docker Image"
docker login --username cloudpeerbits --password cloud@peerbits123
docker pull cloudpeerbits/$REPO_NAME:latest
cd /home/ubuntu/docker

echo "Deploying Docker stack"
docker stack deploy -c docker-compose.yml cloud
docker service update --force `echo $SERVICE_NAME`