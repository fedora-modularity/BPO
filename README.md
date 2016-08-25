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

## Data structure in Elasticsearch

### Module

ID: `name-version-release`

```
{
    "name": "module_name",
    "version": "module_version",
    "release": "module_release",
    "build_state": "build_state"
    "dependencies": [
        "name-version-release",    # link to another module document
        "..."
    ],
    "dependencies_build": [
        "name-version-release",    # link to another module document
        "..."
    ],
    "components": {
        "rpms": [                   # the actual built RPM packages
            {
                "name": "pkg_name",         # pkg name is a unique ID in a module
                "version": "pkg_version",
                "release": "pkg_release",
                "build_state": "pkg_build_state",
            },
            { ... }
        ]
    },
    "api": {
        "rpms": [
            "pkg_name",
            "..."
        ]
    },
    "install_profiles": [
        {
            "name": "profile_name",
            "description": "Lorem ipsum dolor sit amet...",
            "rpms": [
                "pkg_name",
                "..."
            ]
        }
    ]
}
```
