#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return lines

def get_features(a):
    alphas=str("abcdefghijklmnopqrstuvwxyzäö-")
    print(alphas)
    result=np.zeros((1,29))
    for word in a:
        word=word.lower()
        al_ar=np.zeros((1,29))
        i=0
        for letter in alphas:            
            if letter in word:
                for w in word:
                    if w==letter:
                        al_ar[0,i]+=1
                i=i+1
                
            else:
                i+=1
        """li=[word]
        li2=np.array(li).reshape(1,1)
        row_ar=np.hstack((al_ar))"""
        result=np.vstack([result,al_ar])
    result=result[1:,:]
    print(result.shape)

    return result

def contains_valid_chars(s):
    s=s.lower()
    for letter in s:
        if letter in alphabet_set:
            continue
        else:
            return False
    return True

def get_features_and_labels():
    fin=load_finnish()
    Flist=[]
    for f in fin:
        f=f.lower()
        if contains_valid_chars(f):
            Flist.append(f)
    
    eng=load_english()
    Elist=[]
    for e in eng:
        if e[0].islower():
            e=e.lower()
            if contains_valid_chars(e):
                Elist.append(e)
    F_ar=np.array(Flist)
    Fin_feature=get_features(F_ar)
    Fin_target=np.zeros((len(Flist),1))
    print(Fin_feature[0:5])
    E_ar=np.array(Elist)
    Eng_feature=get_features(E_ar)
    Eng_target=np.ones((len(Elist),1))
    combined_feature=np.vstack([F_ar,E_ar])
    combined_target=np.vstack([Fin_target,Eng_target])
    
    return combined_feature,combined_target


def word_classification():
    X,y=get_features_and_labels()
    model=MultinomialNB()
    model = MultinomialNB()
    cval = model_selection.KFold(n_splits=5, shuffle=True, random_state=0)
    scores = cross_val_score(model, X, y, cv=cval)
    return scores


def main():
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()
