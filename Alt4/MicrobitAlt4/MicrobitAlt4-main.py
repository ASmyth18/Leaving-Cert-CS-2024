from microbit import *
import music

# Define the tunes
tune_low = ["C4:4", "D4:4", "E4:4", "C4:4"]
tune_medium = ["E4:4", "F4:4", "G4:4", "E4:4"]
tune_high = ["G4:4", "A4:4", "B4:4", "G4:4"]

# Define the light level thresholds
low_threshold = 50
high_threshold = 200

playing = False

while True:
    # Read the light level
    light_level = display.read_light_level()
    
    # Display the light level on the LED matrix
    display.scroll("Light: " + str(light_level), delay=100)
    
    # Play the tune based on the light level
    if not playing:
        if light_level < low_threshold:
            music.play(tune_low)
        elif light_level < high_threshold:
            music.play(tune_medium)
        else:
            music.play(tune_high)
        playing = True
    
    # Check for button presses
    if button_a.was_pressed():
        # Pause or resume the music
        if playing:
            music.stop()
            playing = False
        else:
            if light_level < low_threshold:
                music.play(tune_low)
            elif light_level < high_threshold:
                music.play(tune_medium)
            else:
                music.play(tune_high)
            playing = True
    
    if button_b.was_pressed():
        # Stop the music and clear the display
        music.stop()
        display.clear()
        playing = False
        break
    
    sleep(500)