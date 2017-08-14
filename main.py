from importlib import import_module
from subprocess import call

import sys, os

from util.interactions import clear_screen

import util.constants as consts

def main():
	clear_screen()
	print(consts.ASCII_WELCOME_BANNER)

	commands = load_commands()
	loop(commands)

# returns a dictionary of command names to their imported modules
def load_commands():
	# valid files include all python files that don't start with '__'
	is_valid_file = lambda file_name: not file_name.startswith('__') and file_name.endswith('.py')

	script_dir = os.path.dirname(os.path.realpath(__file__))
	commands_dir = os.path.join(script_dir, consts.COMMANDS_DIR)

	# map all valid files in the commands dir from their name (minus the .py extension) to their imported module
	commands = {}
	for file in os.listdir(commands_dir):

		# check if this is a valid command file
		if is_valid_file(file):
			file = file[:-3] # strip the .py extension
			module = '{0}.{1}'.format(consts.COMMANDS_MODULE, file)

			commands[file] = import_module(module)

	return commands

# this function will loop forever and execute commands defined in the commands arg
def loop(commands):
	context = {
				consts.CONTEXT_COMMANDS_KEY: commands, 
				consts.CONTEXT_SAFE_KEY: None
			}

	while (True):
		# get input from user
		line = input(consts.COMMAND_PROMPT)
		
		if len(line) > 0:
			words = line.split(' ')

			cmd_name = words[0]
			args = words[1:]

			# special case for exit
			if cmd_name == 'exit':
				break

			# check if the command is in our command dict
			if cmd_name in commands:
				context = commands[cmd_name].execute(context, args)
			else:
				print("Command not found, try 'help'")

	if context[consts.CONTEXT_SAFE_KEY] is not None:
		context[consts.CONTEXT_SAFE_KEY].close()

	# try to clear screen on exit
	clear_screen()

if __name__ == '__main__':
	if sys.version_info.major < consts.MIN_PYTHON_VERSION:
		print("Sorry, this program requires python {0} or newer".format(consts.MIN_PYTHON_VERSION))
	else:
		has_required_libs = True
		try:
			import cryptography
		except ImportError:
			has_required_libs = False
			print("Missing required library 'cryptography' (try `pip install cryptography`)")

		if has_required_libs:
			main()
