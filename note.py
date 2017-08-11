import crypto.cipher_utils as cipher_utils
import util.note_utils as note_utils

from os import listdir, remove
from os.path import isfile, join

# this class encapsulates a note

class Note:
    # class function that loads all notes in a directory and returns them as a list
    def load_from_dir(dir, key):
        notes = []

        for file in listdir(dir):
            full_path = join(dir, file)
            if isfile(full_path) and note_utils.is_valid_note_file(file):
                notes.append(Note.load_from_file(file, key))

        return notes

    # class function that loads a note's metadata from a file name and key
    def load_from_file(file_name, key):
        decrypted_name = cipher_utils.decrypt_string(file_name, key)
        
        return Note(decrypted_name, file_name)

    def __init__(self, name, file_name=None):
        self.name = name
        self.file_name = file_name

    # encrypts contents and saves to disk
    # NOTE this function will delete the old note file it it existed
    def save(self, contents, safe):
        encrypted_filename = cipher_utils.encrypt_string(self.name, safe.derived_key)
        encrypted_contents = cipher_utils.encrypt_string(contents, safe.derived_key)
        contents = ""

        with open(join(safe.safe_dir, encrypted_filename), 'w') as file:
            file.write(encrypted_contents)
        
        # delete old file
        if self.file_name is not None:
            remove(join(safe.safe_dir, self.file_name))

        self.file_name = encrypted_filename