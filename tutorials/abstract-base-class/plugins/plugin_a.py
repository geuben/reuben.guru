from plugin_factory import PluginFactory
from i_plugin import IPlugin

class PluginA(IPlugin):
  def __init__(self):
    pass

  @classmethod
  def name(cls):
    return "PluginA"

  def do_something(self):
    print "I am PluginA doing something"

PluginFactory().register_plugin(PluginA().name(), PluginA())
