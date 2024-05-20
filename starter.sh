#! /bin/bash

docker-compose up --detach --wait

trap_exit() {
   docker-compose down --remove-orphans
}

trap trap_exit EXIT