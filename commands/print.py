import util.constants as consts
import util.command_utils as command_utils

# this command prints the contents of a note
# NOTE the contents can be viewed by anyone with access to the terminal and won't be cleared

def execute(context, args):
    if context[consts.CONTEXT_SAFE_KEY] is None:
        print("No open safe")
        return context

    safe = context[consts.CONTEXT_SAFE_KEY]

    if not validate_args(args, safe):
        return context

    print("WARNING: This command will print the contents of the note to STDOUT.")
    print("Anyone with access to this terminal can potentially read it\n")
    if not command_utils.confirm_action("Are you sure you want to continue?"):
        return context

    note = safe.get_note_by_name(args[0])

    print("\n----------", note.name, "----------\n")
    print(note.get_contents(safe))
    print("-----------{0}-----------".format("-" * len(note.name)))
    return context

def validate_args(args, safe):
    if not command_utils.validate_num_args(args, 1, "print"):
        return False

    if not args[0] in safe.notes:
        print("No such note")
        return False

    return True

def short_help():
    return "Print the contents of a note to the screen"

def long_help():
    return ("Print the contents of a note to the screen\n"
            "        usage: print <note>\n"
            "        note - the name of the note to print")