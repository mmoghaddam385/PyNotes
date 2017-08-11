import util.command_utils as command_utils
import util.constants as consts

from safe import Safe

from getpass import getpass
from os.path import expanduser, isdir, join

# this command opens an existing safe

def execute(context, args):
	if not validate_args(args):
		return context

	# close current safe if one is open
	if not command_utils.confirm_close_current_safe(context):
		return context

	safe_dir = join(args[0], consts.SAFE_ROOT_DIR)
	given_pw = getpass("Enter password: ")

	try:
		new_safe = Safe.open_safe(given_pw, safe_dir)
		context[consts.CONTEXT_SAFE_KEY] = new_safe
	except Exception as ex:
		print("Unable to open safe: ", ex)
		raise ex

	return context

def validate_args(args):
	# num args
	if not command_utils.validate_num_args(args=args, num_args=1, cmd_name='open'):
		return False
	
	args[0] = expanduser(args[0])

	# dir does not exist
	if not isdir(args[0]):
		print("{0} doesn't exist".format(args[0]))
		return False

	# no safe in dir
	if not isdir(join(args[0], consts.SAFE_ROOT_DIR)):
		print("There is no safe in {0}".format(args[0]))
		return False

	return True

def short_help():
	return "This command opens an existing safe"

def long_help():
	return ("This command opens an existing safe in a given location\n"
			"       usage: open <dir>"
			"       dir - the directory that contains the safe")