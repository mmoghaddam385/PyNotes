from importlib import import_module

import util.constants as consts

_open_safe = import_module("commands.open-safe")
_open_note = import_module("commands.open-note")

# this command chooses between forwarding to open-safe or open-note command based on context
# open-safe if no safe is open yet
# open-note otherwise

def execute(context, args):
    if context[consts.CONTEXT_SAFE_KEY] is None:
        print("Delegating to open-safe...")
        return _open_safe.execute(context, args)
    else:
        print("Delegating to open-note...")
        return _open_note.execute(context, args)

def short_help():
    return "Delegates to either 'open-safe' or 'open-note' depending on context"

def long_help():
    return ("Delegates to 'open-safe' if no safe is currently open\n"
            "      Delegates to 'open-note' otherwise")
