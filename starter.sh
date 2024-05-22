#! /bin/bash

docker-compose up

trap_exit() {
   docker-compose down --remove-orphans
}

trap trap_exit EXIT