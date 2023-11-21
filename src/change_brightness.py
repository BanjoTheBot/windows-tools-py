"""
    Changes brightness as inputted by user.
    Shamelessly stolen from StackOverflow.

    Only works on whatever monitor is "first".
    Also only works on some monitors, for some reason.
"""
import wmi


def main():
    brightness = input("Input desired brightness value (0 - 100) ")
    c = wmi.WMI(namespace='wmi')
    methods = c.WmiMonitorBrightnessMethods()[0]
    methods.WmiSetBrightness(brightness, 0)


if __name__ == '__main__':
    main()
