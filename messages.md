# Fedmsg messages associated with a module build

Following are all the fedmsg messages associated with building a module
in the Fedora infrastructure. Messages are in the same order as they would
be emitted.

## Messages

### org.fedoraproject.stg.git.receive

```
"msg": {
    "commit": {
        "username": "sgallagh",
        "stats": {
            "files": {
                "testmodule.yaml": {
                    "deletions": 1,
                    "additions": 1,
                    "lines": 2
                }
            },
            "total": {
                "deletions": 1,
                "files": 1,
                "additions": 1,
                "lines": 2
            }
        },
        "name": "Stephen Gallagher",
        "namespace": "modules",
        "rev": "ce1ff2f6892adf89371f35bfdbd149869cd44b2e",
        "agent": "sgallagh",
        "summary": "Bumping release to 4 to test builds",
        "repo": "testmodule",
        "branch": "master",
        "path": "/srv/git/repositories/modules/testmodule.git",
        "seen": false,
        "message": "Bumping release to 4 to test builds\n",
        "email": "sgallagh@redhat.com"
    }
}
```

### org.fedoraproject.dev.rida.module.state.change

```
"msg": {
    "component_builds": [],
    "name": "testmodule",
    "time_submitted": 1472670725.0,
    "owner": "sgallagh",
    "time_modified": null,
    "release": "4",
    "state": 0,
    "time_completed": null,
    "version": "4.3.44",
    "scmurl": "git://pkgs.stg.fedoraproject.org/modules/testmodule?#ce1ff2f6892adf89371f35bfdbd149869cd44b2e",
    "id": 39,
    "state_name": "init"
}
```



### org.fedoraproject.dev.rida.module.state.change

```
"msg": {
    "component_builds": [],
    "name": "testmodule",
    "time_submitted": 1472670725.0,
    "owner": "sgallagh",
    "time_modified": 1472670728.0,
    "release": "4",
    "state": 1,
    "time_completed": null,
    "version": "4.3.44",
    "scmurl": "git://pkgs.stg.fedoraproject.org/modules/testmodule?#ce1ff2f6892adf89371f35bfdbd149869cd44b2e",
    "id": 39,
    "state_name": "wait"
}
```



### org.fedoraproject.stg.buildsys.package.list.change

```
"msg": {
    "instance": "primary",
    "tag": "module-testmodule-4.3.44-4",
    "package": "module-build-macros"
}
```



### org.fedoraproject.dev.rida.module.state.change

```
"msg": {
    "component_builds": [
        65
    ],
    "name": "testmodule",
    "time_submitted": 1472670725.0,
    "owner": "sgallagh",
    "time_modified": 1472670747.0,
    "release": "4",
    "state": 2,
    "time_completed": null,
    "version": "4.3.44",
    "scmurl": "git://pkgs.stg.fedoraproject.org/modules/testmodule?#ce1ff2f6892adf89371f35bfdbd149869cd44b2e",
    "id": 39,
    "state_name": "build"
}
```



### org.fedoraproject.stg.buildsys.repo.init

```
"msg": {
    "instance": "primary",
    "repo_id": 9006648,
    "tag": "module-testmodule-4.3.44-4-build",
    "tag_id": 439
}
```



### org.fedoraproject.stg.buildsys.repo.done

```
"msg": {
    "instance": "primary",
    "repo_id": 9006648,
    "tag": "module-testmodule-4.3.44-4-build",
    "tag_id": 439
}
```



### org.fedoraproject.stg.buildsys.build.state.change

```
"msg": {
    "build_id": 760075,
    "old": null,
    "name": "module-build-macros",
    "task_id": 90124338,
    "attribute": "state",
    "instance": "primary",
    "version": "0.1",
    "owner": "m8y",
    "new": 0,
    "release": "1.module_testmodule_4.3.44_4"
}
```



### org.fedoraproject.stg.buildsys.build.state.change

```
"msg": {
    "build_id": 760075,
    "old": 0,
    "name": "module-build-macros",
    "task_id": 90124338,
    "attribute": "state",
    "instance": "primary",
    "version": "0.1",
    "owner": "m8y",
    "new": 1,
    "release": "1.module_testmodule_4.3.44_4"
}
```



### org.fedoraproject.stg.buildsys.package.list.change

```
"msg": {
    "instance": "primary",
    "tag": "module-testmodule-4.3.44-4-build",
    "package": "module-build-macros"
}
```



### org.fedoraproject.stg.buildsys.tag",

```
"msg": {
    "build_id": 760075,
    "name": "module-build-macros",
    "tag_id": 439,
    "instance": "primary",
    "tag": "module-testmodule-4.3.44-4-build",
    "user": "m8y",
    "version": "0.1",
    "owner": "m8y",
    "release": "1.module_testmodule_4.3.44_4"
}
```



### org.fedoraproject.stg.buildsys.tag

```
"msg": {
    "build_id": 760075,
    "name": "module-build-macros",
    "tag_id": 438,
    "instance": "primary",
    "tag": "module-testmodule-4.3.44-4",
    "user": "m8y",
    "version": "0.1",
    "owner": "m8y",
    "release": "1.module_testmodule_4.3.44_4"
}
```



### org.fedoraproject.stg.buildsys.repo.init

```
"msg": {
    "instance": "primary",
    "repo_id": 9006649,
    "tag": "module-testmodule-4.3.44-4-build",
    "tag_id": 439
}
```



### org.fedoraproject.stg.buildsys.repo.done

```
"msg": {
    "instance": "primary",
    "repo_id": 9006649,
    "tag": "module-testmodule-4.3.44-4-build",
    "tag_id": 439
}
```



### org.fedoraproject.stg.buildsys.package.list.change

```
"msg": {
    "instance": "primary",
    "tag": "module-testmodule-4.3.44-4",
    "package": "bash"
}
```



### org.fedoraproject.stg.buildsys.build.state.change

```
"msg": {
    "build_id": 760076,
    "old": null,
    "name": "bash",
    "task_id": 90124361,
    "attribute": "state",
    "instance": "primary",
    "version": "4.3.33",
    "owner": "m8y",
    "new": 0,
    "release": "2.module_testmodule_4.3.44_4"
}
```



### org.fedoraproject.stg.buildsys.build.state.change

```
"msg": {
    "build_id": 760076,
    "old": 0,
    "name": "bash",
    "task_id": 90124361,
    "attribute": "state",
    "instance": "primary",
    "version": "4.3.33",
    "owner": "m8y",
    "new": 1,
    "release": "2.module_testmodule_4.3.44_4"
}
```



### org.fedoraproject.stg.buildsys.tag

```
"msg": {
    "build_id": 760076,
    "name": "bash",
    "tag_id": 439,
    "instance": "primary",
    "tag": "module-testmodule-4.3.44-4-build",
    "user": "m8y",
    "version": "4.3.33",
    "owner": "m8y",
    "release": "2.module_testmodule_4.3.44_4"
}
```



### org.fedoraproject.stg.buildsys.tag

```
"msg": {
    "build_id": 760076,
    "name": "bash",
    "tag_id": 438,
    "instance": "primary",
    "tag": "module-testmodule-4.3.44-4",
    "user": "m8y",
    "version": "4.3.33",
    "owner": "m8y",
    "release": "2.module_testmodule_4.3.44_4"
}
```



### org.fedoraproject.stg.buildsys.repo.init

```
"msg": {
    "instance": "primary",
    "repo_id": 9006650,
    "tag": "module-testmodule-4.3.44-4-build",
    "tag_id": 439
}
```



### org.fedoraproject.stg.buildsys.repo.done

```
"msg": {
    "instance": "primary",
    "repo_id": 9006650,
    "tag": "module-testmodule-4.3.44-4-build",
    "tag_id": 439
}
```



### org.fedoraproject.dev.rida.module.state.change

```
"msg": {
    "component_builds": [
        65,
        66
    ],
    "name": "testmodule",
    "time_submitted": 1472670725.0,
    "owner": "sgallagh",
    "time_modified": 1472673373.0,
    "release": "4",
    "state": 3,
    "time_completed": null,
    "version": "4.3.44",
    "scmurl": "git://pkgs.stg.fedoraproject.org/modules/testmodule?#ce1ff2f6892adf89371f35bfdbd149869cd44b2e",
    "id": 39,
    "state_name": "done"
}
```



### org.fedoraproject.dev.rida.module.state.change

```
"msg": {
    "component_builds": [
        65,
        66
    ],
    "name": "testmodule",
    "time_submitted": 1472670725.0,
    "owner": "sgallagh",
    "time_modified": 1472673374.0,
    "release": "4",
    "state": 5,
    "time_completed": null,
    "version": "4.3.44",
    "scmurl": "git://pkgs.stg.fedoraproject.org/modules/testmodule?#ce1ff2f6892adf89371f35bfdbd149869cd44b2e",
    "id": 39,
    "state_name": "ready"
}
```



### org.fedoraproject.dev.pungi.tree

```
"msg": {
    "sigkeys": [
        "unsigned"
    ],
    "path": "/var/www/html/modularity/repos/module-testmodule-4.3.44-4/0",
    "arches": [
        "i686",
        "armv7hl",
        "x86_64"
    ],
    "tag": "module-testmodule-4.3.44-4",
    "state": "running"
}
```



### org.fedoraproject.dev.pungi.tree

```
"msg": {
    "sigkeys": [
        "unsigned"
    ],
    "path": "/var/www/html/modularity/repos/module-testmodule-4.3.44-4/0",
    "arches": [
        "i686",
        "armv7hl",
        "x86_64"
    ],
    "tag": "module-testmodule-4.3.44-4",
    "state": "finished"
}
```



### org.fedoraproject.dev.pungi.tree

```
"msg": {
    "sigkeys": [
        "unsigned"
    ],
    "path": "/var/www/html/modularity/repos/module-testmodule-4.3.44-4/1",
    "arches": [
        "i686",
        "armv7hl",
        "x86_64"
    ],
    "tag": "module-testmodule-4.3.44-4",
    "state": "running"
}
```



### org.fedoraproject.dev.pungi.tree

```
"msg": {
    "sigkeys": [
        "unsigned"
    ],
    "path": "/var/www/html/modularity/repos/module-testmodule-4.3.44-4/1",
    "arches": [
        "i686",
        "armv7hl",
        "x86_64"
    ],
    "tag": "module-testmodule-4.3.44-4",
    "state": "finished"
}
```
