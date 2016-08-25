#!/usr/bin/sh

curl -XPUT 'http://elasticsearch:9200/modularity/module/build-stuff-4.2-1' -d '
{
    "name": "build-stuff",
    "version": "4.2",
    "release": "1",
    "summary": "Basic build tools",
    "build-state": "done",
    "dependencies": [],
    "dependencies-build": [],
    "components": {
        "rpms": []
    },
    "api": {
        "rpms": []
    },
    "install_profiles": {
        "rpms": []
    }
}
'

curl -XPUT 'http://elasticsearch:9200/modularity/module/base-module-1.0-1' -d '
{
    "name": "base-module",
    "version": "1.0",
    "release": "1",
    "summary": "The base module",
    "build-state": "done",
    "dependencies": [],
    "dependencies-build": [],
    "components": {
        "rpms": []
    },
    "api": {
        "rpms": []
    },
    "install_profiles": {
        "rpms": []
    }
}
'

curl -XPUT 'http://elasticsearch:9200/modularity/module/hello-world-1.0-1' -d '
{
    "name": "hello-world",
    "version": "1.0",
    "release": "1",
    "summary": "Hello world examples in various languages",
    "build-state": "wait",
    "dependencies": [
        "base-module-1.0-1"
    ],
    "dependencies-build": [
        "build-stuff-4.2-1",
        "base-module-1.0-1"
    ],
    "components": {
        "rpms": []
    },
    "api": {
        "rpms": []
    },
    "install_profiles": {
        "rpms": []
    }
}
'

curl -XPUT 'http://elasticsearch:9200/modularity/module/hello-world-2.5-1' -d '
{
    "name": "hello-world",
    "version": "2.5",
    "release": "1",
    "summary": "Hello world examples in various languages",
    "build-state": "init",
    "dependencies": [
        "base-module-1.0-1"
    ],
    "dependencies-build": [
        "build-stuff-4.2-1",
        "base-module-1.0-1"
    ],
    "components": {
        "rpms": []
    },
    "api": {
        "rpms": []
    },
    "install_profiles": {
        "rpms": []
    }
}
'

curl -XPUT 'http://elasticsearch:9200/modularity/module/hello-world-2.4-1' -d '
{
    "name": "hello-world",
    "version": "2.4",
    "release": "1",
    "summary": "Hello world examples in various languages",
    "dependencies": [
        "base-module-1.0-1"
    ],
    "dependencies-build": [
        "build-stuff-4.2-1",
        "base-module-1.0-1"
    ],
    "build-state": "wait",
    "components": {
        "rpms": []
    },
    "api": {
        "rpms": []
    },
    "install_profiles": {
        "rpms": []
    }
}
'

curl -XPUT 'http://elasticsearch:9200/modularity/module/random-language-stack-1.0-1' -d '
{
    "name": "random-language-stack",
    "version": "1.0",
    "release": "1",
    "summary": "A module containing a full stack of a random language.",
    "dependencies": [
        "base-module-1.0-1"
    ],
    "dependencies-build": [
        "build-stuff-4.2-1",
        "base-module-1.0-1"
    ],
    "build-state": "build",
    "components": {
        "rpms": [
            {
                "name": "random-language",
                "version": "1.0",
                "release": "1",
                "build_state": "succeeded"
            },
            {
                "name": "random-language-feature",
                "version": "2.1",
                "release": "1",
                "build_state": "running"
            },
            {
                "name": "random-language-extension",
                "version": "1.6",
                "release": "5",
                "build_state": "pending"
            }
        ]
    },
    "api": {
        "rpms": [
            "random-language",
            "random-language-feature",
            "random-language-extension"
        ]
    },
    "install_profiles": {
        "rpms": [
            {
                "name": "default",
                "description": "The default installation of random language.",
                "rpms": [
                    "random-language",
                    "random-language-feature"
                ]
            },
            {
                "name": "extended",
                "description": "An extended installation of random language.",
                "rpms": [
                    "random-language",
                    "random-language-feature",
                    "random-language-extension"
                ]
            }
        ]
    }
}
'

curl -XPUT 'http://elasticsearch:9200/modularity/module/random-language-stack-2.0-1' -d '
{
    "name": "random-language-stack",
    "version": "2.0",
    "release": "1",
    "summary": "A module containing a full stack of a random language.",
    "dependencies": [
        "base-module-1.0-1"
    ],
    "dependencies-build": [
        "build-stuff-4.2-1",
        "base-module-1.0-1"
    ],
    "build-state": "build",
    "components": {
        "rpms": [
            {
                "name": "random-language",
                "version": "2.0",
                "release": "1",
                "build_state": "succeeded"
            },
            {
                "name": "random-language-feature",
                "version": "2.2",
                "release": "1",
                "build_state": "running"
            },
            {
                "name": "random-language-extension",
                "version": "1.6",
                "release": "5",
                "build_state": "pending"
            }
        ]
    },
    "api": {
        "rpms": [
            "random-language",
            "random-language-feature",
            "random-language-extension"
        ]
    },
    "install_profiles": {
        "rpms": [
            {
                "name": "default",
                "description": "The default installation of random language.",
                "rpms": [
                    "random-language",
                    "random-language-feature"
                ]
            },
            {
                "name": "extended",
                "description": "An extended installation of random language.",
                "rpms": [
                    "random-language",
                    "random-language-feature",
                    "random-language-extension"
                ]
            }
        ]
    }
}
'

curl -XPUT 'http://elasticsearch:9200/modularity/module/random-language-stack-2.0-2' -d '
{
    "name": "random-language-stack",
    "version": "2.0",
    "release": "2",
    "summary": "A module containing a full stack of a random language.",
    "dependencies": [
        "base-module-1.0-1"
    ],
    "dependencies-build": [
        "build-stuff-4.2-1",
        "base-module-1.0-1"
    ],
    "build-state": "build",
    "components": {
        "rpms": [
            {
                "name": "random-language",
                "version": "2.0",
                "release": "2",
                "build_state": "succeeded"
            },
            {
                "name": "random-language-feature",
                "version": "2.2",
                "release": "1",
                "build_state": "running"
            },
            {
                "name": "random-language-extension",
                "version": "1.6",
                "release": "5",
                "build_state": "pending"
            }
        ]
    },
    "api": {
        "rpms": [
            "random-language",
            "random-language-feature",
            "random-language-extension"
        ]
    },
    "install_profiles": {
        "rpms": [
            {
                "name": "default",
                "description": "The default installation of random language.",
                "rpms": [
                    "random-language",
                    "random-language-feature"
                ]
            },
            {
                "name": "extended",
                "description": "An extended installation of random language.",
                "rpms": [
                    "random-language",
                    "random-language-feature",
                    "random-language-extension"
                ]
            }
        ]
    }
}
'

curl -XPUT 'http://elasticsearch:9200/modularity/module/random-app-1.0-1' -d '
{
    "name": "random-app",
    "version": "1.0",
    "release": "1",
    "summary": "Random app written in a random language",
    "dependencies": [
        "base-module-1.0-1",
        "random-language-stack-1.0-1"
    ],
    "dependencies-build": [
        "build-stuff-4.2-1",
        "base-module-1.0-1",
        "random-language-stack-1.0-1"
    ],
    "build-state": "build",
    "components": {
        "rpms": []
    },
    "api": {
        "rpms": []
    },
    "install_profiles": {
        "rpms": []
    }
}
'
curl -XPUT 'http://elasticsearch:9200/modularity/module/random-app-2.0-1' -d '
{
    "name": "random-app",
    "version": "2.0",
    "release": "1",
    "summary": "Random app written in a random language",
    "dependencies": [
        "base-module-1.0-1",
        "random-language-stack-2.0-1"
    ],
    "dependencies-build": [
        "build-stuff-4.2-1",
        "base-module-1.0-1",
        "random-language-stack-2.0-1"
    ],
    "build-state": "build",
    "components": {
        "rpms": []
    },
    "api": {
        "rpms": []
    },
    "install_profiles": {
        "rpms": []
    }
}
'

curl -XPUT 'http://elasticsearch:9200/modularity/module/random-app-2.0-2' -d '
{
    "name": "random-app",
    "version": "2.0",
    "release": "2",
    "summary": "Random app written in a random language",
    "dependencies": [
        "base-module-1.0-1",
        "random-language-stack-2.0-2"
    ],
    "dependencies-build": [
        "build-stuff-4.2-1",
        "base-module-1.0-1",
        "random-language-stack-2.0-2"
    ],
    "build-state": "failed",
    "components": {
        "rpms": []
    },
    "api": {
        "rpms": []
    },
    "install_profiles": {
        "rpms": []
    }
}
'
