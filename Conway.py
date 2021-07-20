
#Conways Game Of Life
#Author: Tyler J. Conley
import numpy as np
import matplotlib.pyplot as plt
#size of grid
gscale = 1000
#create blank grid array
grid = [[0 for c in range(gscale)] for r in range(gscale)]

#counter variables
i = 0
j = 0

#create initial glider shape somewhere on grid
grid[12][12] == 1
grid[12][13] == 1
grid[12][11] == 1
grid[11][12] == 1


#any corner position it needs to check 3 neighbors
#any edge position except corners needs to check 5 neighbors
#all middle positions need to check 8 neighbors
#to check surrounding neighbors and switch block on or off
for i in range((gscale-1)):
    for j in range((gscale-1)):
      #CORNER POSITIONS
      if id(grid[i][j]) == id(grid[0][0]) or id(grid[i][j]) == id(grid[29][29]) or id(grid[i][j]) == id(grid[0][29]) or id(grid[i][j]) == id(grid[29][0]):
          #for the (0,0) position
          if id(grid[i][j]) == id(grid[0][0]):
              if grid[i][j] == 1:
                  if grid[0][1] + grid[1][0] + grid[1][1] < 3:
                      grid[i][j] = 0
              elif grid[i][j] == 0:
                  if grid[0][1] + grid[1][0] + grid[1][1] == 3:
                      grid[i][j] = 1
          #for the (29, 29) position
          elif id(grid[i][j]) == id(grid[29][29]):
              if grid[i][j] == 1:
                  if grid[28][29] + grid[29][28] + grid[28][28] < 3:
                      grid[i][j] = 0
              elif grid[i][j] == 0:
                  if grid[28][29] + grid[29][28] + grid[28][28] == 3:
                      grid[i][j] = 1
          #for the (0,29) position
          elif id(grid[i][j]) == id(grid[0][29]):
              if grid[i][j] == 1:
                  if grid[0][28] + grid[1][29] + grid[1][28] < 3:
                      grid[i][j] = 0
              elif grid[i][j] == 0:
                  if grid[i][j] == 0:
                      if grid[28][0] + grid[29][1] + grid[28][1] == 3:
                          grid[i][j] = 1

      #EDGE POSITIONS
      elif id(grid[i][j]) == id(grid[i][0]):
          if grid[i][j] == 0:
              if grid[i+1][j] + grid[i-1][j] + grid[i+1][j+1] + grid[i-1][j+1] + grid[i][j+1] >= 3:
                  grid[i][j] = 1
      elif id(grid[i][j]) == id(grid[0][j]):
          if grid[i][j] == 1:
              if grid[i][j+1] + grid[i][j-1] + grid[i+1][j+1] + grid[i+1][j-1] + grid[i+1][j] < 3:
                  grid[i][j] = 0
      #MIDDLE POSITIONS
      else:
          if grid[i][j] == 1:
              if grid[i+1][j] + grid[i][j+1] + grid[i+1][j+1] + grid[i-1][j-1] + grid[i-1][j] + grid[i][j-1] + grid[i+2][j+1] + grid[i+1][j+2] <= 3:
                  grid[i][j] = 0
          if grid[i][j] == 0:
              if grid[i+1][j] + grid[i][j+1] + grid[i+1][j+1] + grid[i-1][j-1] + grid[i-1][j] + grid[i][j-1] + grid[i+2][j+1] + grid[i+1][j+2] > 3:
                  grid[i][j] = 1
print(grid)
print(grid[12][12])
print(grid[12][13])
print(grid[12][11])
print(grid[11][12])
