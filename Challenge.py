import numpy as np
import matplotlib
import statistics
import matplotlib.pyplot as plt
import random
import math


Nsim=10000
a=[]

for i in range(Nsim):
    position_x=0
    position_y=0
    for j in range (61): 
        rand=random.uniform(0,1)
        if 6*rand<1:
            position_x=position_x+math.cos(1*math.pi/6)
            position_y=position_y+math.sin(1*math.pi/6)
        elif 6*rand>=1 and 6*rand<2:
            position_x=position_x+math.cos(3*math.pi/6)
            position_y=position_y+math.sin(3*math.pi/6)
        elif 6*rand>=2 and 6*rand<3:
            position_x=position_x+math.cos(5*math.pi/6)
            position_y=position_y+math.sin(5*math.pi/6)
        elif 6*rand>=3 and 6*rand<4:
            position_x=position_x+math.cos(7*math.pi/6)
            position_y=position_y+math.sin(7*math.pi/6)
        elif 6*rand>=4 and 6*rand<5:
            position_x=position_x+math.cos(9*math.pi/6)
            position_y=position_y+math.sin(9*math.pi/6)
        elif 6*rand>=5 and 6*rand<6:
            position_x=position_x+math.cos(11*math.pi/6)
            position_y=position_y+math.sin(11*math.pi/6)
    a.append((position_x**2+position_y**2)**0.5)
    i=i+1

print(statistics.mean(a))
print(statistics.stdev(a))
#b=[i for i in a if i>=4]
#print(statistics.mean(b))
b=[i for i in a if i>=15]
c=[i for i in a if i>=20]
p=len(b)
q=len(c)
print(q/p)




    
    
