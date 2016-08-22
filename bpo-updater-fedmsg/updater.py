import fedmsg
import fedmsg.config
from elasticsearch import Elasticsearch
import urllib.request
import json


fedmsg_config = fedmsg.config.load_config()
es = Elasticsearch(hosts=[{'host': 'elasticsearch', 'port': 9200}])

config_topic = "org.fedoraproject.dev.logger.module.state.change"
config_pdc_url = "http://dev.fed-mod.org:8080"

def get_dependencies(name, version, release):
    url = "{pdc_url}/rest_api/v1/unreleasedvariants/?variant_name={name}&variant_version={version}&variant_release={release}".format(
                pdc_url=config_pdc_url, name=name, version=version, release=release)

    response = urllib.request.urlopen(url).read()
    response_string = response.decode('utf8')
    response_json = json.loads(response_string)
    runtime_deps = response_json["results"][0]["runtime_deps"]

    build_deps = response_json["results"][0]["build_deps"]

    return dict(runtime_deps=runtime_deps, build_deps=build_deps)
    

def module_state_change(msg):
    name = msg.get("name")
    version = msg.get("version")
    release = msg.get("release")
    state = msg.get("state")

    if not name or not version or not release or not state:
        return

    id = "{}-{}-{}".format(name, version, release)

    document = {
        "name": name,
        "version": version,
        "release": release,
        "build-state": state,
        "dependencies": [],
        "dependencies-build": [],
        "summary": ""
    }

    try:
        es.create(index="modularity", doc_type="module", id=id, body=document)
    except:
        document = {
            "doc": {
                "name": name,
                "version": version,
                "release": release,
                "build-state": state,
            }
        }
        es.update(index="modularity", doc_type="module", id=id, body=document)

for name, endpoint, topic, msg in fedmsg.tail_messages(**fedmsg_config):
    if config_topic == topic:
        module_state_change(msg["msg"])
