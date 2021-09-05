#!/usr/bin/env python3

import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def fit_line(x, y):
    model=LinearRegression(fit_intercept=True)
    model.fit(x[:,np.newaxis],y)
    n=20
    xfit=np.linspace(10,20,n)
    yfit=model.predict(xfit[:,np.newaxis]) \

    return (model.coef_[0],model.intercept_)
    
def main():
    np.random.seed(2)
    n=20   # Number of data points
    x=np.linspace(10, 20, n)
    y=10*x+40+5*np.random.randn(n)
    a,b=fit_line(x,y)
    print(f"Slope: {a:0.1f}\nIntercept: {b}")
    plt.plot(x,y,'bo')
    plt.plot(x,x*a+b,'r-')
    #plt.plot(xfit,yfit,color='green')
    plt.show()

    
if __name__ == "__main__":
    main()
