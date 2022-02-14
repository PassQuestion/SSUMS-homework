from numpy import*
import matplotlib.pyplot as t
t.rcParams['font.family']=['FreeSans']
'''start'''
def count_word(items):
    f = open("./weather1.txt","r")
    i = 0
    for line in f.readlines():
        if items in line:
                i=i+1
    f.close()
    return i
multiple_weather = count_word("multiple")
sunny_day = count_word("sunny")
cloudy_day = count_word("cloudy")
overcast_day = count_word("overcast")
rainy_day = count_word("rainy")
a = array([multiple_weather*10,sunny_day*10,cloudy_day*10,overcast_day*10,rainy_day*10])
t.pie(a,labels=["multiple_weather","sunny","cloudy","overcast","rainy"],autopct='%.2f%%')
t.title("the weather from 2020.1.30 to 2020.2.8")
t.show()
