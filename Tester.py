from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
#from nltk.tokenize import word_tokenize
from nltk import pos_tag
import pandas as pd

import wordninja

from nltk.corpus import stopwords
stopword=set(stopwords.words('english'))


xtrain=pd.read_csv("xtrain.csv")
xtest=pd.read_csv("xtest.csv")


model=""
with open("anomalyModel3.pkl","rb") as f:
    model=pickle.load(f)


vectorize=TfidfVectorizer()
vectorize.fit_transform(xtrain['keyWords'])
vectorize.transform(xtest['keyWords'])

def checkLink(u_link):
    rej=[':','PRP$','PRP','FW','IN','DT','CD','TO','SYM','CC','WRB','WP','WP$','WDT','WDT','RB']
    lnk=" "

    if(u_link[-1]=="/"):
        u_link=u_link[:-1]
    
    link=u_link.split("/")[-1]
    kWords=wordninja.split(link)
    
    #link=link.split("-")
    tag_words=pos_tag(kWords)
    
    for (word,pos) in tag_words:
        if (pos not in rej) and (word not in stopword):
            lnk+=word+" "
    
    data={"text":[lnk]}
    test_str=vectorize.transform(data['text'])
    res=model.predict(test_str)
    return res[0]