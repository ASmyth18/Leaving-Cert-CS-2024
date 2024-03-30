from microbit import *
from max30102 import MAX30102
import radio

# Initialize radio to stream data to a Python file for analysis
radio.on()

# Initialize MAX30102 sensor
max30102 = MAX30102()

# Set up sensor
max30102.setup_sensor()

# User interaction to begin monitoring
while True:
    display.scroll("Do you wish to begin monitoring? Press A for yes, B for no.")
    if button_b.was_pressed():
        break
    elif button_a.was_pressed():
        # Trigger green LED flash on sensor to signal user to place finger
        for _ in range(3):
            max30102.set_led_mode(2)  # Green LED
            sleep(0.5)
            max30102.set_led_mode(0)  # LED off
            sleep(0.5)

        # Scan for finger and begin monitoring if detected
        if max30102.check():
            # Get BPM data
            red_readings = []
            ir_readings = []
            start_time = running_time()
            while running_time() - start_time < 10000:  # Scan for 10 seconds
                max30102.check()
                red_reading = max30102.get_red()
                ir_reading = max30102.get_ir()
                if red_reading is not None and ir_reading is not None:
                    red_readings.append(red_reading)
                    ir_readings.append(ir_reading)
                    sleep(0.02)

            # Calculate and display average BPM and Max/Min BPM
            avg_bpm = sum(red_readings) // len(red_readings)
            max_bpm = max(red_readings)
            min_bpm = min(red_readings)
            display.scroll("Avg BPM: {:.0f}".format(avg_bpm))
            display.scroll("Max BPM: {:.0f}".format(max_bpm))
            display.scroll("Min BPM: {:.0f}".format(min_bpm))

            # Stream data to Python file for analysis
            radio.send("red_readings:" + str(red_readings))
            radio.send("ir_readings:" + str(ir_readings))
        else:
            # No finger detected
            display.scroll("No finger detected: Please place your index finger on the MAX30102.")
