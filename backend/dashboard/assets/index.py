from dashboard.models import TrainDfLabels
import pandas as pd
import numpy as np
import pickle
import string
import spacy

# removing stopwords and tokenization using spacy 

punct = string.punctuation

import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')
from spacy.lang.en.stop_words import STOP_WORDS
stopwords = list(STOP_WORDS)


class Search:
    def __init__(self,content,searched=None):
        self.content = content

def returnReviews(requests):
    
    mvpdf = pd.DataFrame(TrainDfLabels.objects.all().values())
    df_pos = mvpdf.query("stars_avg > 3 and sentiment_score > 0.5")
    unique_businesses = df_pos.business_id.unique()
    x=np.random.randint(len(unique_businesses), size=(5))
    business_to_render = [unique_businesses[num] for num in x]

    data = []
    for business in business_to_render:
        df_bus = mvpdf.query("business_id == @business")
        index = df_bus.index[0]
        bus_data = {
            "business_id":df_bus.iloc[0].business_id,
            "stars_avg":np.around(df_bus.iloc[0].stars_avg,decimals=2),
            "sentiment_score":np.around(df_bus.iloc[0].sentiment_score,decimals=2),
            "reviews":[{"review_id":mvpdf.iloc[i].review_id, "review":mvpdf.iloc[i].text} for i in df_bus.index[0:5]]
        }

        data.append(bus_data)
    
    return {"content": data}