import pyautogui
import time
import random


def auto_typer(file_path, min_delay=0.1, max_delay=0.75):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    print("You have 5 seconds to focus on the input field...")
    time.sleep(5)

    for char in text:
        if char == "\n":  # Handle newlines manually
            pyautogui.keyDown("shift")
            pyautogui.press("enter")
            pyautogui.keyUp("shift")
        else:
            pyautogui.write(char)
        time.sleep(random.uniform(min_delay, max_delay))


if __name__ == "__main__":
    auto_typer("text_to_type.md", min_delay=0.1, max_delay=0.75)
