from plugin_factory import PluginFactory

class PluginA(object):
  def __init__(self, param):
    self.__param = param
    pass

  @classmethod
  def name(cls):
    return "PluginA"

  def do_something(self):
    print "I am PluginA doing something: " + self.__param

PluginFactory().register_plugin(PluginA.name(), PluginA)
