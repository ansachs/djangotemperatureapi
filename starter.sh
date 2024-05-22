#! /bin/bash
set -x

docker-compose up

trap_exit() {
   docker-compose down --remove-orphans --volumes
   docker-compose rm
}

trap trap_exit int