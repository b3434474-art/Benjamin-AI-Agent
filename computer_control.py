import pyautogui


def move_mouse(x, y):
    pyautogui.moveTo(x, y)


def click():
    confirm = input("Click? (yes/no): ")

    if confirm.lower() == "yes":
        pyautogui.click()
        print("Clicked!")
    else:
        print("Cancelled")


def type_text(text):
    confirm = input(f"Type '{text}'? (yes/no): ")

    if confirm.lower() == "yes":
        pyautogui.write(text)
        print("Typed!")
    else:
        print("Cancelled")
