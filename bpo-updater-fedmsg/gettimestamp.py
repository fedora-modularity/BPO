import subprocess
import shlex
from datetime import datetime

def getTimestamp(container_name):
    # Grab command line results from 'docker ps -a'
    cmd = 'docker ps -a'
    result = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE)
    output = result.communicate()[0]

    #Convert results into a list
    items = output.decode().split()
    items.reverse()

    #Find bpo_fedmsg container ID in 'filelist'
    bpo_container = next((x for x in items if x==container_name), None)
    idx_bpo_container = items.index(bpo_container)
    bpo_container_id = items[idx_bpo_container + 1]

    #Get timestamp (finally)
    timestamp_cmd = 'docker logs --tail=2 -t ' + str(bpo_container_id)
    timestamp_result = subprocess.Popen(shlex.split(timestamp_cmd), stdout=subprocess.PIPE)
    (timestamp_output,stderr) = timestamp_result.communicate()
    timestamp = timestamp_output.decode().split()[0]

    #Convert timestamp to datetime object
    t = timestamp[0:10] +' ' + timestamp[11:19] #format is 2016-08-22T08:28:09.945649000Z
    dt = datetime.strptime(t, "%Y-%m-%d %H:%M:%S")
    return dt

ts = getTimestamp('bpo_bpo-updater-fedmsg')
print ts
