from importlib import import_module

import util.constants as consts

_new_safe = import_module("commands.new-safe")
_new_note = import_module("commands.new-note")

# this command chooses between forwarding to new-safe or new-note command based on context
# new-safe if no safe is open yet
# new-note otherwise

def execute(context, args):
    if context[consts.CONTEXT_SAFE_KEY] is None:
        print("Delegating to new-safe...")
        return _new_safe.execute(context, args)
    else:
        print("Delegating to new-note...")
        return _new_note.execute(context, args)

def short_help():
    return "Delegates to either 'new-safe' or 'new-note' depending on context"

def long_help():
    return ("Delegates to 'new-safe' if no safe is currently open\n"
            "      Delegates to 'new-note' otherwise")
