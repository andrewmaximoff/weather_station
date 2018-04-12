import struct
import smbus
import time
# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04


def get_data():
    return bus.read_i2c_block_data(address, 0)


def get_float(data, index):
    bytes = data[4*index:(index+1)*4]
    return struct.unpack('f', "".join(map(chr, bytes)))[0]


def get_val():
    data = get_data()
    temperature = get_float(data, 0)
    luminosity = get_float(data, 1)
    return ' '.join([temperature, luminosity])


if __name__ == '__main__':
    print(get_val())
