import util.constants as consts

import os
import tempfile

from subprocess import call

# this module has helper functions relating to notes

# checks if a given note name is valid given a safe
def is_valid_note_name(name, safe):
    if name in consts.RESTRICTED_NOTE_NAMES:
        print("That name is reserved for the system and cannot be used")
        return False

    if name in safe.notes:
        print("A note with that name already exists in the safe")
        return False

    return True

# checks if a filename is a valid note file name
def is_valid_note_file(file_name):
    return not file_name.startswith('.')

# call up an editor and get input from user
# set the editor up with `intitial_text`
def open_edit_note(initial_text=''):
    editor = os.environ.get(consts.NOTE_EDITOR_KEY, consts.NOTE_DEFAULT_EDITOR)

    with tempfile.NamedTemporaryFile(mode='w+', suffix='.tmp') as tf:
        tf.write(initial_text)
        tf.flush()
        call([editor, tf.name])

        tf.seek(0)
        note = tf.read()

    return note