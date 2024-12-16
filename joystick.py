import pyvjoy

def test_joystick():
    try:
        j = pyvjoy.VJoyDevice(1)  # Reference vJoy Device 1
        print("vJoy device initialized. Ready to read joystick input.")

        while True:
            # Example: Map the joystick's X-axis and Y-axis to vJoy axes
            j.set_axis(pyvjoy.HID_USAGE_X, 0x4000)  # Set X-Axis halfway
            j.set_axis(pyvjoy.HID_USAGE_Y, 0x4000)  # Set Y-Axis halfway
            
            # Example: Simulate a button press
            j.set_button(1, 1)  # Press button 1
            print("Simulating joystick input. Press Ctrl+C to stop.")
            
    except KeyboardInterrupt:
        print("Exiting vJoy test.")

if __name__ == "__main__":
    test_joystick()
