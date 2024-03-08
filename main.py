import pyautogui
import pathlib
import time


def main():
    file = pathlib.Path("words.txt")
    worlds = file.read_text()

    time.sleep(10)
    pyautogui.write(worlds, interval=0.15)


main()
