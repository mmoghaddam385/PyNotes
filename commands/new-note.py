import crypto.cipher_utils as cipher_utils
import util.command_utils as command_utils
import util.constants as consts
import util.note_utils as note_utils

from note import Note

# This command makes a new note in the current safe

def execute(context, args):
    if context[consts.CONTEXT_SAFE_KEY] is None:
        print("No open safe")
        return context

    safe = context[consts.CONTEXT_SAFE_KEY]

    if not validate_args(args, safe):
        return context

    note_text = note_utils.open_edit_note()

    if note_text is not None:
        new_note = Note(args[0])
        new_note.save(note_text, safe)

        note_text = ""

        safe.notes.append(new_note)

    return context

def validate_args(args, safe):
    if not command_utils.validate_num_args(args, 1, 'new-note'):
        return False

    if not note_utils.is_valid_note_name(args[0], safe):
        return False

    return True

def short_help():
    return "Create a new note in the current safe"

def long_help():
    return ("Create a new note in the current safe\n"
            "           usage: new-note <name>\n"
            "           name - the name of the note to create")
