# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *

import tkinter
from tkinter import *
import PIL.Image
from PIL import Image, ImageTk
import subsample
import random

from tkinter import *

####################################
# customize these functions
####################################

import math
import random

class ques():
    def __init__(self):
        ques.level = 0 
        pass

def makeQues(level):
    if level <= 2: result = generateEQ()
    elif level <= 6: result = generateMQ()
    elif level <= 10: result = generateHQ()
    else: data.mode = "gameOver"
    return result

def generateEQ(a = 10, ops=['+','-','*'], asteroids=4):
    answer = random.randint(1,a)
    numSet = set()
    for i in range(10):
        numSet.add(random.randint(1,a))
    operator = random.choice(ops)
    b1 = random.sample(numSet,1)[0]
    if operator == '+':
        b2 = answer - b1 #random.sample(numSet,1)[0]
    elif operator == '-':
        b2 = answer + b1
    else:
        if answer%b1 == 0: #divisible
            b2 = int(answer/b1)
        else:
            if answer<b1: return generateEQ(a) 
            else:   
                b2 = answer//b1
                b1 = answer//b2
                answer = b1*b2
    numSet = set()
    for i in range(asteroids):
        numSet.add(random.randint(1,a))
    numSet.add(answer)
    numSet.add(b1)
    numSet.add(b2)
    if b1==b2 or b1==answer or b2==answer: return generateEQ(a, ops, asteroids)
#    print(b2, operator, b1, answer, numSet)
    return (b2, operator, b1, answer, numSet)

def generateMQ():
    a=100
    asteroids = 7
    ops=['+','+','-','-','*','*','*']
    b2, operator, b1, answer, numSet = generateEQ(a, ops,asteroids)
    return b2, operator, b1, answer, numSet

def generateHQ():
    a=5000
    ops=['+','-','*','*','*']
    asteroids = 10
    b2, operator, b1, answer, numSet = generateEQ(a, ops, asteroids)
    if -10<=b1<=10 and -10<=b2<=10: return generateEQ(a, ops, asteroids)
    return b2, operator, b1, answer, numSet

def game():
    for level in range(0, 10):
        print(makeQues(level))



def init(data):
    # load data.xyz as appropriate
    data.mode = "introScreen"
    loadCosmosImage(data)
    
    loadAstroidImage(data)
    loadDeathStarImage(data)
    data.level = -1
    #data.astroidClickCount = 0
    data.astroids = None
    data.question = None
    data.box1 = None
    data.box2 = None
    data.operator = None
    data.radius = 20
    data.answer = None
    data.score = 0
    data.timeLeft = 10
    data.message = None
    data.round = None
    data.displayMessage = None
    data.delay = 0
    


def loadCosmosImage(data):
    filename = '/Users/aditribhagirath/Desktop/galaxy.jpg'
    data.cosmos = PIL.ImageTk.PhotoImage(file = filename)
    
def loadAstroidImage(data):
    filename = '/Users/aditribhagirath/Desktop/astroid.jpg'
    data.astroidImage = PIL.ImageTk.PhotoImage(file = filename)
"""      
def loadSpaceshipImage(data):
    filename = '/Users/aditribhagirath/Desktop/galaxy.jpg'
    data.spaceshipImage = PIL.ImageTk.PhotoImage(file = filename)
  
def loadSpaceshipImage(data):
    filename = '/Users/aditribhagirath/Desktop/spaceship.jpg'
    data.spaceshipImage = PIL.ImageTk.PhotoImage(file = filename)
"""    
def loadDeathStarImage(data):
    filename = '/Users/aditribhagirath/Desktop/deathStar.jpg'
    data.deathStarImage = PIL.ImageTk.PhotoImage(file = filename)
    
"""
def loadAsteroidImage(data):
    filename = '/Users/aditribhagirath/Desktop/asteroid.svg'
    data.asteroidImage = PIL.ImageTk.PhotoImage(file = filename)"""


      
    
def redrawAll(canvas, data):
    # use event.x and event.y
    if data.mode == "introScreen":
        introScreenRedrawAll(canvas, data)
    elif data.mode == "startGame":
        startGameRedrawAll(canvas,data)
    elif data.mode == "playGame":
        playGameRedrawAll(canvas,data)
    elif data.mode == "displayMessage":
        playGameRedrawAll(canvas, data) ### MADE CHANGE HERE LOL FUCK DONALD TRUMP ####
        displayMessageRedrawAll(canvas, data)
    elif data.mode == "gameOver":
        gameOverRedrawAll(canvas, data)
    elif data.mode == "laser":
        laserRedrawAll(canvas, data)


def mousePressed(event, data):
    # use event.x and event.y
    if data.mode == "introScreen":
        introScreenMousePressed(event, data)
    elif data.mode == "startGame":
        startGameMousePressed(event,data)
    elif data.mode == "playGame":
        playGameMousePressed(event,data)
    elif data.mode == "displayMessage":
        displayMessageMousePressed(event, data)
    elif data.mode == "gameOver":
        gameOverMousePressed(event, data)
    elif data.mode == "laser":
        laserMousePressed(event, data)
        
        

    

def keyPressed(event, data):
    # use event.char and event.keysym
    if data.mode == "introScreen":
        introScreenKeyPressed(event, data)
    elif data.mode == "startGame":
        startGameKeyPressed(event,data)
    elif data.mode == "playGame":
        playGameKeyPressed(event,data)
    elif data.mode == "displayMessage":
        displayMessageKeyPressed(event,data)
    elif data.mode == "gameOver":
        gameOverKeyPressed(event, data)
    elif data.mode == "laser":
        laserKeyPressed(event, data)


# Make sure you add undo for accidental misclicks
def playGameMousePressed(event, data):
    for astroid in data.astroids:
        if astroid[0]-data.radius < event.x < astroid[0]+data.radius:
            if astroid[1]-data.radius < event.y < astroid[1]+data.radius:
                data.astroids.remove(astroid)
                if data.box1 == None: 
                    data.box1 = astroid[2]
                elif data.box2 == None: 
                    data.box2 = astroid[2]
                    checkResult(data)
                    data.mode = "displayMessage"
 


def playGameRedrawAll(canvas, data):
    
    canvas.create_image(data.width/2, data.height/2,image = data.cosmos)
    #canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")
    
    canvas.create_rectangle(0, 0, data.width, 70, fill = "grey")
    #canvas.create_text(data.width-80, data.height-30, text = "Click to start!", fill = "white", font = "Arial 20 bold")
    canvas.create_rectangle(data.width/2-220, 30, data.width/2-200+70, 60, fill = "black") #first bl box
    canvas.create_rectangle(data.width/2-20, 30, data.width/2+70, 60, fill = "black") #second bl box
    canvas.create_text(data.width-250, 45, text = "=", font = "Arial 26 bold")
    canvas.create_text(50, data.height-40, text = "Time left = %d" % (data.timeLeft))
    createTimer(canvas, data)
    
    drawAstroids(canvas, data)
    if data.answer!= None:
        
        canvas.create_text(data.width-200, 45, text = data.answer, font = "Arial 26 bold")
    
    if data.operator != None:
        canvas.create_text(data.width/2-70, 45, text = data.operator, font = "Arial 30 bold")
    if data.box1 != None:
        canvas.create_text(data.width/2-175, 45, text = data.box1, font = "Arial 26 bold", fill="white")
    if data.box2 != None:
        canvas.create_text(data.width/2+ 25, 45, text = data.box2, font = "Arial 26 bold", fill = "white")
    
        

    canvas.create_text(70, 35,text ="Score = %d" %(data.score))
    #canvas.create_oval(data.width/2-200, data.height/2-200,data.width/2+200,data.height/2+200, fill = "grey")
    
   
def createTimer(canvas, data):
    x, y = 5, data.height-5
    text = '%d seconds left' % data.timeLeft
    if data.timeLeft>=7: fill = 'green'
    elif data.timeLeft>=4: fill = 'yellow'
    elif data.timeLeft>=0: fill = 'red'
    a = len(text)
    canvas.create_rectangle(0,data.height-30, a*10, data.height) 
    canvas.create_text(x, y,text=text, anchor=SW, fill=fill)

def init2(data):
    data.level += 1
    print('data.q before is:', data.question)
    data.question = makeQues(data.level)
    data.answer
    print('data.q after is:', data.question)
    data.box1 = None
    data.box2 = None
    data.message = None
    data.round = None
    data.line = None
    data.timeLeft = 10
    astroidNumbers = data.question[4]
    data.operator = data.question[1]
    data.answer = data.question[3]
    data.astroids = makeAstroids(astroidNumbers,data)
    if data.level >= 10: data.mode = 'gameOver'

    
    
    
def playGameKeyPressed(event, data):
    pass

def timerFired(data):
    if data.mode == "introScreen":
        introScreenTimerFired(data)
    elif data.mode == "startGame":
        startGameTimerFired(data)
    elif data.mode == "playGame":
        playGameTimerFired(data)
    elif data.mode == "displayMessage":
        displayMessageTimerFired(data)
    elif data.mode == "gameOver":
        gameOverTimerFired(data)
    elif data.mode == "laser":
        laserTimerFired(data)
        
def gameOverRedrawAll(canvas, data):
    canvas.create_image(data.width/2, data.height/2,image = data.cosmos)
    canvas.create_text(data.width/2, data.height/2,text = "Your score was: %d" %(data.score), 
           font = "Arial 40 bold", fill = "white")
    canvas.create_text(data.width/2, data.height/2+ 80,text = "Press 'r' to restart!",  
           font = "Arial 30 bold", fill = "white")
    
    
    

def gameOverTimerFired(data):
    pass

def gameOverMousePressed(event, data):
    pass

def gameOverKeyPressed(event, data):
    init(data)
    data.mode = "startGame"
        
def displayMessageRedrawAll(canvas, data):
    if data.message != None:
        a = len(data.message)
        canvas.create_rectangle(data.width/2-10*a, data.height/2-20, data.width/2+10*a,data.height/2+20,fill = "black")
        canvas.create_text(data.width/2, data.height/2, text = data.message, font = "Arial 30 bold", fill = "cyan")
    else:
        canvas.create_rectangle(data.width/2-150, data.height/2-20, data.width/2+150,data.height/2+20,fill = "black")
        canvas.create_text(data.width/2, data.height/2, text = "You gotta be quicker!", font = "Arial 30 bold", fill = "cyan")
        
    
def displayMessageMousePressed(event, data):
    data.mode = "playGame"
    init2(data)    
    print(data.level)
    print(data.mode)
    
def displayMessageTimerFired(data):
    pass
    
def displayMessageKeyPressed(event, data):
    pass
    


def introScreenMousePressed(event, data):
    if data.mode == "introScreen":
        if (event.x <= data.width/2 + 150 and event.x >= data.width/2 - 150
        and event.y <= data.height/2 + 30 and event.y >= data.height/2 - 30):
            print("Bob")
            data.mode = "startGame"
            print(data.mode)
        return 
        


def introScreenRedrawAll(canvas, data):
    # draw in canvas
    canvas.create_image(data.width/2, data.height/2,image = data.cosmos)
    canvas.create_text(data.width/2, 150, text = "MASTEROIDS", font = "Arial 60 bold", fill = "white")
    
    canvas.create_rectangle(data.width/2-140, data.height/2 - 30, data.width/2+140, data.height/2 + 30)
    canvas.create_text(data.width/2, data.height/2, text = "START MATHING!", font = "Arial 30 bold", fill = "white")
                            
def introScreenTimerFired(data):
    pass
    
def introScreenKeyPressed(event, data):
    pass
    
def startGameTimerFired(data):
    pass
    
def playGameTimerFired(data):
    data.delay += 1
    if data.delay% 10 == 0:
        data.timeLeft -= 1
    for astroid in data.astroids:
        deltax = [-2,0,2]
        deltay = [-2,0,2]
        dx = random.choice(deltax)
        dy = random.choice(deltay)
        newX = astroid[0] + dx
        newY = astroid[1] + dy
   
        if (newX <= data.width-40 and newX >= 40 and newY <= data.height-40 and newY >= 80):
            astroid[0] = newX
            astroid[1] = newY
        print(astroid[0], astroid[1])    
    if data.timeLeft <= 0:
        data.mode = "displayMessage"
        data.timeLeft = 10
    #else:
        #data.timeLeft -= 3

                            
def startGameMousePressed(event, data):
    if (event.x <= 150 and event.x >= 0 and 
       event.y <= data.height and event.y >= data.height-40):
        data.mode = "laser"
        data.line = [150,data.height-150]
        data.level += 1
    level = data.level
    data.question = makeQues(level)
    astroidNumbers = data.question[4]
    data.operator = data.question[1]
    data.answer = data.question[3]
    data.astroids = makeAstroids(astroidNumbers, data)
    
def laserRedrawAll(canvas, data):
    #canvas.create_image(data.width/2, data.height/2,image = data.cosmos)
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")
    
    canvas.create_image(data.width/2, data.height/2,image = data.astroidImage)
    #canvas.create_image(data.width-75, 180,image = data.spaceshipImage)
    canvas.create_image(80, data.height-150,image = data.deathStarImage)
    #canvas.create_image(data.width/2, data.height/2,image = data.asteroidImage)    
    
    #canvas.create_text(80, data.height-30, text = "Click to start!", fill = "white", font = "Arial 20 bold")
    canvas.create_line(150, data.height-150, data.line[0], data.line[1], fill = "red",
                       width = 5)
    # Implement leaderboard
    
    #canvas.create_oval(data.width/2-200, data.height/2-200,data.width/2+200,data.height/2+200, fill = "grey")

def laserTimerFired(data):
    data.line[0] += 10
    data.line[1] -= 10
    if data.line[0] >= 300 and data.line[1] <= data.height-150-100:
        data.mode = "playGame"
    
    
def laserMousePressed(event, data):
    pass
    
def laserKeyPressed(event, data):
    pass
 
 
def makeAstroids(astroidNumbers,data):
     
    possible_coordinates = []
    for i in range (80,data.width,40):
        for j in range (100,data.height,40):
            possible_coordinates += [[i,j]]
    astroids = []
    
    for astroid in astroidNumbers:
        coordinate = random.choice(possible_coordinates)
        possible_coordinates.remove(coordinate)
        
        astroids += [[coordinate[0],coordinate[1],astroid]]
    
    return astroids
    
def drawAstroids(canvas, data):
    for astroid in data.astroids:
        canvas.create_oval(astroid[0]-20, astroid[1]-20, astroid[0] + 20, astroid[1] + 20,
                           fill = "grey")
        canvas.create_text(astroid[0],astroid[1], text = astroid[2])
        
    
def startGameRedrawAll(canvas, data):
    #canvas.create_image(data.width/2, data.height/2,image = data.cosmos)
    canvas.create_rectangle(0, 0, data.width, data.height, fill = "black")
    
    canvas.create_image(data.width/2, data.height/2,image = data.astroidImage)
    #canvas.create_image(data.width-75, 180,image = data.spaceshipImage)
    canvas.create_image(80, data.height-150,image = data.deathStarImage)
    #canvas.create_image(data.width/2, data.height/2,image = data.asteroidImage)    
    
    canvas.create_text(80, data.height-30, text = "Click to start!", fill = "white", font = "Arial 20 bold")
    # Implement leaderboard
    canvas.create_rectangle
    #canvas.create_oval(data.width/2-200, data.height/2-200,data.width/2+200,data.height/2+200, fill = "grey")
    

def checkResult(data):
    if data.operator == '+' and data.box1 + data.box2 == data.answer:
        print('lol')
        #make dialog box that answer was correct and now level up
        data.level += 1
        data.score += 10
        data.score += 10 - data.timeLeft
        data.message = "Well done!"
        
    elif data.operator == '-' and data.box1 - data.box2 == data.answer:
        print('lol1')
        #make dialog box that answer was correct and now level up
        data.level += 1
        data.score += 10
        data.score += 10 - data.timeLeft
        data.message = "Well done!"
    elif data.operator == '*' and data.box1 * data.box2 == data.answer:
        print('lol2')
        #make dialog box that answer was correct and now level up
        data.level += 1
        data.score += 10
        data.score += 10 - data.timeLeft
        data.message = "Well done!"
        
    else:
        print('lol3')
        data.message = "Too bad! The right answer was %d %s %d = %d!" % (data.question[0],
                           data.question[1],data.question[2], data.question[3])
        pass
        #make dialogue box that nswer is incorrect
        #show the correct answer
        #do not increase score


                            

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    
    
    
    
    
    # create the root and the canvas
    root = tkinter.Toplevel()
    
    #######
    #data.root = root
    #######
    
    init(data)
    
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()

    
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    
    print("bye!")

run(700, 700)