import sys

def even_or_odd(argv):
    len_args = len(argv)
    if len_args > 2:
        print("AssertionError: more than one argument is provided")
    elif len_args == 2:
        arg = sys.argv[1]
        if arg[0] == '-':
            arg = arg[1:]
        if not arg.isnumeric():
            print("AssertionError: argument is not an integer")
        else:
            if int(arg) % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
                
argv = sys.argv
even_or_odd(argv)