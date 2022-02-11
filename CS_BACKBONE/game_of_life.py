import numpy as np
import os
import time

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

class Conway:
    def __init__(self, m,n, seed_tuples):
        self.height = m
        self.width = n
        self.board = np.full((m, n), False)
        for x,y in seed_tuples: 
            self.board[x,y] = True


    def __str__(self):
        s = ""
        for i in range(self.height):
            for j in range(self.width):
                s += " # " if self.board[i,j] else " . "
            s += "\n"
        return s

    def check_neighbours(self, x,y):
        #there are 8 neighbours
        n = np.array([])
        n = np.append(n , (self.board[(x-1)%self.height, (y-1)%self.width], self.board[(x-1)%self.height, y], self.board[(x-1)%self.height, (y+1)%self.width]))
        n = np.append(n , (self.board[ x               , (y-1)%self.width]                                  , self.board[ x               , (y+1)%self.width]))
        n = np.append(n , (self.board[(x+1)%self.height, (y-1)%self.width], self.board[(x+1)%self.height, y], self.board[(x+1)%self.height, (y+1)%self.width]))
        return np.sum(n)
    
    def iterate(self):
        new_board = np.copy(self.board)
        for i in range(self.height):
            for j in range(self.width):
                n = self.check_neighbours(i,j)
                if self.board[i,j]:
                    new_board[i,j] = True if (n==2 or n==3) else False
                else:
                    new_board[i,j] = True if (n==3) else False

        self.board = new_board
 


if __name__=='__main__':
    game = Conway(20,21,[(1,1),(1,2),(2,2),(2,3),(5,6),(5,5),(5,7),(9,11),(10,10),(10,12),(11,11), (9,2),(10,2),(11,2),(9,3),(10,4)] )
    
    for i in range(500):
        clearConsole()
        print(game)
        game.iterate()
        time.sleep(.05)
    del game