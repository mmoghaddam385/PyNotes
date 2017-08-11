import util.constants as consts

from util.interactions import confirm_action

# this module has helper methods for commands

# this method checks if a safe is open in the given context,
# then prompts the user to close it if there is one
# return True if either no safe was open or current safe was close, False otherwise
def confirm_close_current_safe(context):
	# check if there's an open safe already
	if context[consts.CONTEXT_SAFE_KEY] != None:
		confirmed = confirm_action("Warning: this will close the current safe, are you sure you want to continue?")
		
		if not confirmed:
			# not confirmed? just finish the command here
			return False
		else:
			# else close the safe and continue
			context[consts.CONTEXT_SAFE_KEY].close()

	# either no safe or safe was closed
	return True
	
# checks if the correct number of arguments was supplied, prints appropriate message if not
# return True if len(args) == num_args
def validate_num_args(args, num_args, cmd_name):
	# too few args
	if len(args) < num_args:
		print("Not enough arguments, try 'help {0}'".format(cmd_name))
		return False
	
	# too many args
	if len(args) > num_args:
		print("Too many arguments, try 'help {0}".format(cmd_name))
		return False

	return True