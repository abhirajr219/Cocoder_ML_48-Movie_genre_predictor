from fastapi import FastAPI

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
import pickle
import logging
from models import request_body
import wikipedia
import numpy as np
app=FastAPI(title="Movie Genre Preditor")

my_logger = logging.getLogger()
my_logger.setLevel(logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, filename='logs.log')


model=None

@app.on_event("startup")
def load_model():
  global model
  model=pickle.load(open("/content/drive/MyDrive/AI/movie1.pkl","rb"))
@app.get("/readroot")
async def Owners():
  return {"Owners ":"Jayalekshmi & Abhiraj"}

@app.post("/", tags=["prediction"])
async def get_prediction(iris: request_body):
    data=dict(iris)['data']  
    print(iris)
    try:
        try:
             plot=wikipedia.page(data[0][0]+" "+"movie").content[0:5500]
             print(plot,data)
        except: 
             plot=wikipedia.page(data[0][0]).content[0:5500]
             print(plot,data)
    
        def genre_prediction(sample_script):
              sample_script = re.sub(pattern='[^a-zA-Z]',repl=' ', string=sample_script)
              sample_script = sample_script.lower()
              sample_script_words = sample_script.split()
              sample_script_words = [word for word in sample_script_words if not word in set(stopwords.words('english'))]
              ps = PorterStemmer()
              final_script = [ps.stem(word) for word in sample_script_words]
              final_script = ' '.join(final_script)
              from sklearn.feature_extraction.text import CountVectorizer
              cv = CountVectorizer(max_features=300, ngram_range=(1,2))
              temp = cv.fit_transform([final_script]).toarray()
              return temp

        test_value=genre_prediction(plot)
        value=(model.predict(test_value))
        genre_mapper = {'other': 0, 'action': 1, 'adventure': 2, 'comedy':3,'drama':4, 'horror':5, 'romance':6, 'sci-fi':7, 'thriller': 8}

        return('Prediction: {}'.format(list(genre_mapper.keys())[value[0]]))
  
    except:
      
        return {"prediction": "Something went wrong in finding the movie!.Try giving more specific name of the movie/add word <Movie> to the Search data or try adding year!!!"}
