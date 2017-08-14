import util.constants as consts
import util.command_utils as command_utils

# this command deletes an entire safe

def execute(context, args):
    if context[consts.CONTEXT_SAFE_KEY] is None:
        print("No open safe")
        return context

    safe = context[consts.CONTEXT_SAFE_KEY]

    if not command_utils.validate_num_args(args, 0, "rm-safe"):
        return context

    if command_utils.confirm_action("This action is permanent, are you sure?"):
        print("Removing...", end="")
        safe.delete()
        context[consts.CONTEXT_SAFE_KEY] = None
        print("done")

    return context

def short_help():
    return "Deletes the current safe from the filesystem"

def long_help():
    return short_help()
