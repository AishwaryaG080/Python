import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score,accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier



def MarvellousPlayPredictor(DataPath):
    Border = "-"*40
    #------------------------------------------------------
    # Step 1 : Load Dataset
    #------------------------------------------------------

    print(Border)
    print("Step 1 : Load Dataset")
    print(Border)
    df = pd.read_csv(DataPath)

    print("Few records from the dataset :")
    print(df.head())

    # 
    #------------------------------------------------------
    # Step 2 : Data Cleaning
    #------------------------------------------------------

    print(Border)
    print("Step 2 : Data Cleaning")
    print(Border)
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'], inplace=True)

    print(df.shape)

    #----------------------------------------------------------------
    # Step 3 : Split dataset for traning & testing
    #----------------------------------------------------------------

    print(Border)
    print("Step 3 : Split dataset for Traning & Testing")
    print(Border)

    X = df[['Whether','Temperature']]
    Y = df['Play']

    print("Independent variables :", X.shape)
    print("Dependent variables :", Y.shape)

    X['Whether'] = LabelEncoder().fit_transform(X['Whether'])
    X['Temperature'] = LabelEncoder().fit_transform(X['Temperature'])
    
    le = LabelEncoder()
    Y = le.fit_transform(Y)
    print(X)
    print(Y)

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

    #----------------------------------------------------------------
    # Step 3 : Create & Train the Model
    #----------------------------------------------------------------
    print(Border)
    print("Step 3 : Create & Train the Model")
    print(Border)

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X_train,Y_train)
   
   #----------------------------------------------------------------
    # Step 4 : Test the Model
    #----------------------------------------------------------------
    print(Border)
    print("Step 4 : Test the Model")
    print(Border)

    Y_pred = model.predict(X_test)

    #----------------------------------------------------------------
    # Step 5 : Calculate Accuracy
    #----------------------------------------------------------------
    print(Border)
    print("Step 5 : Calculate Accuracy")
    print(Border)

    accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy :",accuracy*100)
    
def main():
   MarvellousPlayPredictor("PlayPredictor.csv")

if __name__ == "__main__":
    main()