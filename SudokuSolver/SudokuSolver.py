import numpy as np
import time

class SingleCell:
    def __init__(self, x, y, houseNumber, row, col, house, missingInRow, missingInColumn, missingInHouse):
        self.me = 0
        self.x = x
        self.y = y
        self.houseNumber = houseNumber
        self.row = row
        self.column = col
        self.house = house
        self.missingInRow = missingInRow
        self.missingInColumn = missingInColumn
        self.missingInHouse = missingInHouse
        self.cleanLists()

    def simpleCheck(self):
        if len(self.missingInColumn) == 1:
            self.me = self.missingInColumn[0]
        elif len(self.missingInHouse) == 1:
            self.me = self.missingInHouse[0]
        elif len(self.missingInRow) == 1:
            self.me = self.missingInRow[0]
        else:
            return False
        return True

    def cleanLists(self):
        for removeValue in self.column:
            try:
                self.missingInRow.remove(removeValue)
            except ValueError:
                pass
            try:
                self.missingInHouse.remove(removeValue)
            except ValueError:
                pass
        for removeValue in self.row:
            try:
                self.missingInColumn.remove(removeValue)
            except ValueError:
                pass
            try:
                self.missingInHouse.remove(removeValue)
            except ValueError:
                pass
        for removeValue in self.house:
            try:
                self.missingInRow.remove(removeValue)
            except ValueError:
                pass    
            try:
                self.missingInColumn.remove(removeValue)
            except ValueError:
                pass
class SudokuGrid:
    def __init__(self, grid):
        self.grid = grid
        self.cells = []
        for i in range (0,9):
            for j in range (0,9):
                if self.grid[i, j] == 0:
                    missingInRow = [1,2,3,4,5,6,7,8,9]
                    row = self.grid[i, :]
                    for removeValue in row:
                        try:
                            missingInRow.remove(removeValue)
                        except ValueError:
                            pass
                    if len(missingInRow) == 1:
                        self.grid[i,j] = missingInRow[0]
                    else:
                        missingInColumn = [1,2,3,4,5,6,7,8,9]
                        column = self.grid[:, j]
                        for removeValue in column:
                            try:
                                missingInColumn.remove(removeValue)
                            except ValueError:
                                    pass
                        if len(missingInColumn) == 1:
                            self.grid[i,j] = missingInColumn[0]
                        else:
                            houseNumber = [0, 0]
                            if i > 2:
                                if i > 5:
                                    houseNumber[0]=2
                                else:
                                    houseNumber[0]=1
                            if j > 2:
                                if j > 5:
                                    houseNumber[1]=2
                                else:
                                    houseNumber[1]=1
                            house = self.grid[0+houseNumber[0]*3:2+houseNumber[0]*3, 0+houseNumber[1]*3:2+houseNumber[1]*3]
                            missingInHouse = [1,2,3,4,5,6,7,8,9]
                            for i2 in range (0+houseNumber[0]*3,3+houseNumber[0]*3):
                                for j2 in range (0+houseNumber[1]*3,3+houseNumber[1]*3):
                                    try:
                                        missingInHouse.remove(self.grid[i2, j2])
                                    except ValueError:
                                        pass
                            if len(missingInHouse) == 1:
                                self.grid[i,j] = missingInHouse[0]
                            else:
                                self.cells.append(SingleCell(i, j, houseNumber, row, column, house, missingInRow, missingInColumn, missingInHouse))
    def trySolve(self):
        for loops in range(0,10):
            breakLoop = False
            for i in range(0, 20):
                if breakLoop:
                    print("simple", i+1)
                    break
                breakLoop = True
                for obj in self.cells:
                    obj.cleanLists()
                    if obj.simpleCheck():
                        breakLoop = False
                        self.grid[obj.x, obj.y] = obj.me
                        self.cells.remove(obj)

            breakLoop = False
            for i in range(0, 20):
                if breakLoop:
                    print("missing", i+1)
                    break
                breakLoop = True
                for obj in self.cells:
                    obj.cleanLists()
                    if obj.simpleCheck():
                        self.grid[obj.x, obj.y] = obj.me
                        self.cells.remove(obj)
                        continue
                    potencialNumbers = list(obj.missingInHouse)
                    for obj2 in self.cells:
                        if obj2.houseNumber == obj.houseNumber and obj2!=obj:
                            for removeValue in obj2.missingInHouse:
                                try:
                                    potencialNumbers.remove(removeValue)
                                except ValueError:
                                    if len(potencialNumbers) == 0:
                                        break
                                    pass
                            if len(potencialNumbers) == 0:
                                        break
                    if len(potencialNumbers)==1:
                        breakLoop = False
                        self.grid[obj.x, obj.y] = obj.me = potencialNumbers[0]
                        self.cells.remove(obj)
            
            nextLoop = False
            for i in range (0,9):
                for j in range (0,9):
                    if self.grid[i,j] == 0:
                        nextLoop=True;
                        break
                if nextLoop:
                    break
            if nextLoop:
                    break                                
            """
            breakLoop = False
            for i in range(0, 20):
                if breakLoop:
                    print("missing", i)
                    break
                breakLoop = True
                for obj in self.cells:
                    obj.cleanLists()
                    if obj.simpleCheck():
                        self.grid[obj.x, obj.y] = obj.me
                        self.cells.remove(obj)
                        continue
                    houseNum = obj.houseNumber
                    potencialHouseNumbers = list(obj.missingInHouse)
                    for obj2 in self.cells:
                        if houseNum == obj2.houseNumber:
                            if obj2.x != obj.x and obj2.y != obj.y:
                                obj2.cleanLists()
                                for removeValue in obj2.missingInHouse:
                                    try:
                                        potencialHouseNumbers.remove(removeValue)
                                    except ValueError:
                                        if len(potencialHouseNumbers) == 0:
                                            break
                                        pass
                        if len(potencialHouseNumbers) == 0:
                            break
                    if len(potencialHouseNumbers) == 0:
                            continue
                    if len(potencialHouseNumbers) == 1:
                        breakLoop = False
                        self.grid[obj.x, obj.y] = obj.me = potencialHouseNumbers[0]
                        self.cells.remove(obj)
            """

        print("loops", loops+1)
        for i in range (0,9):
            test = set(self.grid[i, :])
            if len(test) != 9:
                return False
        for i in range (0,9):
            test = set(self.grid[:, i])
            if len(test) != 9:
                return False
        return True;

testData3 = np.array([[1,4,0,2,0,8,5,0,7],[9,0,8,0,0,0,0,0,0],[0,5,6,1,0,3,9,2,8],[3,6,1,0,5,4,2,8,0],[8,7,0,0,2,0,0,5,0],[5,9,2,0,0,0,0,0,0],[0,3,0,9,0,2,7,0,4],[2,8,0,0,3,1,6,9,0],[4,1,0,0,6,7,8,0,2]])
"""testData = [[1,4,3,2,9,8,5,6,7],[9,2,8,6,7,5,3,4,1],[7,5,6,1,4,3,9,2,8],[3,6,1,7,5,4,2,8,9],[8,7,4,3,2,9,1,5,6],[5,9,2,8,1,6,4,7,3],[6,3,5,9,8,2,7,1,4],[2,8,7,4,3,1,6,9,5],[4,1,9,5,6,7,8,3,2]]"""

testData2 = np.array([[0,0,0,5,0,0,0,0,0],[7,5,4,3,6,1,2,0,0],[3,0,0,0,0,0,0,7,6],[8,0,9,4,1,0,6,0,3],[6,3,0,7,0,9,1,0,0],[0,4,0,0,8,0,9,5,0],[5,1,0,9,0,8,0,0,2],[0,0,0,0,0,0,0,0,0],[2,9,0,0,4,7,8,6,0]])

testData = np.array([[7,0,0,8,4,0,9,0,0],[0,0,1,0,0,0,0,0,0],[9,3,0,0,0,0,8,6,4],[0,0,0,0,7,0,3,0,8],[0,0,6,9,1,0,4,7,0],[0,8,0,0,3,0,0,0,6],[0,5,0,1,0,0,0,0,9],[4,0,9,0,0,3,0,0,1],[0,0,0,0,0,6,0,0,7]])
"""testData = np.array([[7,0,0,8,4,0,9,0,0],[0,0,1,0,0,0,0,0,0],[9,3,0,0,0,0,8,6,4],[0,0,0,0,7,0,3,0,8],[0,0,6,9,1,0,4,7,0],[0,8,0,0,3,0,0,0,6],[0,5,0,1,0,0,0,0,9],[4,0,9,0,0,3,0,0,0],[0,0,0,0,0,6,0,0,7]])"""


"""for i in range (0,9):
    print(len(testData[i]))"""
for i in range (0,9):
    for j in range (0,9):
        print(testData[i][j], end="")
        if (j+1) % 3 == 0:
            print("|", end="")
    if (i+1) % 3 == 0:
            print()
            print("--"*6, end="")
    print ("")

obj = SudokuGrid(testData)
start_time = time.time()
print(obj.trySolve())
print(time.time() - start_time, "\n")

for i in range (0,9):
    for j in range (0,9):
        print(testData[i][j], end="")
        if (j+1) % 3 == 0:
            print("|", end="")
    if (i+1) % 3 == 0:
            print()
            print("--"*6, end="")
    print ("")
