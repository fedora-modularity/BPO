import fedmsg
import fedmsg.config
from elasticsearch import Elasticsearch
import urllib.request
import json
import sys
from datetime import datetime


# Configuration
# This should be in a config file, really
config_topic_module_state_change = "org.fedoraproject.dev.rida.module.state.change"
config_pdc_url = "http://dev.fed-mod.org:8080"
config_es_url = "elasticsearch"
config_es_port = 9200




def log(*args, **kwargs):
    """
    Write a log for the bpo-updater-fedmsg service.
    Currently uses docker which only needs a print to stderr.
    """

    print(*args, file=sys.stderr, **kwargs)


class PDCResponseException(Exception):
    pass


def query_pdc_metadata(name, version, release):
    """
    Get metadata for a specific module from PDC.
    Returns dicts with: runtime_deps, build_deps
    Returns string with: koji_tag
    TODO: it should support Koji (tag) and Copr (project)
    """

    url = "{pdc_url}/rest_api/v1/unreleasedvariants/?variant_name={name}&variant_version={version}&variant_release={release}".format(
                pdc_url=config_pdc_url, name=name, version=version, release=release)

    response = urllib.request.urlopen(url).read()
    response_string = response.decode('utf8')
    response_json = json.loads(response_string)

    try:
        pdc_module_data = response_json["results"][0]
    except KeyError:
        raise PDCResponseException

    # PDC stores dependencies as [{"dependency":"module-version-release"}]
    # but I want it as ["module-version-release"]
    runtime_deps_pdc = pdc_module_data.get("runtime_deps")
    runtime_deps = [dep["dependency"] for dep in runtime_deps_pdc if "dependency" in dep]

    # the same story here
    build_deps_pdc = pdc_module_data.get("build_deps")
    build_deps = [dep["dependency"] for dep in build_deps_pdc if "dependency" in dep]

    koji_tag = pdc_module_data.get("koji_tag")

    return dict(runtime_deps=runtime_deps, build_deps=build_deps, koji_tag=koji_tag)


def action_module_state_change(msg):
    """
    Reaction to a "module state change" fedmsg message.
    Creates empty/updates existing module document in Elasticsearch.
    """

    log ("Module state change: {}\n".format(topic))

    name = msg.get("name")
    version = msg.get("version")
    release = msg.get("release")
    state = msg.get("state_name")

    log ("Name: {}\nVersion: {}\nRelease: {}\nState: {}\n".format(name, version, release, state))

    # Is the message valid?
    if not name or not version or not release or not state:
        log("ERROR: Data not valid!")
        return

    id = "{}-{}-{}".format(name, version, release)

    # The initial Elasticsearch document - in case it needs to be created
    document = {
        "name": name,
        "version": version,
        "release": release,
        "build-state": state,
        "dependencies": [],
        "dependencies-build": [],
        "summary": "",
        "koji_tag": "",
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

    # Are the module metadata in PDC already? I want them now!
    # I will also do this just once, since module can enter this state only once.
    if state == "wait":
        log("Querying PDC...")
        pdc_data = query_pdc_metadata(name, version, release)
        log("Got the following data:\n{}".format(pdc_data))

        document["dependencies"] = pdc_data["runtime_deps"]
        document["dependencies-build"] = pdc_data["build_deps"]
        document["koji_tag"] = pdc_data["koji_tag"]

    # Push the data into Elasticsearch.
    try:
        # Try to create it
        es.create(index="modularity", doc_type="module", id=id, body=document)
        log("Elasticsearch: created")
    except:
        # Ha! It already exists. So I'll just update it.
        # I want to push just the changes, nothing else.
        document = {
            "doc": {
                "name": name,
                "version": version,
                "release": release,
                "build-state": state,
            }
        }

        # And if I have the data from PDC, include them as well.
        if state == "wait":
            document["dependencies"] = pdc_data["runtime_deps"]
            document["dependencies-build"] = pdc_data["build_deps"]
            document["koji_tag"] = pdc_data["koji_tag"]

        # And finally, update!
        es.update(index="modularity", doc_type="module", id=id, body=document)
        log("Elasticsearch: updated")

    log("Module state change action SUCCEEDED.\n")


def main():
    # Fedmsg and Elasticsearch clients
    fedmsg_config = fedmsg.config.load_config()
    es = Elasticsearch(hosts=[{'host': config_es_url, 'port': config_es_port}])

    # Reading Fedmsg messages
    for name, endpoint, topic, msg in fedmsg.tail_messages(**fedmsg_config):
        log("\n\n==============================================\n")
        log("Fedmsg received!\n")
        log("Time:   {}".format(datetime.now()))
        log("Topic:  {}".format(topic))
        log("Message:\n{}\n".format(msg))

        if topic == config_topic_module_state_change:
            action_module_state_change(msg["msg"])



if __name__ == "__main__":
    main()
