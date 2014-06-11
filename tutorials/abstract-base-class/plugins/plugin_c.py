from plugin_factory import PluginFactory
from i_plugin import IPlugin

class PluginC(IPlugin):
  def __init__(self):
    pass

  @classmethod
  def name(cls):
    return "PluginC"

PluginFactory().register_plugin(PluginC().name(), PluginC())
