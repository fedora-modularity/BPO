#!/bin/sh


# wait for the elasticsearch container to start
until curl http://elasticsearch:9200
do
  sleep 1
  echo waiting
done

# Create the "schema" in elasticsearch
./create_es_mappings.sh

exit 0
