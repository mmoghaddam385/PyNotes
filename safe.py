import crypto.cipher_utils as cipher_utils
import crypto.hash_utils as hash_utils
import util.constants as consts
import util.conversions as conversions

from crypto.hash_classes import HashedPassword
from crypto.key import Key
from note import Note

from os import mkdir
from os.path import join

# this class describes a safe object

class Safe:

	# class function that initializes a safe in the filesystem given a directory and password
	def init_safe(dir, password):
		safe_dir = join(dir, consts.SAFE_ROOT_DIR)
		mkdir(safe_dir)

		verification_hash = hash_utils.create_verification_hash(password)
		key_hash = hash_utils.hash_for_key(password, verification_hash.kdf_params)

		password = ""

		verification_hash.save_to_file(join(safe_dir, consts.SAFE_PASSWORD_FILE))
		dkey = Key.generate_and_encrypt(key_hash.hash, safe_dir)

		print("mkey:", key_hash.hash)
		print("dkey:", dkey.key)

		return Safe(safe_dir, [], dkey)

	# class function that opens an existing safe and returns a new safe object
	def open_safe(given_pw: str, dir):
		#	0: read password file
		expected_pw = HashedPassword.read_from_file(join(dir, consts.SAFE_PASSWORD_FILE))
		
		#	1: verify password
		if not hash_utils.verify_password(given_pw, expected_pw):
			raise Exception("incorrect password")

		#	2: get key_hash
		mkey_hashed = hash_utils.hash_for_key(given_pw, expected_pw.kdf_params)
		mkey = Key(conversions.string_to_bytes(mkey_hashed.hash))
		given_pw = ""

		#	4: open encyrpted key file
		with open(join(dir, consts.SAFE_KEY_FILE)) as key_file:
			encrypted_key = key_file.read()

		#	5: decyrpt derived key
		dkey_string = cipher_utils.decrypt_string(encrypted_key, mkey)
		dkey = Key(conversions.string_to_bytes(dkey_string))
		
		mkey_hashed.destroy()
		mkey.destroy()

		#	6: decrpyt file names to get note names
		notes = Note.load_from_dir(dir, dkey)

		# 	7: return new safe with info
		return Safe(dir, notes, dkey)

	def __init__(self, safe_dir, notes, derived_key: Key):
		self.safe_dir = safe_dir
		self.notes = notes
		self.derived_key = derived_key

	# close this safe by disregarding all sensitive info
	def close(self):
		self.safe_dir = ""
		self.notes = []

		if self.derived_key is not None:
			self.derived_key.destroy()
			self.derived_key = None