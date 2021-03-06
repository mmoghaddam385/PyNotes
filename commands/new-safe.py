import util.command_utils as command_utils
import util.constants as consts

from safe import Safe
from util.interactions import confirm_action, create_password

from os.path import expanduser, isdir, join
from os import makedirs

# this command creates a new safe in a given directory
# it also sets up the required crypto elements that go along with it

def execute(context, args):
	if not validate_args(args):
		# if we have invalid args, finish the command here
		return context

	# check if there's an open safe already
	if not command_utils.confirm_close_current_safe(context):
		return context

	# everything is good to go, start making that safe!
	pw = create_password("Create a password for the new safe: ")

	context[consts.CONTEXT_SAFE_KEY] = Safe.init_safe(args[0], pw)
	pw = ""

	return context

# validates the args; require one that points to a valid directory
def validate_args(args):
	# num args
	if not command_utils.validate_num_args(args=args, num_args=1, cmd_name='new-safe'):
		return False

	args[0] = expanduser(args[0])

	# dir does not exist
	if not isdir(args[0]):
		confirmed = confirm_action("{0} doesn't exist, should I create it for you?".format(args[0]))
		if confirmed:
			makedirs(args[0])
		else:
			return False

	# safe already exists in dir
	if isdir(join(args[0], consts.SAFE_ROOT_DIR)):
		print("A safe already exists in {0}".format(args[0]))
		return False

	return True


def short_help():
	return "Creates a new safe"

def long_help():
	return ("Creates a new safe\n"
			"           usage: new <dir>\n"
			"           dir - the parent directory in which to create the new note safe")