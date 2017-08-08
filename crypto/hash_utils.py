import util.conversions as conversions

from crypto.hash_classes import KDFParams, HashedPassword

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

# this module has helper functions for securely hashing passwords
        
# this function takes a password and hashes it for verification purposes
# use this when the user first creates their password
def create_verification_hash(password):
    kdf_params = KDFParams.default()

    # double hash because verification
    hash = _hash_string(_hash_string(conversions.string_to_bytes(password), kdf_params), kdf_params)
    password = ""

    hash = conversions.bytes_to_b64string(hash)
    return HashedPassword(hash, kdf_params)

# hash a password to derive a key from it
# NOTE: don't use this function to verify keys
def hash_for_key(password, kdf_params):
    hash = _hash_string(conversions.string_to_bytes(password), kdf_params)
    password = ""

    hash = conversions.bytes_to_b64string(hash)
    return HashedPassword(hash, kdf_params)

# internal function to actually perform the hashing
# message must be bytes
def _hash_string(message, kdf_params):
    salt = conversions.string_to_bytes(kdf_params.salt)

    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length = kdf_params.output_length,
        salt = salt,
        iterations = kdf_params.iterations,
        backend = default_backend()
    )

    return kdf.derive(message)

