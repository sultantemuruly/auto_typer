import pyautogui
import time


def auto_writer(text, delay=0.1):
    print("You have 5 seconds to focus on the input field...")
    time.sleep(5)
    pyautogui.write(text, interval=delay)


if __name__ == "__main__":
    my_text = "Some random text to type....."
    auto_writer(my_text, delay=1)
