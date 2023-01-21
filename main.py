from tkinter import *
from pyautogui import *
import time

window = Tk()
window.title("Auto Clicker")
window.geometry("500x250")

def start():
    wait = float(wait_init.get())
    number = number_init.get()
    interval = float(interval_init.get())

    while True:
        time.sleep(1)
        wait -= 1

        if wait == 0:
            break

    for i in range(int(number)):
        click(position())
        time.sleep(interval)


Label(window, text="Enter wait in seconds until clicking starts:").pack()
wait_init = Entry(window)
wait_init.pack()

Label(window, text="Enter number of clicks:").pack()
number_init = Entry(window)
number_init.pack()

Label(window, text="Enter time in seconds in between clicks:").pack()
interval_init = Entry(window)
interval_init.pack()

Button(window, text="Start", command=lambda:start()).pack()

window.mainloop()
