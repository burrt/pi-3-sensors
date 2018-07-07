# DS18B20 Sensor

Currently, the code has been tested on the Waterproof DSB1820 although it should work with the non-waterproof version (I fried my non-waterproof DS18B20 haha). I used the 1-wire interface because it was easy to setup and configure and test this sensor ASAP!

## Setup

Enable the 1-wire interface on your Raspberry Pi, I'm running `Linux raspberrypi 4.14.50-v7+ #1122 SMP armv7l GNU/Linux`, Raspbian Stretch Lite.

If found the easiest and with the lowest probability of screwing your boot settings:

```bash
sudo raspi-config

# Go to Interface settings -> Enable 1-Wire
# Finish

# Now if you run:
tail /boot/config.txt
# dtoverlay=w1-gpio
```

You can edit this file manually if you wanted to, although you may screw your boot configuration which really isn't ideal.

This also assumes you have loaded the following modules already `w1-gpio` and `w1-therm`. If you haven't done so, run:

```bash
sudo modprobe w1-gpio
sudo modprobe w1-therm

# Check with:
lsmod
```

And if you're tired of running those at the start, append to your `/etc/modules`:

```
# /etc/modules: kernel modules to load at boot time.
#
# This file contains the names of kernel modules that should be loaded
# at boot time, one per line. Lines beginning with "#" are ignored.

# 1-wire for DS1B20
w1-gpio
w1-therm
```

## Circuit

GPIO4 is the default for 1-wire interface.

```
                    ███
                   / | \
                  /  |  \
                 |   |   +-------------+
GND  ------------+   |                 |
GPIO ----------------+---R = 4.7 kOhm--+
                                       |
3V   ----------------------------------+

```

## Running

It's only compatible with Python 3.x:

```bash
python3 therm.py
```
### Output

```
Temperature: 19.69°C or 67.44F
Temperature: 19.69°C or 67.44F
Temperature: 19.88°C or 67.78F
Temperature: 20.31°C or 68.56F
Temperature: 20.81°C or 69.46F
Temperature: 21.25°C or 70.25F
Temperature: 21.62°C or 70.92F
Temperature: 21.88°C or 71.38F
Temperature: 22.00°C or 71.60F
^C
Exiting...
```