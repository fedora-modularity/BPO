sleep 15
cat fedmsg_new_build.txt | fedmsg-logger --json-input --modname rida --topic module.state.change
