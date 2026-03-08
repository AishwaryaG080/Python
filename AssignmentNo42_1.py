import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

def MarvellousPredictor():
    #Load the data
    X=[1,2,3,4,5]
    Y=[3,4,2,4,5]

    print("Values of Independent variables : X - ",X)
    print("Values of Dependent variables : Y - ",Y)

    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    print("X_MEAN is :", mean_x) # 3.0
    print("Y_MEAN is :", mean_y) # 3.6

    n = len(X) #5
    
    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
        denominator = denominator + ((X[i] - mean_x) ** 2)

    m = numerator / denominator

    print("Slope of line ie. m :", m)

    C = mean_y - (m*mean_x)

    print("Y intercept of line ie. C :",C)

    x = np.linspace(1,6,n)
    y = C + m * x

    plt.plot(x,y,color = 'g', label = "Regression Line")
    plt.scatter(X,Y,color='r',label = "Scatter Plot")

    plt.xlabel("X : Independent variables")
    plt.ylabel("Y : Dependent variables")

    plt.legend()
    plt.show()

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()
