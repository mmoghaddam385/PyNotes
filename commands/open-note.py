import util.constants as consts
import util.command_utils as command_utils
import util.note_utils as note_utils

# this command opens an existing note for viewing/editing

def execute(context, args):
    if context[consts.CONTEXT_SAFE_KEY] is None:
        print("No open safe")
        return context

    safe = context[consts.CONTEXT_SAFE_KEY]

    if not validate_args(args, safe):
        return context

    note = safe.get_note_by_name(args[0])
    old_contents = note.get_contents(safe)

    new_contents = note_utils.open_edit_note(old_contents)

    if old_contents != new_contents:
        print("Saving...", end="")
        note.save(new_contents, safe)
        print("done")

    return context

def validate_args(args, safe):
    if not command_utils.validate_num_args(args, 1, "open-note"):
        return False

    if not args[0] in safe.notes:
        print("No such note")
        return False

    return True

def short_help():
    return "Open a note for viewing/editing"

def long_help():
    return ("Open a note for viewing/editing; any saved changes will persist\n"
            "            usage: open-note <name>\n"
            "            name - the name of the note to open")
