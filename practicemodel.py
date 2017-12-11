""" Ryan Urquhart - Assingment One - GEOG5995
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


import random
import operator
import matplotlib.pyplot
import agentframework1      
  


      
def distance_between(agent0, agent1):
    return (((agent0.x - agent1.x)**2) + ((agent0.y - agent1.y)**2))**0.5  



      
environment = []        
num_of_agents = 15
num_of_iterations = 200
neighbourhood = 5

agents = []

import csv
f = open ('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)        
 



for row in reader:
    rowlist = []
    for item in row:
       rowlist.append(item)
    environment.append(rowlist)
    
f.close()

matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

    

  
# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework1.Agent(environment, agents))        
     
    
    
# Move the agents.
for j in range(num_of_iterations):
    random.shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
  

      
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()




#below is the code to make the agents add back to the environment once they have
#taken in x amount, this is defined in the agent framework file.
#I'm leaving this out of the final code for now.



for i in range(num_of_agents):
    agents[i].vom()



matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()
        
        


for agent0 in agents:
    for agent1 in agents:
        distance = distance_between(agent0, agent1)       
        #print ("distance test 2 " + str(distance))
        
############################################################








