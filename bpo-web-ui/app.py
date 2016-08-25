from flask import Flask
from flask import render_template, request
from elasticsearch import Elasticsearch
from datetime import datetime
import re

app = Flask(__name__)
es = Elasticsearch(hosts=[{'host': 'elasticsearch', 'port': 9200}])



def safe_input(string):
    return re.sub(r'[^a-zA-Z0-9\-_. ]', '', string)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/modules/')
def modules():
    query = {
        "size": 0,
        "aggs": {
            "modules": {
                "terms": {
                    "field": "name.raw"
                }
            }
        }
    }
    res = es.search(index="modularity", doc_type='module', body=query)

    modules = res["aggregations"]["modules"]["buckets"]
    return render_template("modules.html", modules=modules)


@app.route('/modules/<name>/')
def module_versions(name):
    query = {
         "size": 0,
         "query": {
             "bool": {
                 "must": [
                     { "match": { "name.raw": safe_input(name) }}
                 ]
             }
         },
         "aggs": {
             "modules": {
                 "terms": {
                     "field": "name.raw"
                 },
                 "aggs": {
                        "versions": {
                            "terms": {
                                    "field": "version.raw"
                            }
                        }
                 }
             }
         }
    }

    res = es.search(index="modularity", doc_type='module', body=query)

    versions = res["aggregations"]["modules"]["buckets"][0]["versions"]["buckets"]

    return render_template("module_versions.html",
                                    name=name,
                                    versions=versions)


@app.route('/modules/<name>/<version>/')
def module_version_releases(name, version):
    query = {
        "query": {
            "bool": {
                "must": [
                    { "match": { "name.raw": safe_input(name) }},
                    { "match": { "version.raw": safe_input(version) }}
                ]
            }
        }
    }

    res = es.search(index="modularity", doc_type='module', body=query)

    documents = res["hits"]["hits"]

    return render_template("module_version_releases.html",
                                    name=name,
                                    version=version,
                                    documents=documents)



def get_module(name, version, release):
    query = {
        "query": {
            "bool": {
                "must": [
                    { "match": { "name.raw": safe_input(name) }},
                    { "match": { "version.raw": safe_input(version) }},
                    { "match": { "release.raw": safe_input(release) }}
                ]
            }
        }
    }

    res = es.search(index="modularity", doc_type='module', body=query)

    module = res["hits"]["hits"][0]
    return module

@app.route('/modules/<name>/<version>/<release>/')
def module_overview(name, version, release):
    module = get_module(name, version, release)

    components = module["_source"]["components"]

    return render_template("module/overview.html",
                            name=name,
                            version=version,
                            release=release,
                            module=module,
                            components=components)

@app.route('/modules/<name>/<version>/<release>/components/')
def module_components(name, version, release):
    module = get_module(name, version, release)

    components = module["_source"]["components"]

    return render_template("module/components.html",
                            name=name,
                            version=version,
                            release=release,
                            components=components)

@app.route('/modules/<name>/<version>/<release>/api/')
def module_api(name, version, release):
    module = get_module(name, version, release)

    components = module["_source"]["components"]

    api_names = module["_source"]["api"]["rpms"]

    api_rpms = []

    for component in components["rpms"]:
        if component["name"] in api_names:
            pkg = "{}-{}-{}".format(component["name"],
                                   component["version"],
                                   component["release"])
            api_rpms.append(pkg)


    return render_template("module/api.html",
                            name=name,
                            version=version,
                            release=release,
                            api_rpms=api_rpms)

@app.route('/modules/<name>/<version>/<release>/install_profiles/')
def module_install_profiles(name, version, release):
    module = get_module(name, version, release)
    return render_template("module/install_profiles.html",
                            name=name,
                            version=version,
                            release=release)

@app.route('/modules/<name>/<version>/<release>/dependencies/')
def module_dependencies(name, version, release):
    module = get_module(name, version, release)

    deps_ids = module["_source"]["dependencies"]
    if deps_ids:
        query = {
            "ids": deps_ids
        }
        res = es.mget(index="modularity", doc_type='module', body=query)
        dependencies = res["docs"]
    else:
        dependencies = []

    return render_template("module/dependencies/runtime.html",
                            name=name,
                            version=version,
                            release=release,
                            dependencies=dependencies)

@app.route('/modules/<name>/<version>/<release>/dependencies/build/')
def module_dependencies_build(name, version, release):
    module = get_module(name, version, release)

    deps_ids = module["_source"]["dependencies-build"]
    if deps_ids:
        query = {
            "ids": deps_ids
        }
        res = es.mget(index="modularity", doc_type='module', body=query)
        dependencies = res["docs"]
    else:
        dependencies = []

    return render_template("module/dependencies/build.html",
                            name=name,
                            version=version,
                            release=release,
                            dependencies=dependencies)


@app.route('/modules/<name>/<version>/<release>/dependency_of/')
def module_dependency_of(name, version, release):
    module = get_module(name, version, release)

    query = {
        "query": {
            "filtered": {
                "query": {
                    "match_all": {}
                },
                "filter": {
                    "terms": {
                        "dependencies": [module["_id"]]
                    }
                }
            }
        }
    }

    res = es.search(index="modularity", doc_type='module', body=query)
    dependency_of = res["hits"]["hits"]

    return render_template("module/dependency-of/runtime.html",
                            name=name,
                            version=version,
                            release=release,
                            dependency_of=dependency_of)


@app.route('/modules/<name>/<version>/<release>/dependency_of/build/')
def module_dependency_of_build(name, version, release):
    module = get_module(name, version, release)

    query = {
        "query": {
            "filtered": {
                "query": {
                    "match_all": {}
                },
                "filter": {
                    "terms": {
                        "dependencies-build": [module["_id"]]
                    }
                }
            }
        }
    }

    res = es.search(index="modularity", doc_type='module', body=query)
    dependency_of = res["hits"]["hits"]

    return render_template("module/dependency-of/build.html",
                            name=name,
                            version=version,
                            release=release,
                            dependency_of=dependency_of)

@app.route('/modules/<name>/<version>/<release>/component_of/')
def module_component_of(name, version, release):
    module = get_module(name, version, release)
    return render_template("module/component_of.html",
                            name=name,
                            version=version,
                            release=release)

@app.route('/modules/<name>/<version>/<release>/artifacts/')
def module_artifacts(name, version, release):
    module = get_module(name, version, release)
    return render_template("module/artifacts.html",
                            name=name,
                            version=version,
                            release=release)


@app.route('/search-modules/')
def search_modules():
    search = request.args.get('search')
    query = {
        "query": {
            "match": {
                "_all": safe_input(search)
            }
        }
    }

    res = es.search(index="modularity", doc_type='module', body=query)
    modules = res["hits"]["hits"]

    return render_template("search-modules.html",
                            search=search,
                            modules=modules)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
