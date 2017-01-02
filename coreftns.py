from openbot.abstract.plugin import BotPlugin


class PluginBase(BotPlugin):

  plugin_name = "com.jhnhnck.coreftns"
  plugin_prefix = "core"
  plugin_description = "Core functions included with discord-bot-core"
  plugin_version = "0.0.1"

  def load(self):
    super().load()

  def get_functions(self):
    super().get_functions()
    return [
      "clean",
      "config",
      "help",
      "restart",
      "shutdown",
    ]

  def get_default_config(self):
    super().get_default_config()
    return {'version': self.plugin_version}
