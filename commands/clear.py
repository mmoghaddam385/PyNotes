from util.interactions import clear_screen

# this command clears the screen by printing a bunch of newlines

def execute(context, args):
	clear_screen()
	return context

def short_help():
	return 'Clear the screen'

def long_help():
	return short_help()