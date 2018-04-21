import subprocess


def barometer():
    command = ["python", "test_bar.py"]
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = p.stdout.readlines()
    output = [i.decode() for i in output]
    return ''.join(output)


def tempr():
    command = ["python", "test_bar.py"]
    p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = p.stdout.readlines()
    output = [i.decode() for i in output]
    return output[2]
