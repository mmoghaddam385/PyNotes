import util.constants as consts
import util.command_utils as command_utils

# this command removes a note from the safe

def execute(context, args):
    if context[consts.CONTEXT_SAFE_KEY] is None:
        print("No open safe")
        return context

    safe = context[consts.CONTEXT_SAFE_KEY]

    if not validate_args(args, safe):
        return context

    if command_utils.confirm_action("This action is permanent, are you sure?"):
        print("Removing...", end="")
        note = safe.get_note_by_name(args[0])
        safe.remove_note(note)
        print("done")

    return context

def validate_args(args, safe):
    if not command_utils.validate_num_args(args, 1, "rm-note"):
        return False

    if not args[0] in safe.notes:
        print("No such note")
        return False

    return True

def short_help():
    return "Removes the given note from the safe"

def long_help():
    return ("Removes the given note from the safe\n"
            "          usage: rm-note <note>\n"
            "          <note> - the name of the note to remove")
