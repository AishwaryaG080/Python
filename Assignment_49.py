# Objective:
# Build a Machine Learning model to predict whether a patient is diabetic (1) or not (0) based on medical attributes.


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def MarvellousClassifier(datapath):
    Border = "-"*50
    
    print(Border)
    print("Step 1 : Load and Explore Dataset")
    print(Border)

    df = pd.read_csv(datapath)

    print("First 5 rows : \n",df.head())
    print("Shape of Dataset : \n",df.shape)

    print("Display Statistics : \n",df.describe())

    columns = ['Glucose','BloodPressure','SkinThickness','Insulin','BMI']
    for col in columns:
        df[col] = df[col].replace(0, df[col].mean())

    print(Border)
    print("Step 2 : Split dataset into features and target")
    print(Border)

    X = df.drop('Outcome', axis=1)
    Y = df['Outcome']

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    print(Border)
    print("Step 3 : Split dataset for training and testing")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=42)

    print(Border)
    print("Step 4 : Model Selection")
    print(Border)
    
    model = LogisticRegression()
    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    print(Border)
    print("Step 5 : Evaluate the Model")
    print(Border)

    print("Accuracy is : ",accuracy_score(Y_test, Y_pred)*100)

    print("Confusion Matrix : \n",confusion_matrix(Y_test, Y_pred))

    print("Classification Report : \n",classification_report(Y_test, Y_pred))

    print(Border)
    print("Step 6 : Visualize the data")
    print(Border)

    sns.heatmap(confusion_matrix(Y_test,Y_pred), annot=True, fmt='d')
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.show()
    
    print(Border)
    print("Step 7 : Display Sample Predictions")
    print(Border)

    sample = X_test[:5]
    predictions = model.predict(sample)

    result = pd.DataFrame(sample, columns=X.columns)
    result['Prediction'] = predictions

    print("Sample Preditions : \n",result)

    result.to_csv("predicted_diabetes.csv", index=False)
    print("Predictions saved to CSV file")


def main():
    datapath = "diabetes.csv"

    MarvellousClassifier(datapath)

if __name__ == "__main__":
    main()