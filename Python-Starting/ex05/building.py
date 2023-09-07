import sys


def main():
    """
    Function that displays the sums of its upper-case characters, lower-case
    characters, punctuation characters, digits and spaces
    """
    arg = ""
    if len(sys.argv) > 2:
        return print("AssertionError: more than one argument is provided")
    elif len(sys.argv) == 2:
        arg = sys.argv[1]
    else:
        try:
            # Read input text until Ctrl+D (EOF) is entered
            # while True:
            line = input("What is the text to count?\n")
            arg += line + '\n'

        except EOFError:
            pass  # Ctrl+D is pressed to signal the end of input

    uppercase_count = 0
    lowercase_count = 0
    punctuation_count = 0
    space_count = 0
    digit_count = 0

    for char in arg:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        elif char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
            punctuation_count += 1
        elif char.isspace():
            space_count += 1
        elif char.isdigit():
            digit_count += 1
    print(f"The text contains {len(arg)} characters")
    print(f"Uppercase: {uppercase_count}")
    print(f"Lowercase: {lowercase_count}")
    print(f"Punctuation: {punctuation_count}")
    print(f"Spaces: {space_count}")
    print(f"Digits: {digit_count}")


if __name__ == "__main__":
    # print(main.__doc__)
    main()
