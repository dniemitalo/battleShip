class Matrix():
  grid =   ['0','0','0','0','0',
            '0','0','0','0','0',
            '0','0','0','0','0',
            '0','0','0','0','0',
            '0','0','0','0','0',
            'N','N','N','N','N',
            '0','0','0','0','0',
            '0','0','0','0','0',
            '0','0','0','0','0',
            '0','0','0','0','0',
            '0','0','0','0','0']

playerOne = Matrix()
playerTwo = Matrix()

def lookUpTwo(iVal, bVal):
  if iVal == 0 and bVal == 0:
    return 0 
  else:
    return (iVal*5)  + bVal

def printMatrix(player):
  for i in range(11):
    print [player.grid[lookUpTwo(i,b)] for b in range(5)]

def updateMatrix(player, xVal, yVal):
  lookUpTwo  
  
    
printMatrix(playerOne)
printMatrix(playerTwo)
