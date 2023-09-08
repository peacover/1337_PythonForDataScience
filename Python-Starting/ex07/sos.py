import sys

def main():
    argv = sys.argv
    len_args = len(argv)
    if (len_args != 2):
        return print("AssertionError: the arguments are bad")
    arg = argv[1]
    NESTED_MORSE = {'A': '.-', 'B': '-...',
                    'C': '-.-.', 'D': '-..', 'E': '.',
                    'F': '..-.', 'G': '--.', 'H': '....',
                    'I': '..', 'J': '.---', 'K': '-.-',
                    'L': '.-..', 'M': '--', 'N': '-.',
                    'O': '---', 'P': '.--.', 'Q': '--.-',
                    'R': '.-.', 'S': '...', 'T': '-',
                    'U': '..-', 'V': '...-', 'W': '.--',
                    'X': '-..-', 'Y': '-.--', 'Z': '--..',
                    '1': '.----', '2': '..---', '3': '...--',
                    '4': '....-', '5': '.....', '6': '-....',
                    '7': '--...', '8': '---..', '9': '----.',
                    '0': '-----', ' ': '/'}
    for item in arg:
        if item.upper() not in NESTED_MORSE.keys():
            return print("AssertionError: the arguments are bad")
    ret_str = []
    [ret_str.append(NESTED_MORSE[item.upper()] + ' ') for item in arg]
    print(''.join(ret_str))


if __name__ == "__main__":
    main()
