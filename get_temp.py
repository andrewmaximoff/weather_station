from subprocess import Popen, PIPE
import sys

if __name__ == '__main__':
    with Popen(['/usr/bin/python', '-u', 'temp_4_p2.py'], stdout=PIPE, universal_newlines=True) as process:
        for line in process.stdout:
            print(line, end='')
