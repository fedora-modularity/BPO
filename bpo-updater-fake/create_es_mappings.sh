#!/usr/bin/sh

curl -XPOST elasticsearch:9200/modularity -d '{
    "mappings": {
        "module": {
            "properties": {
                "name": {
                    "type": "string",
                    "fields": {
                        "raw": {
                            "type" : "string",
                            "index" : "not_analyzed"
                        }
                    }
                },
                "version": {
                    "type": "string",
                    "fields": {
                        "raw": {
                            "type" : "string",
                            "index" : "not_analyzed"
                        }
                    }
                },
                "release": {
                    "type": "string",
                    "fields": {
                        "raw": {
                            "type" : "string",
                            "index" : "not_analyzed"
                        }
                    }
                },
                "build_state": {
                    "type": "string",
                    "fields": {
                        "raw": {
                            "type" : "string",
                            "index" : "not_analyzed"
                        }
                    }
                },
                "dependencies": {
                    "type": "string",
                    "index": "not_analyzed"
                },
                "dependencies-build": {
                    "type": "string",
                    "index": "not_analyzed"
                }
            }
        }
    }
}'
