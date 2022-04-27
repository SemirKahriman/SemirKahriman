# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 11:30:17 2022

@author: Semir
"""


"The intention of this model code is to create an agent based model"
"Agents are sheep which consume the envrionment, created here using a raster grid"


import random
import tkinter
import matplotlib.pyplot
import agentframework
import rastergrid
import matplotlib.animation 
import requests
import bs4
import matplotlib
from tkinter import * 






r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})

"changes the backend of spyder for GUI"
matplotlib.use('TkAgg')

"creates the size of the figure window"
fig = matplotlib.pyplot.figure(figsize=(7, 7))

"add axes to the figure"
ax = fig.add_axes([0, 0, 1, 1])

"creates an empty list for the agents, the agents framework is appended into the [] which provides further detail on the agents"
agents = []
dead=[]
num_of_iterations = 500
neighbourhood = 20
dead_agents = []



"global variable starts process"

carry_on = True


"Set seed ,this keeps the starting point the same random number each time the sim is run"
random.seed(1)

"create agents, reads in agent framework.py and defines the agents" 
"for the number of agents that are specified at the start, this will add this data to the list created num_of_agents[]" 
"it calls upon the agentframeworky.py appending the information for each agent on the raster grid."
"Y and X have been read from web page text to define starting grid points"


"test to see if starting positions are being scraped from web correctly"
    # print(agents[i])
"test for sharing of neighbours function using store as agents 2 and 5 were closest"
    # if (j==2):
    #     store=10
    # else:
    #     store = 100


"Runs all the processes each frame"
def update(frame_number):
    #Clears any figures present on the plot
    fig.clear()   
    "Simulation of iterations for num of agents to move eat share, for the 10 agents over 100 iterations and for every agent move eat share and increase age"
    "if the agent is classed as false = dead, then remove the agent from its current position"
    for i in range (len(agents)):
        if agents[i].status == False:
            agents[i].move_grave()
            #Attempt at killing the agents upon criteria met of store and age 
            #dead.append(agents[i])
            
        
        else:
            agents[i].move()
            agents[i].share_with_neighbours(neighbourhood)
            agents[i].increase_age()
            agents[i].excrete()
            agents[i].eat()

    "Once critera has been met of being above the age of 10 and store has increased spawn more agents"
    for i in range (len(agents)):
        if agents[i].age == 10 and agents[i].store <=300 :
            y = None
            x = None
            agents.append(agentframework.Agent(agents,rastergrid.environment,i,td_ys,td_xs, y, x,)) 

       
    
    # for deadagents in dead_agents:
    #     agents.remove(dead_agents)
                    
    "print the agents"
    for i in range(len(agents)):
        if agents[i].status==True:
            #print(agents[i])
            matplotlib.pyplot.xlim(0, 300)            
            matplotlib.pyplot.ylim(0, 300)
            matplotlib.pyplot.title("Agent based model")
            matplotlib.pyplot.imshow(rastergrid.environment,cmap='gist_earth')
            matplotlib.pyplot.scatter(agents[i].x,agents[i].y,s=agents[i].age, c = ('black' if agents[i].sex == "male" else 'white')) 

      



    "Grow the environment if it is above 120, the 120 Signifies the lake/ river area on the raster grid"
    for row in range(len(rastergrid.environment)):
        for col in range(len(rastergrid.environment[row])):
            if (rastergrid.environment[row][col] >= 120):
                #print(rastergrid.environment[row][col], "before adding")
                rastergrid.environment[row][col] = rastergrid.environment[row][col] + 2
                #print(rastergrid.environment[row][col], "after adding")


    "plot the agents within the scatter,create plot of raster and agents and color them black or white depending on male or female"
    
        # print(agents[i].x,agents[i].y)

    "keeps all data on the same scale"
    #ax.set_autoscale_on(False)
    
        
    # for j in range(num_of_iterations):
    "Runs the animation in a GUI window"
def run():

    "adds context window to the animation, figure is the raster plot with agentss, running for the number of iterations and then stopping"
    
    
    

    num_of_agents = int(slider.get())
    
    for i in range(num_of_agents):
        y = int(td_ys[i].text)*3
        x = int(td_xs[i].text)*3
        agents.append(agentframework.Agent(agents,rastergrid.environment,i,td_ys,td_xs, y, x,)) 


    
    animation = matplotlib.animation.FuncAnimation(fig, update, interval=1,repeat=True,frames=num_of_iterations)
    canvas.draw()

    
"creating tkinter window"
root = tkinter.Tk()


"creates the slider bar to change a variable "
v1 = DoubleVar()

# #testing to see if Slider works and Values change, Command function is in the slider code line (command print value)"
def num_agents(val):
        num_of_agents = int(slider.get())
        print(num_of_agents)

sel = "Horizontal Scale Value = " + str(v1.get())
slider = Scale( root, variable = v1, from_ = 1, to = 100, orient = HORIZONTAL,command=num_agents)
l3 = Label(root, text = "Num of Agents")
l1 = Label(root)
slider.pack(anchor = CENTER) 
l3.pack()
l1.pack() 



"creates title for tkinter widnow in top right corner"
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig,master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1) 

"adds menu bar to tikinter model defining menu title and commands within"
menubar = tkinter.Menu(root)
root.config(menu=menubar)
model_menu = tkinter.Menu(menubar)
menubar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run) 
#model_menu.add_command(label="Stop model", command=stop) 
model_menu.add_command(label="Close Model", command=root.destroy)

#w = tkinter.Canvas(root, width=000, height=000)
#w.pack()
#canvas.draw() 
tkinter.mainloop() 
 






"print the agents"
#for i in range(len(agents)):
    #print(agents[i])
    
"Initial version of  creating plot of raster and agents"

# matplotlib.pyplot.xlim(0, 300)
# matplotlib.pyplot.ylim(0, 300)
# matplotlib.pyplot.imshow(rastergrid.environment)
# for i in range(num_of_agents):
#         matplotlib.pyplot.scatter(agents[i].x,agents[i].y)


"OLD CODE"

# for j in range(num_of_iterations):

            # if random.random() < 0.5:
            #     agents[i][0] = (agents[i][0] + 1) % 100
            # else:
            #     agents[i][0] = (agents[i][0] - 1) % 100

            # if random.random() < 0.5:
            #     agents[i][1] = (agents[i][1] + 1) % 100
            # else:
            #     agents[i][1] = (agents[i][1] - 1) % 100

            # if random.random() < 0.5:
            #     agents[i][0] = (agents[i][0] + 1) % 100
            # else:
            #     agents[i][0] = (agents[i][0] - 1) % 100
        
            # if random.random() < 0.5:
            #     agents[i][1] = (agents[i][1] + 1) % 100
            # else:
            #     agents[i][1] = (agents[i][1] - 1) % 100


    #answer = (((agents[0][0] - agents[1][0])**2) + ((agents[0][1] - agents[1][1])**2))**0.5
    
    
#Does this match the YX cooridnates, or is this the old coordinates, the grid doesnt match the list




#Pythagoros code
 


## max AGENT with Color Red
# m = max(agents, key=operator.itemgetter(1))
# matplotlib.pyplot.scatter(m[1],m[0], color='red')
# matplotlib.pyplot.show()
#change color matplotlib.pyplot.scatter(x-coordinate, y-coordinate, color='red')




# random.seed(1)
#  # = random.randint(0,99)
# agents = random.randint(0,99)
# print(agents)