"""
Very simple temperature poll for the DS18B20 sensor using 1-wire.
"""

import os
import re
import glob
import time

DELAY = 1
BASE_W1_DIR = "/sys/bus/w1/devices/"

device_folder = glob.glob(BASE_W1_DIR + '28*')[0]
device_file = device_folder + '/w1_slave'


def temp_raw():
    """
    Read the file from /sys/bus/w1/28-0218403045ff/w1_slave into strings.
    An example of the lines you read:

    16 01 4b 46 7f ff 0c 10 32 : crc=32 YES
    16 01 4b 46 7f ff 0c 10 32 t=17375

    Returns a list of strings.
    """
    lines = []
    with open(device_file, "r") as f:
        lines = f.readlines()
    return lines

def process_temp():
    """
    We obtain the raw data from the file read and process it to human-readable format!
    """
    raw_value = temp_raw()

    # Sanity checks for if read succeeded
    match = re.search("YES", raw_value[0], re.IGNORECASE)
    if not match:
        print("Error reading from sensor DS18B20")
        return

    # Now obtain the temperature information
    match = re.search("([\w\s]+)(t=)(\d+)", raw_value[1])
    if not match:
        print("Error reading from sensor DS18B20")
        return

    # Conversion
    temp_string = match.group(3)
    temp_c = float(temp_string) / 1000.0
    temp_f = temp_c * 9.0 / 5.0 + 32.0
    return temp_c, temp_f


def main():
    try:
        while True:
            temps = process_temp()
            if temps:
                print("Temperature: {0:.2f}°C or {1:.2f}F".format(temps[0], temps[1]))
            time.sleep(DELAY)
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()
