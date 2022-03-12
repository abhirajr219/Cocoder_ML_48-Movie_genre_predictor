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
1. numpy 
2. pandas 
3. matplotlib
4. seaborn
5. nltk
6. from nltk.corpus import stopwords
7. from nltk.stem.porter import PorterStemmer

In main.py, which is for the deployment' the following are installed
1. colabcode
2. wikipedia
3. pyngrok nest_asyncio 
4. fastapi 
5. uvicorn
6. sklearn
7. pydantic
8. from pyngrok import ngrok

#EXPLANATION
--------------------
A summarised idea is discussed here :
1. Necassary dataset is downloaded
2. Different genres are represented as a dictonary : genre_mapper = {'other': 0, 'action': 1, 'adventure': 2, 'comedy':3,'drama':4, 'horror':5, 'romance':6, 'sci-fi':7, 'thriller': 8}
3.  corpus list is declared 
4.  portstemmer is called and the following steps are performed:<br/> a. Cleaning special character from the dialog/script<br/> b.Converting the entire dialog/script into lower case<br/> c. Tokenizing the dialog/script by words<br/> d. Removing the stop words<br/> e. Stemming the words<br/> f. Joining the stemmed words<br/> g. Creating a corpus
5. Datas for training and testing are splited using train_test_split
6. from sklearn.naive_bayes import MultinomialNB
7. Converting to a pickle file 
8. In main.py, from pyngrok import ngrok and necessary modules as said in required section
9. Install fastapi
10. Prediction is done as post request
11. In a function, usoing countVectoriser the plot obtained from wikipedia is cleaned using stopwords
12. Corresponding prediction is return as per the genre_mapper

                
#FAQS
--------------------
1. Why is the accuracy rate so average?
<br/>   The prediction is efficient enough to give an accuary rate of approx 90 %. But during scraping the plot datas from wikipedia, we need to minimise the features in the training datasets. This happens since we use portstemmer for the plot exctracted. 
   
2. Can we deploy this using a permanent url in fastapi?
 <br/>  Sure. We can deploy fastapi using Herku and many other platforms.
  
#STATUS
-----------------
It's completed till the deplyment using fastapi

#ACKNOWLEDGEMENT
----------------
This project is done as a part of an event named Co-coder by Tinkerhub. It's a great opportunity to start with ML. 

