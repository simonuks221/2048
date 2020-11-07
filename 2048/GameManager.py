import numpy as np
import tkinter as tk
import random

class GameManager:
    def __init__(self):
        self.tile = np.zeros((4, 4), dtype = int)
        self.buttons = np.zeros((4, 4), dtype = object)

    #Checks if tile array is full
    def CheckTileFull(self):
        return

    #Checks if game is over
    def CheckGameOver(self):
        return

    #Generate a random tile with 2
    def GenerateRandomTile(self):
        while(True):
            x = np.random.randint(0, 4)
            y = np.random.randint(0, 4)
            if self.tile[y, x] == 0:
                self.tile[y, x] = 2
                break

    #Generate starting tile matrix
    def GenerateTiles(self):
        #Clear tile matrix
        for y in range(4):
            for x in range(4):
                self.tile[y, x] = 0
        
        #Generate 2 starting tiles
        for i in range(2):
            self.GenerateRandomTile()
            
    #Updates button visuals to mach tile values
    def UpdateButtons(self):
        for y in range(4):
            for x in range(4):
                self.buttons[y, x].configure(text = self.tile[y, x])
                
    #Generates game button grid
    def GenerateGrid(self, gridFrame):
        for y in range(4):
            for x in range(4):
                newButton = tk.Button(gridFrame)
                newButton.grid(row = y, column = x)
                self.buttons[y, x] = newButton
        self.UpdateButtons()

    #Return if x and y go out of array boundaries
    def ValidArray(self, x, y):
        return x >= 0 and y >=0 and x < 4 and y < 4

    def ButtonPressed(self, dirX, dirY):
        changed = True
        while(changed):
            changed = False
            for y in range(4):
                for x in range(4):
                    if(self.ValidArray(x + dirX, y + dirY)):
                        if(self.tile[y, x] != 0):
                            #Check if add tile numbers
                            if(self.tile[y, x] == self.tile[y + dirY, x + dirX]):
                                self.tile[y + dirY, x + dirX] = self.tile[y, x] * 2
                                self.tile[y, x] = 0
                                changed = True
                            #Empty tile, move
                            elif(self.tile[y + dirY, x + dirX] == 0):
                                self.tile[y + dirY, x + dirX] = self.tile[y, x]
                                self.tile[y, x] = 0
                                changed = True
        self.UpdateButtons()
        self.CheckGameOver()


    def StartGame(self, gridFrame):
        self.GenerateTiles()
        self.GenerateGrid(gridFrame)

    def GameOver(self):
        return