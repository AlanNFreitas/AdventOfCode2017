import os
import __main__ as main

def input_file():
    return open('input_files/{}.txt'.format(
            os.path.basename(main.__file__).split('.')[0]))

def input_string():
    return input_file().read().rstrip('\n')
