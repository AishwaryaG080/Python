import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

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
    # Step 3 : Split data in X & Y
    #----------------------------------------------------------------

    print(Border)
    print("Step 3 : Split data in X & Y")
    print(Border)

    X = df.drop(columns=['Class'])
    Y = df['Class']

    print("Independent variables :", X.shape)
    print("Dependent variables :", Y.shape)

    #----------------------------------------------------------------
    # Step 4 : Split dataset for traning & testing
    #----------------------------------------------------------------

    print(Border)
    print("Step 4 : Split dataset for Traning & Testing")
    print(Border)

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train,Y_train)
    Y_pred = model.predict(X_test)

    print("Testing Data :")
    print(X_test)

    print("Predicted Data :")
    print(Y_pred)

    print("Actal Data :")
    print(Y_test)
    
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
   MarvellousPlayPredictor("WinePredictor.csv")

if __name__ == "__main__":
    main()