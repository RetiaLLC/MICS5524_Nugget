## Skicka 2024 for Retia
## Read a MICS5524 gas sensor on IO17 and buzz a piezo on IO3 if the sensor reading goes over a cutoff of 10000
## Also turns on the neopixel on a USB Nugget
## Requires: USB Nugget, Piezo, MICS5524 sensor

import board
import analogio
import neopixel
import pwmio  # Changed from pulseio to pwmio
import time

# Setup the gas sensor
gas_sensor = analogio.AnalogIn(board.IO17)

# Setup the NeoPixel LED
num_pixels = 1
pixels = neopixel.NeoPixel(board.IO12, num_pixels, brightness=.1)

# Setup the passive buzzer using pwmio
buzzer = pwmio.PWMOut(board.IO3, duty_cycle=0, frequency=3000, variable_frequency=True)

# Function to handle the buzzing logic
def buzz(frequency, duration):
    buzzer.frequency = frequency
    buzzer.duty_cycle = 2**15  # 50% duty cycle
    time.sleep(duration)
    buzzer.duty_cycle = 0

some_threshold = 10000  # Replace with the calibrated threshold value for your sensor

while True:
    # Read the gas sensor value
    sensor_value = gas_sensor.value
    print("Gas sensor reading:", sensor_value)

    # Turn the NeoPixel red and sound the buzzer if gas is detected, green and no buzzer otherwise
    if sensor_value > some_threshold:
        pixels.fill((255, 0, 0))  # Red
        print("Gas Detected!")
        buzz(3000, 0.2)  # Buzz at 3000Hz for 0.2 seconds
    else:
        pixels.fill((0, 255, 0))  # Green
        buzzer.duty_cycle = 0  # Ensure the buzzer is off

    time.sleep(0.1)  # Delay for a bit before reading again
