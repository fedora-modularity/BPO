#Build Pipeline Overview
This is a service providing a single UI for accessing information about build states of modules. The first version (currently in progress) is an experimental proof-of-concept hackish implementation. [Learn more about BPO](https://fedoraproject.org/wiki/Modularity/BPO)

![architecture](/doc/bpo-architecture.png)

##Local Development
```
$ docker-compose up
```

You might need to wait 10 seconds for the bpo-updater-fake container to push some mock data into elasticsearch.

The UI will be available on http://localhost

Requires docker 1.10 and docker-compose 1.7

## Resources in this repo

* [Data structure in Elasticsearch](data_structure.md)

* [Fedmsg messages associated with a module build](messages.md)
