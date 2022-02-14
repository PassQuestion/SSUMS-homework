import matplotlib.pyplot as t
from numpy import *                                                                                                                                                    t.rcParams['font.family']=['FreeSans']
a=loadtxt("./temp.txt")
t.plot(a, marker = "H")                       
t.title("the temperature from 1.30-2.8")
t.xlabel("days")
t.ylabel("temperature/°C")
t.grid(linestyle=':')
t.show()
