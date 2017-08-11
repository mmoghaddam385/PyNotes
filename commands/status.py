import util.constants as consts

# this command shows the status of the current open safe

def execute(context, args):
    if context[consts.CONTEXT_SAFE_KEY] is not None:
        safe = context[consts.CONTEXT_SAFE_KEY]
        print("Current safe located in:")
        print(safe.safe_dir)
        print("\nThere are", len(safe.notes), "note(s) in the safe")
    else:
        print("No open safe")

    return context

def short_help():
    return "Display the status of the current open safe (if there is one)"

def long_help():
    return short_help()