import math
import random
from agent import *

class Ingress:
        def __init__(self,res_x,res_y,num_portals):
            self.res_x = res_x
            self.res_y = res_y
            self.num_portals = num_portals
            self.agent_list = []

        def create_agent(self):
              agent_id = random.randint(0,100)
              tempAgent = agent(agent_id)
              self.agent_list.append(tempAgent)
              return agent_id