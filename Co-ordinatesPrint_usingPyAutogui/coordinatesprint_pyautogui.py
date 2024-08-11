#correctly capturing the 
import pyautogui
import time

# Function to print the coordinates of the form field
def print_coordinates(field_name):
    # Display a message indicating which field to capture
    print(f"Please move your mouse cursor to the {field_name} field and press Enter.")
    input("Press Enter to continue...")
    # Get the position of the form field
    x, y = pyautogui.position()
    print(f"Coordinates of {field_name}: ({x}, {y})")
    return x, y

# Function to hover the mouse cursor over the coordinates for 10 seconds
def hover_over_coordinates(x, y):
    # Move the mouse cursor to the specified coordinates
    time.sleep(5)
    pyautogui.moveTo(x, y, duration=1)
    # Pause for 10 seconds
    time.sleep(5)

# Function to capture form field coordinates and hover over them
def capture_and_hover_over_coordinates(field_name):
    # Print coordinates of the form field
    x, y = print_coordinates(field_name)
    if x is not None and y is not None:
        # Hover mouse cursor over the coordinates for 10 seconds
        hover_over_coordinates(x, y)

# Capture form field coordinates and hover over them
capture_and_hover_over_coordinates("username")
capture_and_hover_over_coordinates("password")
capture_and_hover_over_coordinates("OK button")
