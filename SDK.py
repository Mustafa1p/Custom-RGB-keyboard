import ManufacturerSDK  # Hypothetical SDK import

def initialize_keyboard():
    try:
        keyboard = ManufacturerSDK.Keyboard()
        keyboard.connect()
        return keyboard
    except ManufacturerSDK.KeyboardConnectionError:
        print("Failed to connect to the keyboard.")
        return None

def change_rgb(keyboard, color):
    if keyboard:
        try:
            keyboard.set_rgb_color(color)
            print("RGB color changed successfully.")
        except ManufacturerSDK.SDKError as e:
            print(f"Failed to change color: {e}")

if __name__ == "__main__":
    keyboard = initialize_keyboard()
    change_rgb(keyboard, "#FF0000")  # Example to change color to red
