"""
Just a basic 50/50 coin flip game to learn a bit about python tkinter GUI
"""


import tkinter as tk
import random
from tkinter import *


class Counter:

    __count: int

    def __init__(self):
        """
        initialize private count variable to 0
        """
        self.__count = 0

    def count_up(self):
        """
        add one to count
        :return: None
        """
        self.__count += 1

    def count_out(self):
        """
        returns count as a int
        :return: count
        """
        return self.__count


def coin_flipper():
    """
    increment flip counter
    update GUI flip counter
    generate random number from 0 to 1
    if number is >= 0.5
    increment score counter
    update info text to win
    else
    update info text to lose
    :return: None
    """
    flipCount.count_up()
    flipCountDisplay.config(text="Flips: "+str(flipCount.count_out()))
    x = random.uniform(0, 1)
    if x >= 0.5:
        scoreCount.count_up()
        text.config(text="You Win")
        score.config(text="Score: "+str(scoreCount.count_out()))
    else:
        text.config(text="You Lose")

    if flipCount.count_out() >= 10:
        flip.pack_forget()
        text.config(text="Game over thank you for playing")


flipCount = Counter()
scoreCount = Counter()
window = Tk()
window.title("Coin Flip")
window.geometry("250x250")


back = tk.Frame(master=window, bg='white')
back.pack(fill=tk.BOTH, expand=1)


text = tk.Message(master=back, width=400, text="Hello Welcome to the Coin Flipper")
text.pack(pady=20)


score = tk.Message(master=back, width=100, text="Score: "+str(scoreCount.count_out()))
score.pack(side=BOTTOM, pady=20)


flipCountDisplay = tk.Message(master=back, width=100, text="Flips: "+str(flipCount.count_out()))
flipCountDisplay.pack(side=BOTTOM, pady=20)


flip = tk.Button(master=back, text="Flip", command=coin_flipper)
flip.pack(side=BOTTOM, pady=20)


window.mainloop()
