from plugin_factory import PluginFactory
from plugins import *

pf = PluginFactory()

some_parms = [ "1", "8", "6" , "10" ]
registered_plugins = pf.get_registered_plugins()
plugin_instances = []

count = 0
for x in range(0, 2):
  for p in registered_plugins:
    plugin_instances.append(pf.create_plugin(p, some_parms[count]))
    count +=1

for pi in plugin_instances:
  pi.do_something()
