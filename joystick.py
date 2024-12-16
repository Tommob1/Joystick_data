import pygame
import sys
import time

def initialize_joystick():
    """
    Initializes the joystick and ensures hardware is connected.
    Returns the joystick object if successful.
    """
    # Initialize Pygame and the joystick module
    pygame.init()
    pygame.joystick.init()

    # Check for connected joysticks
    joystick_count = pygame.joystick.get_count()
    if joystick_count == 0:
        print("Error: No joystick detected. Please connect a joystick and restart.")
        pygame.quit()
        sys.exit()

    # Initialize the first joystick
    joystick = pygame.joystick.Joystick(0)
    joystick.init()

    print(f"Joystick detected: {joystick.get_name()}")
    print(f"Number of axes: {joystick.get_numaxes()}")
    print(f"Number of buttons: {joystick.get_numbuttons()}")
    print(f"Number of hats (D-pad): {joystick.get_numhats()}")

    return joystick

def read_joystick_data(joystick):
    """
    Reads data from the joystick and prints it to the console.
    """
    try:
        print("\nPolling joystick data. Press Ctrl+C to exit.")
        while True:
            # Process Pygame events
            for event in pygame.event.get():
                if event.type == pygame.JOYAXISMOTION:
                    axis_value = joystick.get_axis(event.axis)
                    print(f"Axis {event.axis} moved to {axis_value:.2f}")
                elif event.type == pygame.JOYBUTTONDOWN:
                    print(f"Button {event.button} pressed")
                elif event.type == pygame.JOYBUTTONUP:
                    print(f"Button {event.button} released")
                elif event.type == pygame.JOYHATMOTION:
                    print(f"Hat {event.hat} moved to {joystick.get_hat(event.hat)}")
            time.sleep(0.01)  # Reduce CPU usage
    except KeyboardInterrupt:
        print("\nExiting...")

def main():
    try:
        joystick = initialize_joystick()
        read_joystick_data(joystick)
    finally:
        pygame.quit()
        print("Pygame quit. Cleanup complete.")

if __name__ == "__main__":
    main()