import numpy as np
import tkinter as tk
import random

class GameManager:
    def __init__(self):
        self.tiles = np.zeros((4, 4), dtype = int)
        self.buttons = np.zeros((4, 4), dtype = object)

    #Generate a random tile with 2
    def GenerateRandomTile(self):
        while(True):
            x = np.random.randint(0, 4)
            y = np.random.randint(0, 4)
            if self.tiles[y, x] == 0:
                self.tiles[y, x] = 2
                break

    #Generate starting tile matrix
    def GenerateTiles(self):
        #Clear tile matrix
        for y in range(4):
            for x in range(4):
                self.tiles[y, x] = 0
        
        #Generate 2 starting tiles
        for i in range(2):
            self.GenerateRandomTile()
            
    #Updates button visuals to mach tile values
    def UpdateButtons(self):
        for y in range(4):
            for x in range(4):
                self.buttons[y, x].configure(text = self.tiles[y, x])
                
    #Generates game button grid
    def GenerateGrid(self, gridFrame):
        for y in range(4):
            for x in range(4):
                newButton = tk.Button(gridFrame)
                newButton.grid(row = y, column = x)
                self.buttons[y, x] = newButton
        self.UpdateButtons()

    def ButtonPressed(self, dirX, dirY):
        return

    def StartGame(self, gridFrame):
        self.GenerateTiles()
        self.GenerateGrid(gridFrame)

