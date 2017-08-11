import util.constants as consts
import util.conversions as conversions

from os import urandom

# this module contains classes relating to hashing

# class to hold information about how a hash should be performed
class KDFParams:
    # constructs a new KDFParams object with a random salt and default parameters
    def default():
        salt_bytes = urandom(consts.PASSWORD_SALT_LENGTH)
        salt = conversions.bytes_to_b64string(salt_bytes)

        return KDFParams(salt, consts.PASSWORD_HASH_LENGTH, consts.PASSWORD_HASH_ITERATIONS)

    def __init__(self, salt, output_length, iterations):
        self.salt = salt
        self.output_length = output_length
        self.iterations = iterations

# class to hold information about a hashed password
class HashedPassword:
    # read hash and metadata from file and return a new HashedPassword object
    def read_from_file(file_name):
        with open(file_name, 'r') as file:
            as_string = file.read()
        
        split = as_string.split('|')
        hash = split[0]
        kdf_params = KDFParams(salt=split[1], output_length=int(split[2]), iterations=int(split[3]))

        return HashedPassword(hash, kdf_params)
    
    def __init__(self, hash, kdf_params):
        self.hash = hash
        self.kdf_params = kdf_params

    # save to file in the following format:
    #   passhash|salt|output_length|iterations
    # NOTE: this function will overwrite the file if it already exists
    def save_to_file(self, file_name):
        as_string = '{0}|{1}|{2}|{3}'.format(self.hash, self.kdf_params.salt, self.kdf_params.output_length, self.kdf_params.iterations)
        
        with open(file_name, 'w') as file:
            file.write(as_string)

    def destroy(self):
        self.hash = None
        self.kdf_params = None