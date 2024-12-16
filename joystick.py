import pygame
import sys

# Initialize Pygame
pygame.init()

# Initialize the joystick module
pygame.joystick.init()

# Check for connected joysticks
if pygame.joystick.get_count() == 0:
    print("No joystick detected. Please connect a joystick and restart.")
    sys.exit()

# Select the first joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Joystick detected: {joystick.get_name()}")
print(f"Number of axes: {joystick.get_numaxes()}")
print(f"Number of buttons: {joystick.get_numbuttons()}")
print(f"Number of hats: {joystick.get_numhats()}")

# Loop to read joystick input
try:
    print("\nPress Ctrl+C to exit.")
    while True:
        # Process Pygame events
        for event in pygame.event.get():
            if event.type == pygame.JOYAXISMOTION:
                print(f"Axis {event.axis} moved to {joystick.get_axis(event.axis):.2f}")
            elif event.type == pygame.JOYBUTTONDOWN:
                print(f"Button {event.button} pressed")
            elif event.type == pygame.JOYBUTTONUP:
                print(f"Button {event.button} released")
            elif event.type == pygame.JOYHATMOTION:
                print(f"Hat {event.hat} moved to {joystick.get_hat(event.hat)}")
except KeyboardInterrupt:
    print("\nExiting...")

# Quit Pygame
pygame.quit()