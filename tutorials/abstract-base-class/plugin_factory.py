class PluginFactory(object):
  registered_plugins = {}

  @classmethod
  def register_plugin(cls, name, plugin):
    PluginFactory.registered_plugins[name] = plugin

  def __init__(self):
    pass

  def get_registered_plugins(self):
    return PluginFactory.registered_plugins
