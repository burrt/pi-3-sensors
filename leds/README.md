# LED

Basic led toggler that toggles on/off every 4 seconds. On Ctrl+C, it should turn your LED off.

## Circuit

```
             +---+
GPIO --------|LED|-----+
             +---+     |
                       |
                       R = 330 Ohm
                       |
                       |
GND  ------------------+

```

## Running

It can be run with Python 2.x or Python 3.x.

```
# If you haven't done so:
# sudo apt-get install python-rpi.gpio
# sudo apt-get install python3-rpi.gpio

python leds.py
```
