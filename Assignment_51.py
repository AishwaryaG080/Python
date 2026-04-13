# Predict whether a news article is Fake or Real using text classification techniques.
# This assignment demonstrates the power of ensemble learning using a Voting Classifier with models like Logistic Regression Decision Tree.
# Dataset Information:
# Dataset Name: Fake News Dataset


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def MarvellousFakeNewsClassifier(fakepath, truepath):
    Border = "-"*50

    print(Border)
    print("Step 1 : Load and Prepare Data")
    print(Border)

    fake_df = pd.read_csv(fakepath)
    true_df = pd.read_csv(truepath)

    fake_df["label"] = 0
    true_df["label"] = 1

    df = pd.concat([fake_df, true_df], ignore_index=True)

    df.dropna(inplace=True)

    X = df["text"]
    Y = df["label"]

    print("Shape of dataset : ",df.shape)
    print(Border)

    sns.countplot(x=Y)
    plt.title("Fake vs Real Distribution")
    plt.show()

    print(Border)
    print("Step 2 : Feature Extraction using TF-IDF")
    print(Border)

    vectorizer = TfidfVectorizer(stop_words='english',  max_df=0.7)

    X_tfidf = vectorizer.fit_transform(X)

    print(Border)
    print("Step 3 : Split the data for Training and Testing")
    print(Border)

    X_train, X_test, Y_train, Y_test = train_test_split(X_tfidf, Y, test_size=0.2, random_state=42)

    print(Border)
    print("Step 4 : Model Training")
    print(Border)

    lr = LogisticRegression(max_iter=1000)
    dt = DecisionTreeClassifier()

    hard_voting = VotingClassifier(
        estimators=[('lr', lr), ('dt', dt)],
        voting='hard'
    )

    soft_voting = VotingClassifier(
        estimators=[('lr', lr), ('dt', dt)],
        voting='soft'
    )

    models = {
        "Logistic Regression" : lr,
        "Decision Tree" : dt,
        "Hard Voting" : hard_voting,
        "Soft voting" : soft_voting
    }

    print(Border)
    print("Step 5 : Evaluate the Model")
    print(Border)

    for name, model in models.items():
        model.fit(X_train, Y_train)
        Y_pred = model.predict(X_test)

        print("\n===================================")
        print(name)
        print("===================================")

        print("Accuracy : ",accuracy_score(Y_test, Y_pred)*100)

        cm = confusion_matrix(Y_test, Y_pred)
        print("Confusion Matrix : \n", cm)

        print("Classification Report :\n", classification_report(Y_test, Y_pred))

        plt.figure()
        sns.heatmap(cm, annot=True, fmt='d')
        plt.title(name + " Confusion Matrix")
        plt.xlabel("Predicted")
        plt.ylabel("Actual")
        plt.show()


def main():

    fakepath = "Fake.csv"
    truepath = "True.csv"

    MarvellousFakeNewsClassifier(fakepath, truepath)

if __name__ == "__main__":
    main()