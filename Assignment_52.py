# Cluster students into different academic performance groups based on features like:
## Final grades
## Study time
## Failures
## Absences
# This helps identify:
## Top Performers
## Average Students
## Struggling Students
# Dataset Details:
## Dataset Name: Student Performance Data Set


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

def MarvellousStudentClustering(datapath):
    Border = "-"*50

    print(Border)
    print("Step 1 : Load the Data")
    print(Border)

    df = pd.read_csv(datapath, sep=';')

    # Selected Features for Clustering
    df = df[["G1", "G2", "G3", "studytime", "failures", "absences"]]

    print("First 5 rows :\n", df.head())

    print(Border)
    print("Step 2 : Preprocessing the Data")
    print(Border)

    df.dropna(inplace=True)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df)

    print(Border)
    print("Step 3 : Train the Model")
    print(Border)

    model = KMeans(n_clusters=3, random_state=42)

    df["Cluster"] = model.fit_predict(X_scaled)

    print("Cluster Centers :\n", model.cluster_centers_)

    print(Border)
    print("Step 4 : Cluster Analysis")
    print(Border)

    result = df.groupby("Cluster").mean()
    print(result)


    print(Border)
    print("Cluster Labelling")
    print(Border)

    labels = {}

    for cluster in result.index:
        avg_G3 = result.loc[cluster, "G3"]
        avg_failure = result.loc[cluster, "failures"]
        avg_studytime = result.loc[cluster, "studytime"]

        if avg_G3 > 14 and avg_failure < 1:
            labels[cluster] = "Top Performers"
        elif avg_G3 < 10 and avg_failure >= 1:
            labels[cluster] = "Struggling Students"
        else:
            labels[cluster] = "Average Students"

    print("Cluster Labels Mapping : ",labels)

    df["Performance"] = df["Cluster"].map(labels)

    print(Border)
    print("Step 5 : Visualize the Data")
    print(Border)

    plt.figure() 
    sns.scatterplot(x=df["G3"], y=df["studytime"], hue=df["Performance"])
    plt.title("Student Performance Clusters")
    plt.xlabel("Final Grade (G3)")
    plt.ylabel("Study Time")
    plt.show()

    print(Border)
    print("Sample Output")
    print(Border)
    print(df[["G3", "studytime", "failures", "absences", "Performance"]].head())
   

def main():

    datapath = "student-mat.csv"
    MarvellousStudentClustering(datapath)

if __name__ == "__main__":
    main()