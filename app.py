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
    ans=ques(x)
    return render_template('index.html', your_list=ans)

if __name__ == "__main__":
    app.run(debug=True)
