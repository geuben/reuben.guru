from plugin_factory import PluginFactory

class PluginB(object):
  def __init__(self, param):
    self.__param = param
    pass

  @classmethod
  def name(cls):
    return "PluginB"

  def do_something(self):
    print "I am PluginB doing something : " + self.__param

PluginFactory().register_plugin(PluginB.name(), PluginB)
