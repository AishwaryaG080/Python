import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.preprocessing import StandardScaler

def StdScalar():
    #Load the data
    df = np.array( [[25, 20000],
            [30, 40000],
            [35, 80000]] )

    print("Data",df)
    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(df)

    print("Scaled Data :", scaled_data)
   

def main():
    StdScalar()

if __name__ == "__main__":
    main()
