class PluginFactory(object):
  registered_plugins = {}

  @classmethod
  def register_plugin(cls, name, plugin):
    PluginFactory.registered_plugins[name] = plugin

  def __init__(self):
    pass

  def create_plugin(self, plugin_type, param):
    return PluginFactory.registered_plugins[plugin_type](param)
 
  def get_registered_plugins(self):
    return PluginFactory.registered_plugins.keys()
