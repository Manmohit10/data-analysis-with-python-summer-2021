#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn import linear_model


def coefficient_of_determination():
    df=pd.read_csv("src/mystery_data.tsv",sep="\t")
    model=linear_model.LinearRegression(fit_intercept=True)
    model.fit(df.loc[0:,['X1','X2','X3','X4','X5']],df['Y'])
    X=df.loc[0:,['X1','X2','X3','X4','X5']]
    Y=df['Y']
    r2=[]
    r2.append(model.score(X,Y))
    model1=linear_model.LinearRegression(fit_intercept=True)

    for i in range(0,5):
        x=df[[f'X{i+1}']]  #df.iloc[:,i][:,np.newaxis]
        model1.fit(x,Y)
        r2.append(model1.score(x,Y))
    return r2
    
def main():
    coeff=coefficient_of_determination()
    print(f"R2-score with feature(s) X: {coeff[0]}")
    for i in range(1,6):
        print(f"R2-score with feature(s) X{i}: {coeff[i]}")

if __name__ == "__main__":
    main()
