import sys
import Adafruit_DHT

# Temperature and humidity
sensor = Adafruit_DHT.DHT11
pin = 17


def temperature():
    _, result = Adafruit_DHT.read_retry(sensor, pin)
    return 'Temp={:.2f}'.format(result)


def humidity():
    result, _ = Adafruit_DHT.read_retry(sensor, pin)
    return 'Humidity={:.2f}'.format(result)
