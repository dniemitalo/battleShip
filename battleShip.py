# Battleship: The Terminal
# Jack Tupper and Matt Behnke

import replit # Importing replit to clear the screen
class Matrix(): # defining class matrix to set up players one and two
  def __init__(self):  #init for Matrix class 
    self.grid =['00','1','2','3','4','5',   # starting grid
                '01','0','0','0','0','0',   # for the players
                '02','0','0','0','0','0',
                '03','0','0','0','0','0',
                '04','0','0','0','0','0',
                '05','0','0','0','0','0',
                '06','N','N','N','N','N',
                '07','0','0','0','0','0',
                '08','0','0','0','0','0',
                '09','0','0','0','0','0',
                '10','0','0','0','0','0',
                '11','0','0','0','0','0']
    self.score = 0    # initializing score 
    self.distance = 0 # initializing distance

playerOne = Matrix() # Creating player one from the matrix
playerTwo = Matrix() # Creating player two from the matrix

def lookUp(iVal, bVal):       # Function that takes coordinates and
  if iVal == 0 and bVal == 0: # places it on the array
    return 0 
  else:
    return (iVal*6)  + bVal

def printMatrix(player): # Prints each players grid when called
  for i in range(12):
    print [player.grid[lookUp(i,b)] for b in range(6)]

def updateMatrix(value, xVal, yVal, player): # used to change values on
  place = lookUp(yVal,xVal)                  # on a players grid
  player.grid[place] = value
  
def checkMarix(x, y, player, value): # Used to check if value is right
  if player.grid[lookUp(y, x)] == str(value):
    return True  # returns true if the value is the same 
  else:
    return False # returns False when the values do not match

def distance(player, x1,y1,x2,y2): # used to caculate distance between
  player.distance = 0              # two points 
  isHorizontal = False # defining isHorizontal
  isVertical = False   # defining isVertical
  if x1 == x2: # check if the points are vertical 
    isHorizontal = False
    isVertical = True
    if y2 > y1: # check if the points are backwards
      isBackwards = False
      distance = y2 - y1 + 1
    else:       # not backwards
      isBackwards = True
      distance = y1 - y2 + 1
  elif y1 == y2: # check if points are horizontal
    isVertical = False
    isHorizontal = True
    if x2 > x1: # check if points are backwards
      isBackwards = False
      distance = x2 - x1 + 1
    else:       # not backwards
      isBackwards = True
      distance = x1 - x2 + 1
  if x1 != x2 and y1 != y2: # if points are not vertical or horizontal
    print 'provid valid coordinate points'
  else:
    player.distance = distance
  

def placeShip(player, x1, y1, x2, y2): # placing point based on coordinates
  isHorizontal = False # defining isHorizontal
  isVertical = False   # defining isVertical
  if x1 == x2 and y1 == y2: # check if points on it self
    print 'Ship can not be placed on it self'
  elif x1 == x2: # check  if vertical
    isHorizontal = False
    isVertical = True
    if y2 > y1: # check if backwards
      isBackwards = False
      distance = y2 - y1 + 1
    else:
      isBackwards = True
      distance = y1 - y2 + 1
  elif y1 == y2: # check if horizontal
    isVertical = False
    isHorizontal = True
    if x2 > x1: # check if backwards
      isBackwards = False
      distance = x2 - x1 + 1
    else:
      isBackwards = True
      distance = x1 - x2 + 1
  else: # ships can not be diagonal
    print 'Ship cannot be placed diagonally'
  for i in range(abs(distance)): # finding the amount of points to print 
    if isBackwards: # if backwards the i is negative 
      i = -i
    if isHorizontal: # if horizontal then x + i
      updateMatrix('1',(x1+i),y1, player)
    elif isVertical: # if vertical then y +  i
      updateMatrix('1',x1,(y1+i), player)

def playerName(player): # geting the name from player and seting name 
  if player == playerOne:  # if playerOne 
    x = 'player One'
  elif player == playerTwo: # if playerTwo
    x = 'player Two'
  player.name = raw_input('Who will be ' + x+'?')
  return player.name

def playerShip(player): # placeing points from coordinates
  print player.name + ' you are up'
  print 'place your ship by providing coordinates'
  for i  in range(3): # for each ship
    if player == playerOne:
      printMatrix(playerOne)
    elif player == playerTwo:
      printMatrix(playerTwo)
    if i == 0: # on ship one 
      print 'Place ship #1 (length of 2)'
      while player.distance != 2:
        validate(player, 2)
    elif i == 1: # on ship two
      print 'Place ship #2 (length of 3)'
      while player.distance != 3:
        validate(player, 3)
    elif i == 2: # on ship three
      print 'Place ship #3 (length of 2)'
      while player.distance != 2:
        validate(player, 2)
    
def validate(player, value): # checking if inputs are valid
  x1 = raw_input('x1 ')  # get value for x1
  while type(x1) == str: # while the type is a string  
    try:                 # try to covert to a int 
      x1 = int(x1)
    except ValueError:   # catch errer ValueError 
      print 'Use a valid coordinate'
      x1 = raw_input('x1 ')
  while int(x1)>5 or int(x1)<1: # wont allow input not to be in range 
    print 'not a valid spot'
    x1 = int(raw_input('x1 '))
  y1 = raw_input('y1 ')  # get value for y1
  while type(y1) == str: # while the type is a string 
    try:                 # try to covert to a int 
      y1 = int(y1)
    except ValueError:   # catch errer ValueError 
      print 'Use a valid coordinate'
      y1 = raw_input('y1 ')
  while int(y1)> 11 or int(y1)<7: # wont allow input not to be in range 
    print 'not a valid spot'
    y1 = int(raw_input('y1 '))
  x2 = raw_input('x2 ')  # get value for x2
  while type(x2) == str: # while the type is a string 
    try:                 # try to covert to a int 
      x2 = int(x2)
    except ValueError:   # catch errer ValueError 
      print 'Use a valid coordinate'
      x2 = raw_input('x2 ')
  while int(x2)> 5 or int(x2)<1: # wont allow input not to be in range 
    print 'not a valid spot'
    x2 = int(raw_input('x2 '))
  y2 = raw_input('y2 ')  # get value for y2
  while type(y2) == str: # while the type is a string
    try:                 # try to covert to a int 
      y2 = int(y2)
    except ValueError:   # catch errer ValueError 
      print 'Use a valid coordinate'
      y2 = raw_input('y2 ')
  while int(y2)> 11 or int(y2)<7: # wont allow input not to be in range 
    print 'not a valid spot'
    y2 = int(raw_input('y2 '))
  distance(player,x1,y1,x2,y2)
  if player.distance == value: # check if the distance put in is corect length
    placeShip(player, abs(x1), abs(y1), abs(x2), abs(y2)) # places the ship
  else:
    print 'Put in a distance of ', value

def won(player): # called when a player won 
  print '~~~~~~~~~~~~~~~~~~~~~~'
  print player.name, 'Has Won'
  print '~~~~~~~~~~~~~~~~~~~~~~'
  main() # retart the program 

def shoot(player): # func for the player to shoot
  print 'Where would', player.name  ,'like to shoot'
  x = raw_input('X ')
  while type(x) == str: # while type == string 
    try:            # tries to convert x to an integer
      x = int(x)
      while int(x)>5 or int(x)<1: # forces x value to be in a range
        print 'not valid spot'
        x = raw_input('X ')
    except ValueError:     # Catches if user put in a non integer
      print 'not valid spot'
      x = raw_input('X ')
      
  y = raw_input('Y ')
  while type(y) == str:  # while type == string
    try:            # tries to convert y to an integer
      y = int(y)
      while int(y)>5 or int(y)<1: # forces y value to be in a range
        print 'not valid spot'
        y = raw_input('Y ')
    except ValueError:     # Catches if user put in a non integer
      print 'not valid spot'
      y = raw_input('Y ')   
    
  while player.grid[lookUp(y,x)] != '0': # Checks if coordinate has been shot
    print 'you have already shot there' 
    x = raw_input('X ')
    while type(x) == str:  # while type == string
      try:            # tries to convert x to an integer
        x = int(x)
        while int(x)>5 or int(x)<1: # forces x value to be in a range
          print 'not valid spot'
          x = raw_input('X ')
      except ValueError:    # Catches if user put in a non integer
        print 'not valid spot'
        x = raw_input('X ')
    y = raw_input('Y ')
    while type(y) == str:  # while type == string
      try:            # tries to convert y to an integer
        y = int(y)
        while int(y)>5 or int(y)<1: # forces y value to be in a range
          print 'not valid spot'
          y = raw_input('Y ')
      except ValueError:    # Catches if user put in a non integer
        print 'not valid spot'
        y = raw_input('Y ') 
    
  y = int(y)+6
  if player == playerOne:   # Checks if player is player one
    if checkMarix(x,y,playerTwo, '1'): # Checking for enemy ships
      print 'Hit'
      updateMatrix('H',x,(y - 6),playerOne)
      printMatrix(player)
      playerOne.score = playerOne.score + 1
      if playerOne.score < 7: # Checks if player has not hit all ships
        shoot(playerOne)
      else:   # player wins
        won(playerOne)
    else:     # shot misses
      print 'Miss'
      updateMatrix('X',x,(y - 6),playerOne)
      printMatrix(player)
      
  elif player == playerTwo:   # Switches to player two
    if checkMarix(x,y,playerOne, '1'): # Checking for enemy ships
      print 'Hit'
      updateMatrix('H',x, (y - 6),playerTwo)
      printMatrix(player)
      playerTwo.score = playerTwo.score + 1
      if playerTwo.score < 7: # Checks if player has not hit all ships
        shoot(playerTwo)
      else:  # player wins
        won(playerTwo)
    else:    # shot misses
      print 'Miss'
      updateMatrix('X',x,(y - 6),playerTwo)
      printMatrix(player)

def main():      # Defines the starting sequence
  playerOne.distance = 0
  playerTwo.distance = 0
  # Start text
  print 'Welcome to battleship'
  print 'The aim of the game is to sink your opponent\'s ships.'
  print 'Each player gets 3 ships: 2 ships that are 2 units long and 1 ship that is 3 units long'
  playerName(playerOne)   # Gets player one's name
  replit.clear()
  playerName(playerTwo)   # Gets player two's name
  replit.clear()
  print 'The players are', playerOne.name, 'and' ,playerTwo.name
  playerShip(playerOne)   # calls place ship function for player one
  replit.clear()
  playerShip(playerTwo)   # calls place ship function for player two
  replit.clear()
  while True:
    printMatrix(playerOne)  # prints player one's grid
    shoot(playerOne)        # calls player one's turn to shoot
    replit.clear()
    printMatrix(playerTwo)  # prints player two's grid
    shoot(playerTwo)        # calls player two's turn to shoot
    replit.clear()
    
main()
