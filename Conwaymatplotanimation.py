#Conway's Game Of Life
#Author: Tyler Conley
import argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

#global animation
Fmin2 = 0
Fmin1 = 1

fig, ax = plt.subplots()
#img = ax.imshow(grid, interpolation='nearest')
time_text = ax.text(0.2, 0.95, '', transform=ax.transAxes)


# init function needed for animation to keep time somehow i think?
def init():
    global Fmin2, Fmin1
    Fmin2 = 0
    Fmin1 = 1
    time_text.set_text('')
    line.set_date([],[])
    return line, time_text


# animation function
def animate(i):
    global Fmin2, Fmin1
    Fn = Fmin1 + Fmin2
    Fmin2 = Fmin1
    Fmin1 = Fn
    time_text.set_text('i={:d}'.format(i))



        #values needed to create the grid
ON = 255
OFF = 0
vals = [ON, OFF]
#define function that returns a random grid of size scale*scale
def randgrid(scale):
    #returns a random grid of scale*scale values
    # not sure what p=[0.2, 0.8] is doing
    return np.random.choice(vals, scale*scale, p=[0.2, 0.8]).reshape(scale, scale)
#define function that adds a glider at (i, j)
def glider(i, j, grid):
    #array to hold glider shape
    glider = np.array([[0, 0, 255], [255, 0 , 255], [0, 255, 255]])
    #choose spot on grid to place the glider to start
    #sets the elements from that spot in grid to the values
    #of the elements in glider
    grid[i:i+3, j:j+3] = glider

#update frame
def updateframe(framenumber, img, grid, scale):
    #copy current grid to a holder variable
    #because this calculates line by line
    holderGrid = grid.copy()
    #loop through grids element by element
    for i in range(scale):
        for j in range(scale):
            #Compute 8-neighbor sum
            #wouldn't this array need to be 3D in order
            #to create a toridal surface?
            tot = int ((grid[i, (j-1)%scale] + grid[i, (j+1)%scale] +
                        grid[(i-1)%scale, j] + grid[(i+1)%scale, j] +
                        grid[(i-1)%scale, (j-1)%scale] + grid[(i-1)%scale, (j+1)%scale] +
                        grid[(i+1)%scale, (j-1)%scale] + grid[(i+1)%scale, (j+1)%scale])/255)

                    #APPLY CONWAY'S RULES
            #
            if grid[i, j] == ON:
                if (tot < 2) or (tot > 3):
                    newgrid[i, j] = OFF
            else:
                if tot == 3:
                    newgrid[i, j] = ON
    #copy grid into newgrid to hold
    img.set_data(newgrid)
    grid[:] = newgrid[:]
    return img
# main()
def main():
    #create argument parser variable
    parser = argparse.ArgumentParser(description="Conway's Game Of Life")
    #add arguments to the parser variable parser
  #destination arguments
    parser.add_argument('--grid-size', dest='scale', required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
  #action arguments
    parser.add_argument('--glider', action='store_true', required=False)
    parser.add_argument('--learn', action='store_true', required=False)
  #parse the arguments and assign it to the args variable
    args = parser.parse_args()

    #if --learn argument is thrown
    if args.learn:
        print('===========================================================================')
        print('Try typing Conwaymatplotanimation.py --grid-size 32 --interval 500 --glider')
        print('===========================================================================')
        quit()

    #the grid size can never be smaller that 8
    scale = 100
    if args.scale and int(args.scale) > 8:
        scale = int(args.scale)

        #set the animation update interval
    updateinterval = 50
    if args.interval:
        updateinterval = int(args.interval)
    #declare a blank grid
    grid = np.array([])
    #place the glider somewhere
    if args.glider:
        #clear grid
        grid = np.zeros(scale*scale).reshape(scale, scale)
        #insert glider into new fresh grid
        glider(1, 1, grid)
    else:
        #populate grid randomly
        grid = randgrid(scale)
    # this sets up matplotlib.animation or something
#    fig, ax = plt.subplots(figsize=(scale, scale))
    img = ax.imshow(grid, interpolation='nearest')
    animation = anim.FuncAnimation(fig, updateframe, init_func=init, fargs=(img, grid, scale),
                                   frames = 10, interval=updateinterval, save_count=50)


    # create output file
    if args.movfile:
        anim.save(args.movfile, fps=30, extra_args=['-vcodec', 'libx264'])
    # show plot ?? play iterations?
    plt.show()
#call main
if __name__ =='__main__':
    main()

