#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn import metrics
from sklearn.metrics import accuracy_score

def plant_classification():
    data=load_iris()
    x_train,x_test,y_train,y_test=train_test_split(data.data,data.target,random_state=0,train_size=0.8)
    model=naive_bayes.GaussianNB()
    model.fit(x_train,y_train)
    predict=model.predict(x_test)
    print(data.target_names[predict])
    acc=accuracy_score(predict,y_test)

    return acc

def main():
    print(f"Accuracy is {plant_classification()}")

if __name__ == "__main__":
    main()
