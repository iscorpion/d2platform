#!/usr/bin/env bash
set +e
EXEC_OPTION=$1
SCRIPT_DIR=$(dirname $0)
SOURCE_DIR=$(pwd)

set -euo pipefail
IFS=$'\n\t'

IMAGE_DB_NAME=postgres-d2platform
CONTAINER_DB_NAME=postgres-d2platform-container
GRADLE_DB_SERVER=local

stop_container () {
  if [[ -n $(docker ps -q -f name=$CONTAINER_DB_NAME) ]]; then
    echo "Stopping container ${CONTAINER_DB_NAME}"
    docker stop $(docker ps -q -f name=$CONTAINER_DB_NAME)
  fi
}

start_container () {
  echo "Starting container ${CONTAINER_DB_NAME}"
  docker run --name=$CONTAINER_DB_NAME --network=postgres-network --restart=unless-stopped -p 5432:5432 -d $IMAGE_DB_NAME
}

remove_container() {
  if [[ -n $(docker ps -q -a -f name=$CONTAINER_DB_NAME) ]]; then
    echo "Removing container"
    docker rm $(docker ps -q -a -f name=$CONTAINER_DB_NAME)
  fi
}

remove_image() {
  if [[ -n $(docker images -q $IMAGE_DB_NAME) ]]; then
    echo "Removing image"
    docker rmi $(docker images -q $IMAGE_DB_NAME)
  fi
}

build_image() {
  echo "Building image"
  docker build --no-cache -t $IMAGE_DB_NAME .
}

create_network() {
  if [[ -n $(docker network ls name=postgres-network) ]]; then
    echo "Creating network"
    docker network create postgres-network
  fi
}

migrate() {
  cd $SOURCE_DIR
  ./gradle/gradlew -b grade/build.gradle databaseMigration -Dserver=$GRADLE_DB_SERVER --stacktrace --info
}

build_image_process() {
  cd $SCRIPT_DIR
  stop_container
  remove_container
  remove_image
  create_network
  build_image
  start_container
}


run () {
  build_image_process
  sleep 10s
#  migrate
}

run