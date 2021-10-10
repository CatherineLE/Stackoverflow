from flask import Flask, render_template, request,jsonify
import pickle
import unidecode
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer,TfidfTransformer,CountVectorizer
import numpy as np
import cufflinks as cf
import re
from sklearn.preprocessing import MultiLabelBinarizer

app = Flask(__name__)



def nettoyage(texte):
    stop=pickle.load(open('stopwords.pkl', 'rb'))
    
    t=[]
    texte=str(texte)
    texte=unidecode.unidecode(texte).replace('\'',' ').replace('\n',' ')
    
    # Je ne garde que les éléments non numériques et sans les . ,
    p='([^0-9\'".,;]{1,})'
    for elem in re.findall(p,texte):
        for el in elem.split():
            if el.lower() in stop or len(el) < 3:
                continue
            else :
                t.append(el)
    return ' '.join(t)




@app.route("/")
def home():
    return render_template("index.html", title='Home')




@app.route("/result",methods=['GET', 'POST'])

    
def retour():
    user_text = request.form.get('input_text')
    
    user_text=nettoyage(user_text)

    pickled_pipeline=pickle.load(open('pipeline.pkl', 'rb')) 
    
    y_pred = pickled_pipeline.predict([user_text])
    
    mlb = pickle.load(open('MultiLabelBinarizer.pkl', 'rb'))
    tags = mlb.inverse_transform(y_pred)
    
    resp = tags[0]   #premier element de la liste = string

    return jsonify({'reponse':resp})
    #return {'reponse': resp}



#if __name__ == "__main__":
    #app.run(host='127.0.0.1', port=5000, debug=False)
    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)

