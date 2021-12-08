#!/bin/bash

while true
do
   echo "I will continue to restart unless you press Ctrl+C"
   docker-compose restart rabbitmq
   sleep 30
done
