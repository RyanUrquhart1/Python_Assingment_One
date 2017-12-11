""" 
Ryan Urquhart - Assingment One - GEOG5995
    Copyright (C) 2017  Ryan Urquhart

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

#This File contains my agent class for the practical work.
#The code in this file defines what an agent is and how they interact as individuals, with each other and with the environment.

class Agent():
    def __init__ (self, environment, agents):
        self.environment = environment
        self.agents = agents
        self.store = 0
        self.x = random.randint(0,100)
        self.y = random.randint(0,100)

#The code above defines the agent and places this in the environment.
#When imported to the model code it this dicates how the agents behave.
#Within this code we have assinged each agent a store of zero, this will increase as they interacted with the environment.
#Each Agent will start with a random x/y cordinate on a 100x100 grid.

    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 99
        else:
            self.x = (self.x - 1) % 99
        if random.random() < 0.5:
            self.y = (self.y + 1) % 99
        else:
            self.y = (self.y - 1) % 99
            
#The above 'move' code is the movement of the agents.
#Using the random function the cordinates will change based on a generated figure, allowing movements to be classed as 'random'.
          
            
    def eat(self):
        if self.environment[self.y][self.x] > 10:
               self.environment[self.y][self.x] -=10
               self.store +=10
        
#The above 'eat' code is the interaction with the environment. The store variable created earlier is used.
#If the point the agents are stood on has an environment figure greater than 10, this will be taken off the environment and added to the agent store variable.
#The environemnt value is defined by the csv file read in the model programme with each number making up the environment.        


    def vom(self):
        if self.store > 1000:
            self.store = 750
            self.environment[self.x][self.y] = self.environment[self.x][self.y] + 250
  
 #The above 'vom' code is further interaction with the environment.
#If the agents store variable passes a certain level they will return a value back to the environment file.
#Once this happens their store value goes back to 750 out of a possible 1000, meaning they don't return ALL their store, just a quarter.
    
    
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2 
                self.store = ave
                agent.store = ave 
                #print("sharing" + str(dist) + " " + str(ave))
     
#The 'share_with_mneighbours' is the point communication between agents enters the model.
#Here agents are either adjusting their variables or each others and uses the distance inbetween individual agents that is below this comment.
#The commented out print command is to check the code is working and can indlued to return distances between agents.
       
           
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
        
            
########################################################
        
            
    
               
        
        


    
         
         
         
         
         
         
         
         
         
         
         
         
         

        
         

         
         
         
         
import random
