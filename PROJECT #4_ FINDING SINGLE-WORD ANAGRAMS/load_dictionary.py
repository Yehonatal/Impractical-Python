"""
    Load a text file as a list.
    Arguments:
        -text file name
    Exceptions:
        -IOError if filename not found.
    Returns:
        -A list of all words in text file in lower case.
    Requires-import sys
"""

import sys

def load(file):
    try:
        with open(file) as in_f:
            loaded_txt = in_f.read().strip().split('\n')
            loaded_txt = [x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as f:
        print("{}\nError opening {}. Terminating program.".format(f, file), file=sys.stderr)
        sys.exit(1)