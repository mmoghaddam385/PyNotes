# Commands

Each module in this directory is imported and can be called as a command in the program.

## Required Exports

#### Execute Function

This function is called when the command is invoked in the program. 

```python
def execute(context, args):
  ...
  return context
```

`context` - a dictionary with information about the context of the program. Keys into the dictionary are in `util.constants.CONTEXT_<key-name>_KEY`  


`args` - the list of arguments passed into the command when invoked by the user

##### Return Value
The function must return a context dictionary.

#### Short Help Function

This function is called when the `help` command is executed with no arguments

```python
def short_help():
  return "A short description of the command"
```

##### Return Value
The function should return a short string describing the command

#### Long Help Function

This function is called when the `help` command is called with this command as an argument

```python
def long_help():
  return "A long description of the command, with usage, etc."
```

##### Return Value
This function should return a longer (multiline) string describing the command and what arguments it takes
