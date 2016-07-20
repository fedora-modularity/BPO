#!/bin/sh


# wait for the elasticsearch container to start
sleep 10

# Create the "schema" in elasticsearch
./create_es_mappings.sh

# Push fake data into elasticsearch
./create_es_testing_data.sh
