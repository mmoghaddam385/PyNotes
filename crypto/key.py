import util.constants as consts
import util.conversions as conversions

from cryptography.fernet import Fernet
from os import urandom
from os.path import join

# this module contains classes that encapsulate encryption keys

class Key:
    # class function that generates, encrypts and saves a new key to disk
    # return an unencrypted version of the key
    def generate_and_encrypt(password: str, safe_dir):
        mkey = Fernet(conversions.string_to_bytes(password))
        
        dkey_bytes = Fernet.generate_key()
        enc_dkey = mkey.encrypt(dkey_bytes).decode()

        with open(join(safe_dir, consts.SAFE_KEY_FILE), 'w') as key_file:
            key_file.write(enc_dkey)

        return Key(dkey_bytes)

    def __init__(self, key: bytes):
        self.key = key

    def fernet_key(self):
        return Fernet(self.key)

    def destroy(self):
        self.key = None