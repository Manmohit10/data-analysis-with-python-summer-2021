#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances

from matplotlib import pyplot as plt

import seaborn as sns
sns.set(color_codes=True)
import scipy
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc

def find_permutation(n_clusters, real_labels, labels):
    permutation=[]
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label=scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation

def toint(x):
    DNA=['A','C','G','T']
    LI=[0,1,2,3]
    #d=dict(zip("ACGT", range(4)))
    result=dict(zip(DNA,LI))
    return result[x]

def get_features_and_labels(filename):
    df = pd.read_csv(filename, sep='\t')
    #print(df.head())
    mat = np.zeros((len(df.index),len(df.loc[2,'X'])))
    for i in range(len(df.index)):
        str=df.loc[i,'X']
        row=[]
        for w in str:
            row.append(toint(w))
        mat[i]=np.array(row)
    #print(mat[0:10,:])
    return (mat, df['y'])

def plot(distances, method='average', affinity='euclidean'):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g=sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage )
    g.fig.suptitle(f"Hierarchical clustering using {method} linkage and {affinity} affinity")
    plt.show()

def cluster_euclidean(filename):
    feature,data_label=get_features_and_labels(filename)
    model=AgglomerativeClustering(linkage='average',affinity='euclidean')
    model.fit(feature)
    permutation=find_permutation(len(list(data_label.unique())),model.labels_,data_label)
    perm_label=[permutation[label] for label in model.labels_]
    acc=accuracy_score(data_label,perm_label)
    return acc

def cluster_hamming(filename):
    model=AgglomerativeClustering(linkage='average',affinity='precomputed')
    feature,data_label=get_features_and_labels(filename)
    distance=pairwise_distances(feature,metric='hamming')
    model.fit(distance)
    permutation=find_permutation(len(list(data_label.unique())),model.labels_,data_label)
    perm_label=[permutation[label] for label in model.labels_]
    acc=accuracy_score(data_label,perm_label)
    #plot(distance, "average", "hamming")
    return acc


def main():
    print("Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq"))
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))
    #get_features_and_labels("src/data.seq")
if __name__ == "__main__":
    main()
