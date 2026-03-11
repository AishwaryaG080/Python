import numpy as np

def CalMean():
    #Load the data
    X=[6,7,8,9,10,11,12]

    print("Mean Values are: ",X)

    mean_x = np.mean(X)
    variance = np.var(X)
    Std_dev = np.std(X)

    print("MEAN is :", mean_x)
    print("variance is :", variance)
    print("Std_dev is :", Std_dev)

def main():
    CalMean()

if __name__ == "__main__":
    main()