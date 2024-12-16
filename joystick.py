import hid

# Replace these values with your device's VID and PID
VID = 0x046D  # Logitech Vendor ID
PID = 0xC215  # Extreme 3D Pro Product ID (replace if needed)

def list_hid_devices():
    """
    Lists all connected HID devices.
    """
    print("Listing all HID devices:")
    for device in hid.enumerate():
        print(f"VID: {hex(device['vendor_id'])}, PID: {hex(device['product_id'])}, Product: {device['product_string']}")

def read_joystick_data():
    """
    Reads raw input data from the Logitech Extreme 3D Pro joystick.
    """
    print(f"\nConnecting to device: VID={hex(VID)}, PID={hex(PID)}")
    try:
        # Open the HID device
        joystick = hid.device()
        joystick.open(VID, PID)
        print(f"Connected to {joystick.get_product_string()}")

        print("Listening for joystick input... Move the stick or press buttons. (Ctrl+C to exit)\n")
        while True:
            data = joystick.read(64)  # Read 64-byte HID input report
            if data:
                print(f"Raw Data: {data}")
    except KeyboardInterrupt:
        print("\nExiting...")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        joystick.close()
        print("Joystick connection closed.")

if __name__ == "__main__":
    list_hid_devices()
    read_joystick_data()
