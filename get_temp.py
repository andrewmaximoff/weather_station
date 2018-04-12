from subprocess import Popen, PIPE
import sys


def main():
    with Popen(['/usr/bin/python', '-u', 'temp_4_p2.py'], stdout=PIPE, universal_newlines=True) as process:
        indicators = process.stdout
    return str(indicators).split(' ')


if __name__ == '__main__':
    with Popen(['/usr/bin/python', '-u', 'temp_4_p2.py'], stdout=PIPE, universal_newlines=True) as process:
        indicators = process.stdout
    print(type(indicators))
    print(indicators)
