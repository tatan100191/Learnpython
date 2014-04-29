# una funcion que permite varios parametros de entrada
def print_two(*args):
    arg1, arg2, arg3= args
    print "arg1: %r, arg2: %r, arg3: %r" % (arg1, arg2, arg3)

# se especifican los parametros de entrada
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %r" % arg1

# Esta es una funcion sin parametros de entrada
def print_none():
    print "I got nothin'."


print_two("Zed","Shaw","tatan")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
