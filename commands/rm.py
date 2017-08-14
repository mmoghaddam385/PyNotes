from importlib import import_module

_rm_note = import_module("commands.rm-note")

# alias for rm-note

def execute(context, args):
    return _rm_note.execute(context, args)

def short_help():
    return "Alias for 'rm-note'"

def long_help():
    return "Alias for 'rm-note'"
