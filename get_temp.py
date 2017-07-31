import subprocess


def main():
    return subprocess.Popen('python temp_4_p2.py', stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout


if __name__ == '__main__':
    main()
