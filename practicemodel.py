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
#functions used within the code are imported at the start of the code.
#The first three are built in functions where as 'agentframework1' contains the agent class that I have created.

import random
import operator
import matplotlib.pyplot
import agentframework1      
  
#Distance Between agents is cacluted and set to return the distance figure. 
#This code is used the agent to agent communication later on.
      
def distance_between(agent0, agent1):
    return (((agent0.x - agent1.x)**2) + ((agent0.y - agent1.y)**2))**0.5  


#The following code sets up the basics of the model. We have empty lists for the environement and the agents that will be filled later in the code.
#I have set the value of agents to be 15 with the modell running 200 times. The neighborhood value is used in agent to agent communication.     
environment = []        
num_of_agents = 15
num_of_iterations = 200
neighbourhood = 5
agents = []


#The data is read into the model in CSV format, this file contains the environemnt information.
#The numbers represent the amount of food at any given point, the higher the number, the more food and the darker the colour of the visual output.
import csv
f = open ('in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)        
 
#The environment data is then stored in the blank environment list created a few steps previously.

for row in reader:
    rowlist = []
    for item in row:
       rowlist.append(item)
    environment.append(rowlist)
f.close()

#The matplotlib code below is to ensure the environment data is working correctly. 
#This creates the first of three visual outputs, the inital environemnt before any agents appearence or interaction.

matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()

    
#We then create the agents. This is done using the code created earlier and using the imported agentframework1 code.
#This creates 15 individual agents and stores them in the empty agents list.
#The agents position on the grid, characteristics and behaviour is dictated by the agentfamework agent class.

for i in range(num_of_agents):
    agents.append(agentframework1.Agent(environment, agents))        

#I have then added new matplotlib code to show where the agents start on the environemnt.
#We can see looking at the second visual output they have already taken values from the environment and added to their 'store'.     
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()
   
# Moving the agents uses the pre defined number of iterations, 200 in this case.
# The shuffle function has been used to move the agents in a random order, rather than the order dictated by the list, adding to the robustness of the model.
# The agents behaviour here; eat, move and share is dictated by the agentframework1 class, the code can be seen in that file.

for j in range(num_of_iterations):
    random.shuffle(agents)
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
  
#Again I have then added to show the updated visual output following ths code.
#The thrd visual output shows how the 15 agents have moved after 200 iterations.
#The changing environemnt shows how the agents have taken away from the environment.
      
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()


#The final piece of behavioural code is then added. This is the agents added back to the environment.
#In the context of this project it adds realism, the sheep can only eat so much.
#Again, the code that defines how this action takes place is in the agentframework1 agent class.
for i in range(num_of_agents):
    agents[i].vom()


#A final visual output is then created, output 4 shows how the environment looks after all interaction has taken place.
#This generally shows the environemnt as much darker as the spread of resources is much less concentrated than initally due to the agent movement.
matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
matplotlib.pyplot.show()
        
        
#This final bit of code calculates distance between which is used in the agent interaction.
#The final commented out code can be inluded, this shows the distance between agents.

for agent0 in agents:
    for agent1 in agents:
        distance = distance_between(agent0, agent1)       
        #print ("distance test 2 " + str(distance))
        
############################################################

f2 = open('environmentout.csv', 'w', newline='') 
writer = csv.writer(f2, delimiter=' ')
for row in environment:		
	writer.writerow(row)		# List of values.
f2.close()

#This code writes the final environment state into a new file









