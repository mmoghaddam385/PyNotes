from getpass import getpass

# prompt the user to confirm a given action
# the user is prompted repeatedly until valid input is recieved
# return True if user confirms, False otherwise
def confirm_action(msg):
	while True:
		answer = input('{0} (y/n) '.format(msg))

		if len(answer) == 1:
			if answer.lower() == 'y':
				return True
			elif answer.lower() == 'n':
				return False


# prompt the user to enter a password
# the user must then confirm the password
# return the confirmed password
def create_password(initial_prompt, confirm_prompt="Confirm your password: "):
	while True:
		pw = getpass(prompt=initial_prompt)
		confirmation = getpass(prompt=confirm_prompt)

		if pw == confirmation:
			break
		else:
			print("Passwords didn't match, try again\n")

	confirmation = ""
	return pw