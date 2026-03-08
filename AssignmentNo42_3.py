import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

def MarvellousPredictor():
    Border = "-"*40
    #------------------------------------------------------
    # Step 1 : Load Dataset
    #------------------------------------------------------

    print(Border)
    print("Step 1 : Load Dataset")
    print(Border)
    
    X=[1,2,3,4,5]
    Y=[20000,25000,30000,35000,40000]

    X = np.array(X).reshape(-1,1)
    Y = np.array(Y)

    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    print("X_MEAN is :", mean_x)
    print("Y_MEAN is :", mean_y)

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

    #calculate YP, R ** 2

    #----------------------------------------------------------------
    # Step 2 : Split dataset for traning & testing
    #----------------------------------------------------------------
    print(Border)
    print("Step 2 : Split dataset for Traning & Testing")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    #----------------------------------------------------------------
    # Step 3 : Create & Train the Model
    #----------------------------------------------------------------
    print(Border)
    print("Step 3 : Create & Train the Model")
    print(Border)

    model = LinearRegression()

    model.fit(X_train,Y_train)

    #----------------------------------------------------------------
    # Step 4 : Test the Model
    #----------------------------------------------------------------
    print(Border)
    print("Step 4 : Test the Model")
    print(Border)

    Y_pred = model.predict(X_test)

    #----------------------------------------------------------------
    # Step 5 : Evaualte the Model
    #----------------------------------------------------------------
    print(Border)
    print("Step 5 : Evaualte the Model")
    print(Border)

    MSE = mean_squared_error(Y_test, Y_pred)
    RMSE = np.sqrt(MSE)
    R2 = r2_score(Y_test,Y_pred)

    print("Mean sqaured error :", MSE)
    print("Root Mean sqaured error :", RMSE)
    print("R square value",R2)
    
    #----------------------------------------------------------------
    # Step 6 : Plot actual vs predicted
    #----------------------------------------------------------------
    print(Border)
    print("Step 6 : Plot actual vs predicted")
    print(Border)

    plt.figure(figsize=(8,5))
    plt.scatter(Y_test,Y_pred)
    plt.xlabel("Salary")
    plt.ylabel("Experience")
    plt.title("Experience vs Salary")
    plt.grid(True)
    #plt.show()

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()