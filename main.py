#   Rubicks cube simulator engine   #
#       Created by Alpacah          #
#           27/11/2016              #

from tkinter import *
from random import randrange

def drawCube():
    global cube
    drawFace(120, 90, 0)
    drawFace(120, 25, 1)
    drawFace(185, 90, 2)
    drawFace(120, 155, 3)
    drawFace(55, 90, 4)
    drawFace(250, 90, 5)

def drawFace(startX, startY, face):
    global cube
    colors = ["#FFFFFF", "#FF6600", "#0000FF", "#FF0000", "#00FF00", "#BBBB00"]
    for part in range(9):
        if (part == 3 or part == 6):
            startX -= 60
            startY += 20
        cubeCanvas.create_rectangle(startX + part * 20, startY, startX + part * 20 + 20, startY + 20, fill=colors[cube[face][part]], width=2)

def moveFace(moveFace):
    global cube
    colors = ["#FFFFFF", "#FF5800", "#0051BA", "#C41E3A", "#009E60", "#FFD500"]
    isReverse = []
    # adjacent in clockaround order [face, part0, part1, part2]
    adjacents = [[[1, 6, 7, 8], [2, 0, 3, 6], [3, 2, 1, 0], [4, 8, 5, 2]], #fix
                 [[5, 2, 1, 0], [2, 2, 1, 0], [0, 2, 1, 0], [4, 2, 1, 0]], #fix
                 [[1, 8, 5, 2], [5, 0, 3, 6], [3, 8, 5, 2], [0, 8, 5, 2]], #fix
                 [[0, 6, 7, 8], [2, 6, 7, 8], [5, 6, 7, 8], [4, 6, 7, 8]], #fix
                 [[1, 0, 3, 6], [0, 0, 3, 6], [3, 0, 3, 6], [5, 8, 5, 2]], #fix
                 [[1, 2, 1, 0], [4, 0, 3, 6], [3, 6, 7, 8], [2, 8, 5, 2]]] #fix
    moveList = [2, 5, 8, 1, 4, 7, 0, 3, 6] # defines witch part goes where on the moved face
    # save variables; can't simply save the cube array even with list()
    savedFace = []
    for i in range(9):
        savedFace.append(cube[moveFace][i])
    savedLine = ["", cube[adjacents[moveFace][0][0]][adjacents[moveFace][0][1]], cube[adjacents[moveFace][0][0]][adjacents[moveFace][0][2]], cube[adjacents[moveFace][0][0]][adjacents[moveFace][0][3]]]

    #move parts in face
    for i in range(9):
        cube[moveFace][i] = savedFace[moveList[i]]

    #move around faces
    for layer in range(4):
        for part in range(1, 4):
            if (layer < 3):
                cube[adjacents[moveFace][layer][0]][adjacents[moveFace][layer][part]] = cube[adjacents[moveFace][layer+1][0]][adjacents[moveFace][layer+1][part]]
            else:
                cube[adjacents[moveFace][layer][0]][adjacents[moveFace][layer][part]] = savedLine[part]                

def makeMove(move):
    moves = [["U", 0, 3],["U'", 0, 1],["R", 2, 3],["R'", 2, 1],["L", 4, 3],["L'", 4, 1],["D", 5, 3],["D'", 5, 1],["B", 1, 3],["B'", 1, 1],["F", 3, 3],["F'", 3, 1]]
    # find ressource id
    identifier = 0
    for i in range(12):
        if (moves[i][0] == move):
            identifier = i

    # calculate position
    for i in range(moves[identifier][2]):
        moveFace(moves[identifier][1])
    drawCube()

def executeCommand(command):
    # read sequence
    command = command.replace(" ", "").replace("²", "2").replace("\n", "").replace("\r", "")
    commands = []
    i = 0
    while i < len(command):
        action = command[i]
        if (i < len(command) - 1):
            if (command[i+1] == "'"):
                action = action + "'"
                i += 1
            elif (command[i+1] == "2"):
                commands.append(action)
                i += 1

        commands.append(action)
        i += 1
    print(commands)

    #play sequence
    for i in range(len(commands)):
        makeMove(commands[i])

def shuffle():
    commands = ["U", "U'", "L", "L'", "R", "R'", "D", "D'", "B", "B'", "F", "F'"]
    moves = 20
    chain = ""
    for i in range(moves):
        chain = chain + commands[randrange(12)]
    print("suffle command: " + chain)
    executeCommand(chain)
        
def solve():
    global cube
    cube = [[0, 0, 0, 0, 0, 0, 0, 0, 0], # white
        [1, 1, 1, 1, 1, 1, 1, 1, 1], # orange
        [2, 2, 2, 2, 2, 2, 2, 2, 2], # blue
        [3, 3, 3, 3, 3, 3, 3, 3, 3], # red
        [4, 4, 4, 4, 4, 4, 4, 4, 4], # green
        [5, 5, 5, 5, 5, 5, 5, 5, 5]] # yellow
    drawCube()

#    1
#  4 0 2 5
#    3
        
cube = [[0, 0, 0, 0, 0, 0, 0, 0, 0], # white
        [1, 1, 1, 1, 1, 1, 1, 1, 1], # orange
        [2, 2, 2, 2, 2, 2, 2, 2, 2], # blue
        [3, 3, 3, 3, 3, 3, 3, 3, 3], # red
        [4, 4, 4, 4, 4, 4, 4, 4, 4], # green
        [5, 5, 5, 5, 5, 5, 5, 5, 5]] # yellow

root = Tk()

cubeCanvas = Canvas(root, width=360, height=240)
cubeCanvas.grid(row=0, column=0)
drawCube()

frame = Frame(root)
frame.grid(row=0, column=1)

Button0 = Button(frame, text="U", command=lambda: makeMove("U"))
Button0.grid(row=1, column=1)
Button1 = Button(frame, text="B", command=lambda: makeMove("B"))
Button1.grid(row=0, column=1)
Button2 = Button(frame, text="R", command=lambda: makeMove("R"))
Button2.grid(row=1, column=2)
Button3 = Button(frame, text="F", command=lambda: makeMove("F"))
Button3.grid(row=2, column=1)
Button4 = Button(frame, text="L", command=lambda: makeMove("L"))
Button4.grid(row=1, column=0)
Button5 = Button(frame, text="D", command=lambda: makeMove("D"))
Button5.grid(row=1, column=3)

Label(frame, text="Reverse").grid(row=3, column=1)

Button0 = Button(frame, text="U'", command=lambda: makeMove("U'"))
Button0.grid(row=5, column=1)
Button1 = Button(frame, text="B'", command=lambda: makeMove("B'"))
Button1.grid(row=4, column=1)
Button2 = Button(frame, text="R'", command=lambda: makeMove("R'"))
Button2.grid(row=5, column=2)
Button3 = Button(frame, text="F'", command=lambda: makeMove("F'"))
Button3.grid(row=6, column=1)
Button4 = Button(frame, text="L'", command=lambda: makeMove("L'"))
Button4.grid(row=5, column=0)
Button5 = Button(frame, text="D'", command=lambda: makeMove("D'"))
Button5.grid(row=5, column=3)

commandPrompt = Entry(root)
commandPrompt.grid(row=1, column=0)

commandButton = Button(root, text="Execute command", command=lambda: executeCommand(commandPrompt.get()))
commandButton.grid(row=1, column=1)
resetButton = Button(root, text="Solve cube", command=solve)
resetButton.grid(row=1, column=2)
resetButton = Button(root, text="Shuffle cube", command=shuffle)
resetButton.grid(row=2, column=1)

print("F2 R' B' U R' L F' L F' B D' R B L2")
root.mainloop()
