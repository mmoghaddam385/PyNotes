import util.constants as consts

from os import mkdir
from os.path import join

# this class describes a safe object

class Safe:

	# class function that initializes a safe in the filesystem given a directory and password
	def init_safe(dir, password):
		safe_dir = join(dir, consts.SAFE_ROOT_DIR)
		mkdir(safe_dir)