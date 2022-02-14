from numpy import*
import matplotlib.pyplot as t
t.rcParams['font.family']=['FreeSans']                            '''start'''                                                       def count_word(items):                                                f = open("./weather.txt","r")                                     i = 0
    for line in f.readlines():
        if items in line:
                i=i+1
    return i
sunny_day=count_word("sunny")                                     cloudy_day=count_word("cloudy")
rainy_day=count_word("rainy")
heavy_cloudy_day=count_word("heavy")                              n = array([sunny_day*10,cloudy_day*10,rainy_day*10,heavy_cloudy_day*10])
t.pie(n , labels=["sunny","cloudy","rainy","overcast"],autopct='%.2f%%')
t.title("the weather from 2021.1.30 to 2021.2.8")
t.show()
