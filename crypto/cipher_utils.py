import util.conversions as conversions

# this module has helper methods for encrypting things

def encrypt_string(plaintext: str, key):
    fernet_key = key.fernet_key()
    plaintext_bytes = conversions.string_to_bytes(plaintext)

    return fernet_key.encrypt(plaintext_bytes).decode()

def decrypt_string(ciphertext: str, key):
    fernet_key = key.fernet_key()
    ciphertext_bytes = conversions.string_to_bytes(ciphertext)

    return fernet_key.decrypt(ciphertext_bytes).decode()