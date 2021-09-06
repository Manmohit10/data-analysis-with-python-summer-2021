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
    alphas=list("abcdefghijklmnopqrstuvwxyzäö-")
    result=np.zeros((len(a),29))
    for w,word in enumerate(a):
        word=word.lower()
        i=0
        for letter in word:
            i=alphas.index(letter)
            result[w,i]+=1
        """features = np.zeros((len(a), len(alphabet)))
	    for i, w in enumerate(a):
		counts = Counter(w)
		for j, l in enumerate(alphabet):
			features[i, j] = counts[l]"""

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
    Fin_target=np.zeros((len(Flist),1))
    Eng_target=np.ones((len(Elist),1))
    print(Fin_target.shape,Eng_target.shape)
    combined_target=np.vstack([Fin_target,Eng_target])
    print(combined_target[0:2])
    Fin_feature=get_features(F_ar)
    print(Fin_feature[0:5])
    E_ar=np.array(Elist)
    Eng_feature=get_features(E_ar)
    combined_feature=np.vstack([Fin_feature,Eng_feature])
    
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
