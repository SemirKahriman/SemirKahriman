Programming with Python
To run the programme, a Python Command console must be used. Open the file directory ‘SemirKahriman/SemirKahriman’ and run the following: model.py to use the model. 

GitHub Directory: ( ‘SemirKahriman/SemirKahriman’ )
model.py
agentframework.py
rastergrid.py
README.TXT
License.TXT

Testing:

Index link:

Software:
The Software is an Agent Based Model, using Python script to simulate Agents interacting with the environment as well as one another. 
A Raster grid text file was used to display rows on a 300 by 300 grid. Using the Matplotlib library to display the grid. 
Each value within the grid is the environment and Agents will subtract from this in the form of sheep grazing on the grass. 
The higher the value the more grass within that pixel.  Applications of this software can be used in automation, 
adapting similar methods and processes to machine learning and other decision-making software. An agent class created 
and given attributes, based on integer and Boolean type values. If and else statements allow for simple decision 
making as well as defining criteria to be met for the simulation to increase in complexity. 

When the software is Run it should show random movement of Sheep along a raster plot, 
they will consume the environment based and grow as their store and age increase.  
The Male and Female sheep will interact with each other and share their stores based 
on distance and the environment will grow above the value of 120 which is designed 
to be water areas. 

Current Software Abilities:
- Eat
Agents can consume the environment as they move around the grid. A store attribute has been added so that when Sheep consume the environment it adds to Store. 

- Move
Agents can share with themselves using the Share with neighbours function, if agents are within a certain distance to each other they can share.

- Increase Age
With every frame or iteration, the age will also increase by 1 for each agent.

- Grow
The Environment will grow in sequence of iterations (frames) above the value of 120.  

- Spawn
When criteria such as certain level of store or is met another set of agents will spawn randomly across the grid. 

- Die
Upon meeting criteria of Age, Agents will pass. 

Gender:
Sheep are displayed as Gender on the graph, White sheep are female black sheep are male. 

Known Issues:
When Agents spawn, they are spawning at random points based on XY Random choice, 
distance between function needs to be created between male and female 
agents as well as spawning correct agents within proximity. 

Ideas for further development
Excrete: Create an' ‘Excrete’ point on the map which increases the value of the Environment in the place of an Agent that reaches a certain value of Store. 
Graveyard: Once an Agent has died and has been removed into a Dead category, display these agents in a graveyard or mark them as an X on the Map. 
Game: Create a Chase Agent that the User can interact with using Buttons on the GUI, this could be in this example a Fox which the user would control by 
moving (up. down, left. Right) by clicking buttons on the GUI. 

Licence:
The licence provided is the MIT which provides permissions on use, states limitations on liability and does not provide a warranty for the Code. 
