#Data structure in Elasticsearch

## Module

ID: `name-version-release`

```PYTHON
{
    "name": "module_name",
    "version": "module_version",
    "release": "module_release",
    "build_state": "build_state"
    "dependencies": [
        "name-version-release",                  # link to another module document
        "..."
    ],
    "dependencies_build": [
        "name-version-release",                  # link to another module document
        "..."
    ],
    "components": {
        "rpms": [                                # the actual built RPM packages
            {
                "name": "pkg_name",              # pkg name is a unique ID in a module
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
