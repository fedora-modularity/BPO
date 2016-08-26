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
                "dependencies_build": {
                    "type": "string",
                    "index": "not_analyzed"
                },
                "components": {
                    "type": "object",
                    "properties": {
                        "rpms": {
                            "type": "object",
                            "properties": {
                                "name": {
                                    "type": "string",
                                    "index": "not_analyzed"
                                },
                                "version": {
                                    "type": "string",
                                    "index": "not_analyzed"
                                },
                                "release": {
                                    "type": "string",
                                    "index": "not_analyzed"
                                },
                                "build_state": {
                                    "type": "string",
                                    "index": "not_analyzed"
                                }
                            }
                        }
                    }
                },
                "api": {
                    "type": "object",
                    "properties": {
                        "rpms": {
                            "type": "string",
                            "index": "not_analyzed"
                        }
                    }
                },
                "install_profiles": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "index": "not_analyzed"
                        },
                        "description": {
                            "type": "string"
                        },
                        "rpms": {
                            "type": "string",
                            "index": "not_analyzed"
                        }
                    }
                }
            }
        }
    }
}'
