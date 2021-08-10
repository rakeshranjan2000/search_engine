import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import string
import nltk
from nltk.tokenize import TreebankWordTokenizer
from helper import ques
from nltk.stem.porter import PorterStemmer
STEMMER = PorterStemmer()
REMOVE_PUNCTUATION_TABLE = str.maketrans({x: None for x in string.punctuation})
TOKENIZER = TreebankWordTokenizer()


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def tokenize_and_stem(s):
    return [STEMMER.stem(t) for t in TOKENIZER.tokenize(s.translate(REMOVE_PUNCTUATION_TABLE))]

@app.route('/predict',methods=['POST'])
def predict():
    x=request.form['query']
    #cv=pickle.load(open('converting_matrix.pkl','rb'))
    #doc_vectors=pickle.load(open('doc_vectors.pkl','rb'))
    #ans=ques(x,cv,doc_vectors)
    ans=[]
    y={"link":"check",
       "text":"rakesh"
      }
    ans.append(y)
    return render_template('index.html', your_list=ans)

if __name__ == "__main__":
    app.run(debug=True)
