import util.constants as consts

# This is the help command
# 
# every command file must define the following methods:
#	execute(context, args) - execute the command and return a new context (or the same if nothing changes)
#		where context is a dictionary with the following:
#			commands - a dictionary of all commands
#			safe - the current open safe, or None if there is none yet
#	short_help() - returns a short (1 line) string describing the command 
# 	long_help() - returns a more in depth description of the command and how to use it, including arg options

def execute(context, args):
	commands = context[consts.CONTEXT_COMMANDS_KEY]

	if len(args) == 0:
		print_all_commands(commands)
	else:
		print_given_commands(commands, args)

	return context

def print_all_commands(cmd_dict):
	print("To get more detailed help for a given command, try help [cmd...]\n")
	for cmd_name, cmd in cmd_dict.items():
		print('{0} - {1}'.format(cmd_name, cmd.short_help()))

def print_given_commands(cmd_dict, to_print):
	for cmd_name in to_print:
		if cmd_name in cmd_dict:
			help_text = cmd_dict[cmd_name].long_help()
		else:
			help_text = "Command not found"

		print('\n{0} - {1}'.format(cmd_name, help_text))

def short_help():
	return "Displays help for a given list of commands or all commands"

def long_help():
	return ("Displays help for a given list of commands or all commands\n"
			"       usage: help [cmd...]\n"
			"       cmd - one or more names of commands to get help for")