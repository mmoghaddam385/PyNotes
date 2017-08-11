import util.constants as consts

# this command closes the current safe

def execute(context, args):
    if context[consts.CONTEXT_SAFE_KEY] is not None:
        context[consts.CONTEXT_SAFE_KEY].close()
        context[consts.CONTEXT_SAFE_KEY] = None
        print("Safe closed")
    else:
        print("No open safe")

    return context

def short_help(): 
    return "Close the current safe"

def long_help(): 
    return short_help()