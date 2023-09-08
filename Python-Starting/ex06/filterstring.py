import sys


def main():
    argv = sys.argv
    len_argv = len(argv)
    if len_argv != 3:
        return print("AssertionError: the arguments are bad")
    else:
        try:
            to_num = lambda n : int(n)
            num = to_num(argv[2])
            return print([item for item in argv[1].split(' ') if len(item) > num])
        except:
            return print("AssertionError: the arguments are bad") 


if __name__ == "__main__":
    main()
