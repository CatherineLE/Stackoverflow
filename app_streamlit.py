#https://github.com/jalalmansoori19/Classfiying-Iris-flower-species/blob/master/requirements.txt
'''>python -m venv env
   > env\scripts\activate
   >python   .py
   >streamlit run .py
'''

import streamlit as st
import os

from flask import jsonify 
import pickle
import unidecode
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer,TfidfTransformer,CountVectorizer
import numpy as np
import re
from sklearn.preprocessing import MultiLabelBinarizer



mlb = pickle.load(open('MultiLabelBinarizer.pkl', 'rb'))
pipeline=pickle.load(open('pipeline.pkl', 'rb')) 


    
def nettoyage(texte):
    stop=pickle.load(open('stopwords.pkl', 'rb'))
    
    t=[]
    texte=str(texte)
    texte=unidecode.unidecode(texte).replace('\'',' ').replace('\n',' ')
    
    # Je ne garde que les éléments non numériques et sans les . ,
    p='([^0-9\'".,;]{1,})'
    for elem in re.findall(p,texte):
        for el in elem.split():
            if el.lower() in stop or len(el) < 1:
                continue
            else :
                t.append(el)
    return ' '.join(t)



st.title('Questions Tags')
st.header("Multi-Labels Classification Tool")
st.subheader("Enter the statement that you want to tag")



user_text = st.text_input('Exemple :  possible print variable type standard cplusplus, access url cookie use socket, scrollview ignore child layout_height, cplusplus ide linux')
user_text = nettoyage(user_text)

if st.button('Predict') :

    y_pred = pipeline.predict([user_text])
    tags = mlb.inverse_transform(y_pred)
    #tuple to list
    resp = [', '.join(map(str, x)) for x in tags] 
    #resp = jsonify({'reponse':resp})  #ne pas mettre en json car sinon il faudra app.app_context() 
    st.write('Topics  :  {}'.format(resp)) 

    


    


