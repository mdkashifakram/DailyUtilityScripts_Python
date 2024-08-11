from screeninfo import get_monitors

def get_screen_size():
    monitors = get_monitors()
    for monitor in monitors:
        print(f"Monitor: {monitor.name}")
        print(f"Width: {monitor.width} pixels")
        print(f"Height: {monitor.height} pixels")
        print(f"Width: {monitor.width_mm} mm")
        print(f"Height: {monitor.height_mm} mm")
        print(f"Monitor Size: {monitor.width_mm / 25.4:.2f} inches x {monitor.height_mm / 25.4:.2f} inches")
        print("")

if __name__ == "__main__":
    get_screen_size()
