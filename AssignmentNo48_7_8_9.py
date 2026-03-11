from sklearn.metrics import confusion_matrix,classification_report

def main():
    Actual = [1,1,1,1,0,0,0,0,]
    Predicted = [1,1,0,1,0,1,0,0]

    matrix = confusion_matrix(Actual,Predicted)
    print(matrix)

    classreport = classification_report(Actual,Predicted)
    print(classreport)


if __name__ == "__main__":
    main()