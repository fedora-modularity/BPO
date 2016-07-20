from flask import Flask
from flask import render_template
from redis import Redis
from elasticsearch import Elasticsearch
from datetime import datetime

app = Flask(__name__)
redis = Redis(host='redis', port=6379)
es = Elasticsearch(hosts=[{'host': 'elasticsearch', 'port': 9200}])


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/modules/')
def modules():
    res = es.search(index="modularity", doc_type='module')
    return render_template("modules.html", res=res)


@app.route('/modules/<name>/')
def module_versions(name):
    query = {
        "query" : {
            "constant_score" : {
                "filter" : {
                    "term" : {
                        "name" : name
                    }
                }
            }
        }
    }

    res = es.search(index="modularity", doc_type='module', body=query)
    return render_template("module_versions.html", name=name, res=res)

@app.route('/modules/<name>/<version>/<release>/')
def module_overview(name, version, release):
    return render_template("module/overview.html",
                            name=name,
                            version=version,
                            release=release)

@app.route('/modules/<name>/<version>/<release>/packages/')
def module_packages(name, version, release):
    return render_template("module/packages.html",
                            name=name,
                            version=version,
                            release=release)

@app.route('/modules/<name>/<version>/<release>/dependencies/')
def module_dependencies(name, version, release):
    return render_template("module/dependencies.html",
                            name=name,
                            version=version,
                            release=release)

@app.route('/modules/<name>/<version>/<release>/required_by/')
def module_required_by(name, version, release):
    return render_template("module/required-by.html",
                            name=name,
                            version=version,
                            release=release)

@app.route('/modules/<name>/<version>/<release>/artifacts/')
def module_artifacts(name, version, release):
    return render_template("module/artifacts.html",
                            name=name,
                            version=version,
                            release=release)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
