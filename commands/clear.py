from shutil import get_terminal_size

# this command clears the screen by printing a bunch of newlines

def execute(context, args):
	shell_height = get_terminal_size().lines

	print('\n' * shell_height)

	return context

def short_help():
	return 'Clear the screen'

def long_help():
	return short_help()