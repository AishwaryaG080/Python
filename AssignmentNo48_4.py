import numpy as np
import pandas as pd
import math

def EucDistance(P1,P2):

    Ans = math.sqrt((P1['X'] - P2['X']) ** 2 + (P1['Y'] - P2['Y']) ** 2)

    return Ans

data =    [
            {'X':25, 'Y':20000},
            {'X':30, 'Y':40000},
            {'X':35, 'Y':80000}
            ]

series = pd.Series(data)
print(series)

#description = series.describe()
#print(description)

new_point = {'X' : 33, 'Y' : 55000}
print(data[0])
print("New Point :",new_point)

Result = EucDistance(data[0], new_point)
print("EucDistance :",Result)