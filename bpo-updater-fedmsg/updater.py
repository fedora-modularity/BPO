import fedmsg
import fedmsg.config
from elasticsearch import Elasticsearch

fedmsg_config = fedmsg.config.load_config()
es = Elasticsearch(hosts=[{'host': 'elasticsearch', 'port': 9200}])

config_topic = "org.fedoraproject.dev.logger.module.state.change"


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
