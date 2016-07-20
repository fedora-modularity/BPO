from elasticsearch import Elasticsearch
import fedmsg
from datetime import datetime

es = Elasticsearch(hosts=[{'host': 'elasticsearch', 'port': 9200}])


def module_state_change(name, version, release, state):
    id = "{}-{}-{}".format(name, version, release)
    module = {
        "name": name,
        "version": version,
        "release": release,
        "build_state": state,
        'updated': datetime.now(),
    }

    res = es.index(index="modularity", doc_type='module', id=id, body=module)

module_state_change("cheese-piza", "2.6", "42", "wait")

print ("I can not do anything yet. Bye!")
