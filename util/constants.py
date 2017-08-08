
# branding of the program
ASCII_WELCOME_BANNER = """
\n\n\n\n\n\n\n\n\n\n\n\n
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@                                               @
@       ____        _   __      __              @
@      / __ \__  __/ | / /___  / /____  _____   @
@     / /_/ / / / /  |/ / __ \/ __/ _ \/ ___/   @
@    / ____/ /_/ / /|  / /_/ / /_/  __(__  )    @
@   /_/    \__, /_/ |_/\____/\__/\___/____/     @
@         /____/                                @
@                                               @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

To create a safe, use the 'new' command
For more help, use the 'help' command

"""

# the directory where all of the commands are defined
COMMANDS_DIR = "commands/"

# the module where all of the commands are defined
COMMANDS_MODULE = "commands"

# the prompt to display for a new command
COMMAND_PROMPT = "\n>> "

# the max length for the name of a note
NOTE_NAME_MAX_LEN = 20

# the recommended minimum width for the shell to run this program in
RECOMMENDED_SHELL_WIDTH = 50 

# the keys into the context dictionary
CONTEXT_COMMANDS_KEY = "commands"
CONTEXT_SAFE_KEY = "safe"

# the name of the safe directory
SAFE_ROOT_DIR = ".pynote-safe"