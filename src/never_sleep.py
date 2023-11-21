"""
    Prevents the system going into sleep mode, regardless of power settings
"""
from wakepy import keep


def main():
    with keep.presenting():
        print("Your system is currently being kept awake with a Python script")
        print("Be sure not to leave it open somewhere unsecure!")
        print("\nPress Ctrl + C to stop the script and let your computer get some rest")

        while True:
            continue


if __name__ == '__main__':
    main()
