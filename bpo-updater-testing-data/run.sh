#!/bin/sh


# wait for the elasticsearch container to start
sleep 15

# Push fake data into elasticsearch
./create_es_testing_data.sh
