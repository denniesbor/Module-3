import pandas as pd
import re
import string
import numpy as np
import spacy
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.pipeline import Pipeline
# models
from dashboard.models import TrainDfLabels
# expanded tokens
from .expanded_nltk import expanded
# gensim models
from .gensim_semantic import search_similar


# main df
df = pd.DataFrame(TrainDfLabels.objects.values_list('business_id','choice','stars_avg','sentiment','review_id','text','name','latitude','longitude'), \
    columns=['business_id','choice','stars_avg','sentiment','review_id','text','restaurant_name','latitude','longitude'])


def returnReviews(requests):
   
    #For output labels must be invers_transformed to words for matching to our restaurant database
    categories = expanded(requests['content'])
    
    business_ids,df_ = search_similar(' '.join(categories))

    # unique_businesses = df_.restaurant_name.unique()
    
    data = []
    for business_id in business_ids:
        df_bus = df_[df_['business_id']==business_id]
        bus_data = {
            "business_id":df_bus.iloc[0].business_id,
            "restaurant_name":df_bus.iloc[0].restaurant_name,
            "stars_avg":df_bus.iloc[0].stars_avg,
            "sentiment_score":df_bus.iloc[0].sentiment,
            "reviews":[{"review_id":df_bus.iloc[i].review_id, "review":df_bus.iloc[i].text} for i,ind in enumerate(df_bus.index[0:5])]
        }

        data.append(bus_data)
      
    return {"content": data, "search": ' '.join(categories)}

