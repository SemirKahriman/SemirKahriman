# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 11:30:17 2022

@author: Semir
"""
import random
from sys import exit
import rastergrid

class Agent:
    "Defining all the agents, applying characteristics and coordinate start point set age of agents at 0,store starts at 0"
    def __init__ (self,agents,environment,ia,td_ys,td_xs, y, x,sex=None):
        """
        
        Parameters
        ----------
        agents : TYPE
            DESCRIPTION.
        environment : TYPE
            DESCRIPTION.
        ia : TYPE
            DESCRIPTION.
        td_ys : TYPE
            DESCRIPTION. "using the web scraping  to find X coordinate, if there are values unknown or missing it will be classed as None, If it is None a Random Number will be assigned."

        td_xs : TYPE
            DESCRIPTION. "using the web scraping to find X coordinate, if there are values unknown or missing it will be classed as None, If it is None a Random Number will be assigned."
        y : TYPE
            DESCRIPTION.
            Float giving position of Y Coordinate read from Web or provided by random.random
        x : TYPE
            DESCRIPTION.
            Float giving position of X Coordinate read from Web or provided by random.random


        sex : TYPE, optional
            DESCRIPTION. The default is None.
            Defining the gender of the Agents

        Returns
        -------
        None.


        """
        self.id = ia
        self.environment = environment
        self.age = 0
        self.store = 0
        self.agents = agents
        self.status = True
        self.sex = sex
        # self.x = random.randint(0,300)
        # self.y = random.randint(0,300)

        "Defines the sex of agent from value initial starting class as None into Male or Female,"


        # if webscraping result does not return any coordinate then the X or Y is provided by random.random
        if (x == None):
            self.x = random.randint(0,300)
        else:
            self.x = x 
        if (y == None):
            self.y = random.randint(0,300)
        else:
            self.y = y

        # Define sex of agent as male or female so that it can be coloured black or white
        if sex is None:
            self.sex = random.choice(['male','female'])
        else:
            self.sex = sex
        
        
    def increase_age(self):
        """
        Parameters
        ----------
        increase age by 1 until reaching 80 at which point agent classed as dead (false status)

        Returns:
        
        Agent will age with each iteration and then die at the age of 70
        None.

        """
        self.age = (self.age+1)
        if self.age >= 70:
            self.status = False
    
    def move(self):
        """
        Parameters
        ----------
        "move the agent based upon the set environment sequence up to 300" 

        Returns:
        Agent moves +1 in the X or Y position
        With each movement store is decreased by 5
        None.

        """
        if  random.random() <0.5:
            self.x=(self.x+1) %300
        else:
            self.x=(self.x-1) %300
        if  random.random() <0.5:
            self.y=(self.y+1) %300
        else:
            self.y=(self.y-1) %300
        self.store -= 5

    

    def move_grave(self):
        """
        Parameters
        ----------
        If Agent is classed as False due to Age Store or other attribute then 
        
        Returns:
        Agent is moved to position (310,360) on the grid (graveyard) which is off the model screen

        """
        
        self.x = random.randint(310,360)
        self.y = random.randint(310,360)
            

    def eat(self): # eating 10
        """
        Parameters
        ----------
        eat the environment by 10
        
        Returns:
        Store is increased by a value of 10
        Environment is decreased by a value of 10
        --------
        
        """
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
    

    def excrete(self): #excrete 100
        """
        Parameters
        ----------
        If store of agent increases above 200 after eating the environment.
        
        Returns:
        -------
        Removes the store and increase that xy position on the environment by 50
        Store is decreased by 50 on the agent, and the environment is grown by 50 on that plot. 
        If store reaches above 350 agent will die 
        """
        if self.store >= 200:
            self.store-=50
            self.environment[self.y][self.x]+= 50
        
        if self.store >= 350:
            self.status = False
                

    
    "calculate distance between self and other agents "
    def distance_between(self,agent):    
        """
        
        
        Parameters
        ----------
        Distance between :"calculate distance between self and other agents "
        
        Returns:
        -------
        Distance of Sheep between eachother based on pythagoras theorem
        
        
        """
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5 
    
    
    "share with agents, if self then do not share use distance and share equally"
                    
                    
    
    def share_with_neighbours(self,neighbourhood):
        """
        

        Parameters
        ----------
        Argument: Distance to neighbour must be less than the value of the environment
        neighbourhood : calculate distance between self and other agents and checks against the environment

        Returns:
        -------
        Store of the agents will be shared between eachother based on average (total store between two agents / 2)

        """
        
        
        
        
        for agent in self.agents:
            if self.id != agent.id:
               
                distance = self.distance_between(agent) 
                "If distance is less than or equal to the neighbourhood"
     
                if distance <= neighbourhood:    
                   #print("sharing",self.id,agent.id)  
                   sum = self.store + agent.store
                   avg = sum /2
                   self.store = avg
                   agent.store = avg
                   return
                   
         
    "When printing these will be listed this is the defintiion of the string at the start of the code"
    def __str__(self):
        return "id" + str(self.id) + ", x = " + str(self.x) + ", y = " +str(self.y)+ ", store = "+str(self.store)+ ", age = "+str(self.age)+ ", sex = "+str(self.sex)
     
    