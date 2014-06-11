import abc

class IPlugin(object):
  __metaclass__ = abc.ABCMeta

  @abc.abstractmethod
  def do_something(self):
    return
