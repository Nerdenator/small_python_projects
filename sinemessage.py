import math
import shutil
import sys
import time

WIDTH, HEIGHT = shutil.get_terminal_size()
# we can't print to the last column on Windows without it adding
# a newline automatically, so reduce width by one:
WIDTH -= 1


def get_message():
    message = input(f'What message do you want to display? (Max {WIDTH // 2} chars.)')
    if len(message) > (WIDTH // 2):
        print("Message too long.")
        get_message()
    sine_wave(message)


def sine_wave(msg):
    step = 0.0   # The "step" determines how far into the sine wave we are.
    # Sine goes from -1.0 to 1.0, so we need to change it by a multiplier
    multiplier = (WIDTH - len(msg)) / 2
    try:
        while True:     # Main program loop
            sin_of_step = math.sin(step)
            padding = ' ' * int((sin_of_step + 1) * multiplier)
            print(padding + msg)
            time.sleep(0.1)
            step += 0.25
    except KeyboardInterrupt:
        sys.exit()


if __name__ == '__main__':
    get_message()