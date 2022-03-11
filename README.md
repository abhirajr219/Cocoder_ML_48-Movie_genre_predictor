# Cocoder_ML_48-Movie_genre_predictor

#CONTENTS
-----------------------
1. Introduction
2. Requirements
3. Explaintion 
4. FAQS
5. Status
6. Acknowledgement

#INTRODUCTION 
----------------------
This ML project is to predict the genre of a movie by accepting its name, and based on the plot obtained using wikipedia module, the genre is displayed

#REQUIREMENTS
---------------------
These are the basic required modules in the project
1.numpy 
2.pandas 
3.matplotlib
4.seaborn
5.nltk
6.from nltk.corpus import stopwords
7.from nltk.stem.porter import PorterStemmer

In main.py, which is for the deployment' the following are installed
1.colabcode
2.wikipedia
3.pyngrok nest_asyncio 
4.fastapi 
5.uvicorn
6.sklearn
7.pydantic
8.from pyngrok import ngrok

#EXPLANATION
--------------------


FAQS
--------------------
1. Why is the accuracy rate so average?
   The prediction is efficient enough to give an accuary rate of approx 90 %. But during scraping the plot datas from wikipedia, we need to minimise the features in the training datasets. This happens since we use portstemmer for the plot exctracted. 
   
2. Can we deploy this using a permanent url in fastapi?
  Sure. We can deploy fastapi using Herku and many other platforms.
  
#STATUS
-----------------
It's completed till the deplyment using fastapi

#Acknowledgement
----------------
This project is done as a part of an event named Co-coder by Tinkerhub. It's a great opportunity to start with ML. 

