import pyautogui
import time


def auto_typer(file_path, delay=0.5):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    print("You have 5 seconds to focus on the input field...")
    time.sleep(5)

    pyautogui.write(text, interval=delay)
    pyautogui.press("enter")


if __name__ == "__main__":
    auto_typer("text_to_type.md", delay=0.5)
