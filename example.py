from kinet import *
import time
import sys
import os

'''
Blue_1 10, 163, 207
Blue_2 0, 101, 196
Blue_3 0, 62, 120
'''

pds = PowerSupply("192.168.50.99")

def ocean_cycle(pds, pause = 0.2):
    for i in range(175, 211) + range(210, 175, -1):
        for k in range(45, 101, 1) + range(100, 45, -1):
            hue = i / float(360.0)
            saturation = 0.95
            value = k / float(100.0)

            print(hue, saturation, value)
            for fixture in pds:
                fixture.hsv = (hue, saturation, value)
            
            pds.go()
            time.sleep(0.2)

def main():
    fix1 = FixtureRGB(0)
    fix2 = FixtureRGB(3)
    fix3 = FixtureRGB(6)
    fix4 = FixtureRGB(9)
    pds.append(fix1)
    pds.append(fix2)
    pds.append(fix3)
    pds.append(fix4)

    while True:
        ocean_cycle(pds)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        pds.clear()
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
