#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression

def mystery_data():
    df=pd.read_csv("src/mystery_data.tsv",sep="\t")
    model=LinearRegression(fit_intercept=False)
    model.fit(df.loc[0:,['X1','X2','X3','X4','X5']],df['Y'])
    print(model.coef_)
    print(model.intercept_)
    return model.coef_

def main():
    coeff = mystery_data()
    print(f"Coefficient of X1 is {coeff[0]}\nCoefficient of X2 is {coeff[1]}\nCoefficient of X3 is {coeff[2]}\
            \nCoefficient of X4 is {coeff[3]}\nCoefficient of X5 is {coeff[4]}")
    
if __name__ == "__main__":
    main()
