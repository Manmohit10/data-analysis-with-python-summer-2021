#!/usr/bin/env python3

import pandas as pd
import numpy as np
import scipy
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def nonconvex_clusters():
    df=pd.read_csv("src/data.tsv",sep="\t")
    #print(df.head())
    X=df[['X1','X2']]
    Y=df['y']
    model=[]
    acc=[]
    clusters=[]
    original_clusters=len(set(Y))
    outliers=[]
    
    n=np.arange(0.05, 0.2, 0.05)
    columns=['eps','Score','Clusters','Outliers']
    result=pd.DataFrame(columns=columns)

    for i in range(4):
        model.append(DBSCAN(eps=n[i]))
        model[i].fit(X)
        y_predict=model[i].labels_
        
        df[i]=y_predict
        mod_Y=df[df[i]!=-1]['y']
        #idx=y_predict!=(-1)
        #mod_Y_predict=y_predict[idx]
        mod_Y_predict=df[df[i]!=-1][i]


        cluster_temp=set(y_predict)
        if (-1) in cluster_temp:
            new_clusters=len(cluster_temp)-1
            clusters.append(new_clusters)
        else:
            new_clusters=len(cluster_temp)
            clusters.append(new_clusters)
        if original_clusters==new_clusters:
            acc.append(accuracy_score(mod_Y,mod_Y_predict))            
        else:
            acc.append(np.nan)
        outliers.append(list(y_predict).count(-1))
        result.loc[len(result.index)]=[n[i],acc[i],clusters[i],outliers[i]]
    #permulation=find_permutation()
    

    new_label=[]    
    fig,ax=plt.subplots(2,2)
    m=0
    for j in range(2):
        for k in range(2):
            ax[j,k].scatter(df['X1'],df['X2'], c=model[m].labels_)
            m+=1
    #plt.show()
    return result

def main():
    print(nonconvex_clusters())

if __name__ == "__main__":
    main()
