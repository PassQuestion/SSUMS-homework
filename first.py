import matplotlib.pyplot as t
from numpy import *                                                                                                                 '''start'''                                                       t.rcParams['font.family']=['FreeSans']
a=loadtxt("./temp.txt")
t.plot(a, marker = "H")                                           t.legend(labels=["2020max","2020min","2021max","2021min"])
t.title("the temperature from 1.30-2.8")
t.xlabel("days")
t.ylabel("temperature/°C")
t.grid(linestyle=':')
t.show()
