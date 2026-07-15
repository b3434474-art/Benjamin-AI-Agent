import pyautogui


def take_screenshot():
    image = pyautogui.screenshot()
    image.save("screen.png")
    print("Screenshot saved as screen.png")


if __name__ == "__main__":
    take_screenshot()
