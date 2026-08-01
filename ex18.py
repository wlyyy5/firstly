# this one is like your scripts with argv
def print_two(*args):
arg1,arg2 = args
print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this
