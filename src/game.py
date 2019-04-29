"""
Just a basic 50/50 coin flip game to learn a bit about python tkinter GUI
"""


import tkinter as tk
import random
from tkinter import *


def coin_flipper():
    global scoreCount
    global flipCount
    flipCount += 1
    flipCountDisplay.config(text="Flips: "+str(flipCount))
    x = random.uniform(0, 1)
    if x >= 0.5:
        scoreCount += 1
        text.config(text="You Win")
        score.config(text="Score: "+str(scoreCount))
    else:
        text.config(text="You Lose")
    print(x)


flipCount = 0
scoreCount = 0
window = Tk()
window.title("Coin Flip")
window.geometry("250x250")


back = tk.Frame(master=window, bg='white')
back.pack(fill=tk.BOTH, expand=1)


text = tk.Message(master=back, width=400, text="Hello Welcome to the Coin Flipper")
text.pack(pady=20)


score = tk.Message(master=back, width=100, text="Score: "+str(scoreCount))
score.pack(side=BOTTOM, pady=20)


flipCountDisplay = tk.Message(master=back, width=100, text="Flips: "+str(flipCount))
flipCountDisplay.pack(side=BOTTOM, pady=20)


flip = tk.Button(master=back, text="Flip", command=coin_flipper)
flip.pack(side=BOTTOM, pady=20)


window.mainloop()
