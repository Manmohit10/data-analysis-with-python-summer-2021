#!/usr/bin/env python3
import numpy as np
from gzip import open  
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

def spam_detection(random_state=0, fraction=1.0):
    with open("src/ham.txt.gz",'r') as h:
        ham=h.readlines()
        f=int(fraction*len(ham))
        ham=ham[0:f]
    with open("src/spam.txt.gz",'r') as s:
        spam=s.readlines()
        f=int(fraction*len(spam))
        spam=spam[0:f]
    comb=ham+spam
    #print(comb[0])
    vector=CountVectorizer()
    x=vector.fit_transform(comb)
    X=x.toarray()
    Y=np.array([0]*len(ham)+[1]*len(spam))[:,np.newaxis]
    print(Y.shape)
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=random_state)
    model=MultinomialNB()
    model.fit(X_train,Y_train)
    predict=model.predict(X_test)

    acc=accuracy_score(predict,Y_test)
    misclassified=[x for x in range(0,Y_test.shape[0]) if predict[x]  !=Y_test[x] ]
    print(misclassified)

    return (acc, X_test.shape[0], len(misclassified))

def main():
    accuracy, total, misclassified = spam_detection(0,0.1)
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
