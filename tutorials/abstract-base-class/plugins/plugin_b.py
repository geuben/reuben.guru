from plugin_factory import PluginFactory
from i_plugin import IPlugin

class PluginB(IPlugin):
  def __init__(self):
    pass

  @classmethod
  def name(cls):
    return "PluginB"

  def do_something(self):
    print "I am PluginB doing something"

PluginFactory().register_plugin(PluginB().name(), PluginB())
