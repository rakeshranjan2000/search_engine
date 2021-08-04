import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import string
import nltk
from nltk.tokenize import TreebankWordTokenizer
from helper import ques,tokenize_and_stem
from nltk.stem.porter import PorterStemmer

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    x=request.form['query']
    cv=pickle.load(open('converting_matrix.pkl','rb'))
    doc_vectors=pickle.load(open('doc_vectors.pkl','rb'))
    ans=ques(x,cv,doc_vectors)
    return render_template('index.html', your_list=ans)

if __name__ == "__main__":
    app.run(debug=True)
