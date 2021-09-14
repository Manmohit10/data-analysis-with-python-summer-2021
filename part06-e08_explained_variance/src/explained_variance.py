#!/usr/bin/env python3

import pandas as pd
from sklearn.decomposition import PCA
import numpy as np
import matplotlib.pyplot as plt

def explained_variance():
    df = pd.read_csv('src/data.tsv', sep='\t')
    var = df.var(axis=0)
    pca = PCA()
    pca.fit(df)
    return var, pca.explained_variance_

def main():
    v, ev = explained_variance()
    print(sum(v), sum(ev))
    print("The variances are:", " ".join([f"{x:.3f}" for x in v]))
    print("The explained variances after PCA are:", " ".join([f"{x:.3f}" for x in ev]))
    plt.plot(np.arange(1,11), np.cumsum(ev));
    plt.show()

if __name__ == "__main__":
    main()
