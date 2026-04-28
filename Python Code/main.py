from machine import I2C, Pin
from pico_i2c_lcd import I2cLcd
from time import sleep
import neopixel
import machine
import utime


# LCD SETUP
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

try:
    lcd.backlight_on()
except:
    pass


# BUTTON SETUP
# These buttons select which roommate is currently active
WhiteButton = Pin(15, Pin.IN, Pin.PULL_UP)
YellowButton = Pin(14, Pin.IN, Pin.PULL_UP)
BlueButton = Pin(13, Pin.IN, Pin.PULL_UP)

# These buttons add or remove guests
SmallRedButton = Pin(12, Pin.IN, Pin.PULL_UP)
SmallBlueButton = Pin(11, Pin.IN, Pin.PULL_UP)

# This button activates STOP MODE (temporary green LED + message)
SMALLButton = Pin(9, Pin.IN, Pin.PULL_UP)


# LED STRIP
n = 8
np = neopixel.NeoPixel(machine.Pin(10), n)


# DATA
# List storing roommate names
roommates = ["Roommate 1", "Roommate 2", "Roommate 3"]

# Stores number of guests each roommate has brought
guest_counts = [0, 0, 0]

# Keeps track of which roommate is currently selected
selected_roommate = 0

# Save program start time (used to track elapsed time later)
program_start = utime.time()

# Name of file where guest activity will be logged
LOG_FILE = "guest_log.txt"


# TIME
def get_time_passed():
    """
    Calculates how much time has passed since the program started.

    Returns:
    hours, minutes, seconds, and total elapsed seconds
    """
    elapsed = utime.time() - program_start
    h = elapsed // 3600
    m = (elapsed % 3600) // 60
    s = elapsed % 60
    return h, m, s, elapsed


# FILE LOG
def log_data(action):
    """
    Saves roommate activity into a text file.
    """
    h, m, s, elapsed = get_time_passed()

    line = "{},{},{},{},{:02d}:{:02d}:{:02d}\n".format(
        roommates[selected_roommate],
        action,
        guest_counts[selected_roommate],
        elapsed,
        h, m, s
    )

    with open(LOG_FILE, "a") as f:
        f.write(line)


# TERMINAL OUTPUT
def print_status(action):
    """
    Prints current roommate activity status to the terminal.
    """
    h, m, s, elapsed = get_time_passed()

    print("----------------------------")
    print("Roommate:", roommates[selected_roommate])
    print("Action:", action)
    print("Guests:", guest_counts[selected_roommate])
    print("Time Passed: {:02d}:{:02d}:{:02d}".format(h, m, s))
    print("Seconds:", elapsed)
    print("----------------------------")


# DISPLAY
def update_display():
    """
    Updates LCD screen to show selected roommate and guest count.
    """
    lcd.clear()
    lcd.putstr(roommates[selected_roommate])
    lcd.move_to(0, 1)
    lcd.putstr("Guests: {}".format(guest_counts[selected_roommate]))


def welcome_screen():
    """
    Displays startup message when program begins.
    """
    lcd.clear()
    lcd.putstr("Guest Tracker")
    lcd.move_to(0, 1)
    lcd.putstr("Ready")
    sleep(2)

    update_display()


# LED
def set_strip(color):
    """
    Changes entire LED strip to one color.
    """
    for i in range(n):
        np[i] = color
    np.write()


# INIT FILE
with open(LOG_FILE, "w") as f:
    f.write("Roommate,Action,Guests,ElapsedSeconds,TimePassed\n")


welcome_screen()

set_strip((255, 0, 0))


# BUTTON STATES
# Stores previous button values so presses only trigger once
last_states = {
    "white": 1,
    "yellow": 1,
    "blue": 1,
    "add": 1,
    "remove": 1,
    "stop": 1
}


# MAIN LOOP
while True:

    # Read current button values
    w = WhiteButton.value()
    y = YellowButton.value()
    b = BlueButton.value()
    add = SmallBlueButton.value()
    rem = SmallRedButton.value()
    stop = SMALLButton.value()


    # SELECT ROOMMATE
    if w == 0 and last_states["white"] == 1:
        selected_roommate = 0
        update_display()
        log_data("Selected")
        print_status("Selected")

    if y == 0 and last_states["yellow"] == 1:
        selected_roommate = 1
        update_display()
        log_data("Selected")
        print_status("Selected")

    if b == 0 and last_states["blue"] == 1:
        selected_roommate = 2
        update_display()
        log_data("Selected")
        print_status("Selected")


    # ADD GUEST
    if add == 0 and last_states["add"] == 1:
        if guest_counts[selected_roommate] < :
            guest_counts[selected_roommate] += 1
            update_display()
            log_data("Added Guest")
            print_status("Added Guest")

        else:
            lcd.clear()
            lcd.putstr("DENIED")
            lcd.move_to(0, 1)
            lcd.putstr("Max 8 Guests")

            for _ in range(3):
                set_strip((255, 0, 0))
                sleep(0.3)
                set_strip((0, 0, 0))
                sleep(0.3)

            set_strip((255, 0, 0))
            update_display()

            log_data("Denied - Max Guests")
            print_status("Denied - Max Guests")


    # REMOVE GUEST
    if rem == 0 and last_states["remove"] == 1:
        if guest_counts[selected_roommate] > 0:
            guest_counts[selected_roommate] -= 1

        update_display()
        log_data("Removed Guest")
        print_status("Removed Guest")


    # STOP MODE
    if stop == 0 and last_states["stop"] == 1:
        lcd.clear()
        lcd.putstr("You're good")
        lcd.move_to(0, 1)
        lcd.putstr("to go")

        set_strip((0, 255, 0))

        log_data("Stop Mode")
        print_status("Stop Mode")

        sleep(3)

        set_strip((255, 0, 0))
        update_display()


    # SAVE STATES
    last_states["white"] = w
    last_states["yellow"] = y
    last_states["blue"] = b
    last_states["add"] = add
    last_states["remove"] = rem
    last_states["stop"] = stop


    sleep(0.05)
