from openbot.abstract.function import FunctionBase


class BotFunction(FunctionBase):
  """
  Stub file for jhnhnck_coreftns/chat_update.py
  Auto-generated by discord-bot-core on 2017-02-15 10:21:10.582597
  """

  def load_test(self):
    """
    Loading Self Test.
    Implement this method to allow for more vigorous control over loading requirements.

    Returns:
      Dictionary with two keys:
        state: True if the function should be loaded
        msg: Detailed error message (Do not use logging here; It may not always work)
    """
    return {'state': False, 'msg': 'Stub Function'}

  def call(self, args, mod):
    """
    Call.
    Main entry point for a function called with a command is initialized.

    Args:
      args: array of arguments passed by the user
      mod: dictionary of modifiers passed by the user that are also defined in the pluginname.json file; extra modifiers
       are silently ignored
    """
    pass
