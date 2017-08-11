
# min python version
MIN_PYTHON_VERSION = 3

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

# the recommended minimum width for the shell to run this program in
RECOMMENDED_SHELL_WIDTH = 50 

# the keys into the context dictionary
CONTEXT_COMMANDS_KEY = "commands"
CONTEXT_SAFE_KEY = "safe"

# safe file structure constants
SAFE_ROOT_DIR = ".pynote-safe"
SAFE_PASSWORD_FILE = ".password"
SAFE_KEY_FILE = ".key"

# note constants
NOTE_NAME_MAX_LEN = 20
RESTRICTED_NOTE_NAMES = [SAFE_PASSWORD_FILE, SAFE_KEY_FILE]

# string encoding to use throughout the program
STANDARD_ENCODING = "utf-8"

# password hashing related constants
PASSWORD_HASH_ITERATIONS = 10000
PASSWORD_HASH_LENGTH = 32
PASSWORD_SALT_LENGTH = 16

# master key related constants
MASTER_KEY_LENGTH = 256