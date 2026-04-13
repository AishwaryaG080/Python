#------------------------------------------------------------------
## Bank Term Deposit Subscription Prediction ##
#------------------------------------------------------------------
# Domain: Banking, Marketing
# Problem Statement:
# A Portuguese bank conducted marketing compaigns to promote term deposit subscriptions. 
# The goal is to predict whether a client will subscribe (yes or no) to a term deposit based on their profile and compaign interaction details.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve

def MarvellousClassifier(datapath):
    Border = "-"*50

    print(Border)
    print("Step 1 : Load and Explore Data")
    print(Border)

    df = pd.read_csv(datapath, sep=';')
    print("First 5 rows :\n", df.head())
    print(Border)
    print(df.columns)

    print("Display Statistics :\n",df.describe())

    df.replace('unknown',np.nan, inplace=True)
    df.ffill()

    sns.countplot(x=df["y"])
    plt.title("Class Distribution")
    plt.show()

    print(Border)
    print("Step 2 : Preprocess the data")
    print(Border)

    le = LabelEncoder()
    for col in df.select_dtypes(include='object').columns:
        df[col] = le.fit_transform(df[col])

    X = df.drop("y", axis=1)
    Y = df["y"]

    print("Shape of X : ",X.shape)
    print("Shape of Y : ",Y.shape)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    print(Border)
    print("Step 3 : Split data for Training and Testing")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=42)

    print(Border)
    print("Step 4 : Train the Models")
    print(Border)

    models = {
        'Logistic Regression' : LogisticRegression(),
        'KNN' : KNeighborsClassifier(n_neighbors=5),
        'Random Forest' : RandomForestClassifier() 
    }

    print(Border)
    print("Step 5 : Evaluate the Models")
    print(Border)

    for name, model in models.items():
        model.fit(X_train, Y_train)
        Y_pred = model.predict(X_test)

        print("\n==============================")
        print(name)
        print("==============================")

        print("Accuracy : ",accuracy_score(Y_test, Y_pred)*100)

        cm = confusion_matrix(Y_test, Y_pred)
        print("Confusion Matrix : \n",cm)

        print("Classification Report :\n", classification_report(Y_test, Y_pred))

        # ROC-AUC Score
        Y_prob = model.predict_proba(X_test)[:,1]
        auc = roc_auc_score(Y_test, Y_prob)
        print("ROC-AUC Score : ",auc)

        plt.figure()
        sns.heatmap(cm, annot=True, fmt='d')
        plt.title(name + " Confusion Matrix")
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.show()

        # ROC Curve
        plt.figure()
        fpr, tpr, threshold = roc_curve(Y_test, Y_prob)
        plt.plot(fpr, tpr, label=name + "(AUC="+ str(round(auc,2)) + ")")
        plt.xlabel("False Positive Rate")
        plt.ylabel("True Positive Rate")
        plt.title(name + " ROC Curve")
        plt.legend()
        plt.show()

def main():

    datapath = "bank-full.csv"
    MarvellousClassifier(datapath)

if __name__ == "__main__":
    main()