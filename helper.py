import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import string
import nltk
from nltk.tokenize import TreebankWordTokenizer
from nltk.stem.porter import PorterStemmer


import json
with open('coding_qustion.json') as file:
    input = json.load(file)
    
STEMMER = PorterStemmer()
REMOVE_PUNCTUATION_TABLE = str.maketrans({x: None for x in string.punctuation})
TOKENIZER = TreebankWordTokenizer()
def tokenize_and_stem(s):
    return [STEMMER.stem(t) for t in TOKENIZER.tokenize(s.translate(REMOVE_PUNCTUATION_TABLE))]
           
def ques(query,cv,doc_vectors):
    #cv=pickle.load(open('converting_matrix.pkl','rb'))
    #doc_vectors=pickle.load(open('doc_vectors.pkl','rb'))
    x=[query]
    query_vector = cv.transform(x)
    similarity = cosine_similarity(query_vector, doc_vectors)
    ranks = (-similarity).argsort(axis=None)
    output=[]
    for i in range(0,50):
        y={"link":input['data'][ranks[i]]['link'],
           "text":input['data'][ranks[i]]['text']
        }
        output.append(y)
    ans=[]
    for i in output:
        if i not in ans:
            ans.append(i)
            if len(ans)==10:
                break
    return ans

    
