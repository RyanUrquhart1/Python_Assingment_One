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

#This File contains 

class Agent():
    def __init__ (self, environment, agents):
        self.environment = environment
        self.agents = agents
        self.store = 0
        self.x = random.randint(0,100)
        self.y = random.randint(0,100)

    def move(self):
        if random.random() < 0.5:
            self.x = (self.x + 1) % 99
        else:
            self.x = (self.x - 1) % 99
        if random.random() < 0.5:
            self.y = (self.y + 1) % 99
        else:
            self.y = (self.y - 1) % 99
            
    def eat(self):
        if self.environment[self.y][self.x] > 10:
               self.environment[self.y][self.x] -=10
               self.store +=10

    def vom(self):
        if self.store > 1000:
            self.store = 750
            self.environment[self.x][self.y] = self.environment[self.x][self.y] + 250
       
       
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
            if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2 
                self.store = ave
                agent.store = ave 
                #print("sharing" + str(dist) + " " + str(ave))
                
    def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
        
            
########################################################
        
            
    
               
        
        


    
         
         
         
         
         
         
         
         
         
         
         
         
         

        
         

         
         
         
         
import random
