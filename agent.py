from screenshot import take_screenshot
from computer_control import move_mouse, click, type_text


print("🤖 Benjamin AI Agent Started")

while True:

    command = input("\nCommand: ")

    if command == "screenshot":
        take_screenshot()

    elif command.startswith("move"):
        parts = command.split()

        x = int(parts[1])
        y = int(parts[2])

        move_mouse(x, y)

    elif command == "click":
        click()

    elif command.startswith("type "):
        text = command[5:]
        type_text(text)

    elif command == "exit":
        print("Goodbye!")
        break

    else:
        print("Unknown command")
