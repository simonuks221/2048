import tkinter as tk
import GameManager as gm

t = tk.Tk()
t.geometry("500x500")

gameFrame = tk.Frame(t)
gameFrame.pack()

gameManager = gm.GameManager()
gameManager.StartGame(gameFrame)

t.mainloop()
