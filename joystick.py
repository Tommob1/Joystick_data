import pywinusb.hid as hid

def find_joystick():
    """
    Finds the first connected joystick and returns its HID device.
    """
    all_devices = hid.find_all_hid_devices()
    if not all_devices:
        print("No HID devices found.")
        return None

    for device in all_devices:
        if "joystick" in device.product_name.lower():
            print(f"Joystick found: {device.product_name}")
            print(f"Vendor ID: {device.vendor_id}, Product ID: {device.product_id}")
            return device

    print("No joystick device found.")
    return None

def read_joystick_data(device):
    """
    Reads and prints input data from the joystick.
    """
    try:
        device.open()

        def raw_data_handler(data):
            print(f"Raw Data: {data}")

        device.set_raw_data_handler(raw_data_handler)

        print("Reading joystick data. Press Ctrl+C to exit.")
        while True:
            pass  # Keep the script running to receive data
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        device.close()

def main():
    device = find_joystick()
    if device:
        read_joystick_data(device)

if __name__ == "__main__":
    main()