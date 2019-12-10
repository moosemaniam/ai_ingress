import random
from agent import *
from portal import *
class world:
    def __init__(self,res_x,res_y,num_portals):
        self.res_x = res_x
        self.res_y = res_y
        self.num_portals=num_portals 
        self.portal_list=[]

        #Create the required number of portals
        #Randomize the x and y location 
        for i in range(0,self.num_portals):
            x = random.randint(0,res_x)
            y = random.randint(0,res_y)
            self.portal_list.append(portal(x,y))

        


              