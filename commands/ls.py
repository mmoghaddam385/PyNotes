import util.constants as consts

# this command lists all notes in the current safe

def execute(context, args):
    if context[consts.CONTEXT_SAFE_KEY] is None:
        print("No open safe")
        return context

    if not validate_args(args):
        return context

    safe = context[consts.CONTEXT_SAFE_KEY]

    if len(args) == 1 and args[0] == '-l':
        long_print(safe.notes, safe.safe_dir)
    else:
        short_print(safe.notes)

    return context

def validate_args(args):
    if len(args) > 1:
        print("Too many arguments")
        return False

    if len(args) == 1 and args[0] != '-l':
        print("Unknown argument:", args[0])
        print("Try 'help ls'")
        return False

    return True

def long_print(notes, safe_dir):
    print("\nThe safe is located in", safe_dir)
    print("There are", len(notes), "note(s) in the safe\n")

    longest = max([len(note.name) for note in notes])

    for note in notes:
        print("{0} ->  {1}".format(note.name.ljust(longest), note.file_name))

def short_print(notes):
    for note in notes:
        print(note.name)

def short_help():
    return "Lists the notes in the currently open safe"

def long_help():
    return ("Lists the notes in the currently open safe\n"
            "     usage: ls [-l]\n"
            "     [-l] - optional long print; displays more information about each note")