from plugin_factory import PluginFactory
from plugins import *

pf = PluginFactory()
loaded_plugins = pf.get_registered_plugins()
for loaded_plugin in loaded_plugins:
  loaded_plugins[loaded_plugin].do_something()
