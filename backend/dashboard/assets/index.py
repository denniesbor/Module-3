from dashboard.models import TrainDfLabels,Meals,Recipe

import pandas as pd
import re
import string
import numpy as np
import spacy
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.pipeline import Pipeline

from .text_cleaning import text_data_cleaning

# removing stopwords and tokenization using spacy 

class Search:
    def __init__(self,content,searched=None):
        self.content = content
        

#  nlp tasks

        
# read  meals, recipe and impt columns
meals = pd.DataFrame(Meals.objects.all().values())
recipe = pd.DataFrame(Recipe.objects.all().values())
df = pd.DataFrame(TrainDfLabels.objects.values_list('business_id','choice','stars_avg','sentiment','review_id','text','name'), \
    columns=['business_id','choice','stars_avg','sentiment','review_id','text','restaurant_name'])

def returnReviews(requests):
    
    #  read models
    # print(list(set(df.name.unique())))
    course_model= pickle.load(open('meal_model.sav', 'rb'))
    diet_model= pickle.load(open('diet_model.sav', 'rb'))
    cuisine_model= pickle.load(open('cuisine_model.sav', 'rb'))
     
    ## creating mapping from unique label texts to unique integers
    labelencoderCourse = LabelEncoder()
    labelencoderCourse.fit_transform(meals['Food_Category'])
    labelencoderDiet = LabelEncoder()
    labelencoderDiet.fit_transform(recipe['diet'])
    labelencoderCuisine = LabelEncoder()
    labelencoderCuisine.fit_transform(recipe['cuisine'])

    print(requests['content'])
    input_test= [requests['content']]
    #input_test =[input()]
    predm=course_model.predict(input_test) #classifies course or meal type
    predd=diet_model.predict(input_test) #classifies diet type
    predc=cuisine_model.predict(input_test) #classifies cuisine type

    #For output labels must be invers_transformed to words for matching to our restaurant database
    categories = list((labelencoderCourse.inverse_transform(predm)) + ',' + " "+ list(labelencoderDiet.inverse_transform(predd) + ',' + ' ' + labelencoderCuisine.inverse_transform(predc)))

    # regex to match all the categories
    base = r'^{}'
    expr = '(?=.*{})'
    words =categories[0].split(',')  # example
    pat = base.format(''.join(expr.format(w) for w in words))

    df_filter = df[df.choice.str.contains(pat=pat,flags=re.IGNORECASE, regex=True)]

    # regex to match some of the categories
    if df_filter.shape[0] < 1:
        pat = '|'.join(categories[0].split(','))
        df_filter = df[df.choice.str.contains(pat=pat,flags=re.IGNORECASE, regex=True)]

    
    df_pos = df_filter.query("stars_avg > 2 and sentiment > 5")
    df_pos = df_pos.sort_values(['sentiment','stars_avg'], ascending=False)
    unique_businesses = df_pos.restaurant_name.unique()[0:10]
    print(unique_businesses)
    # x=np.random.randint(len(unique_businesses), size=(5))
    # business_to_render = [unique_businesses[num] for num in x]
    data = []
    for business in unique_businesses:
        df_bus = df_pos[df_pos['restaurant_name']==business]
        bus_data = {
            "business_id":df_bus.iloc[0].restaurant_name,
            "stars_avg":df_bus.iloc[0].stars_avg,
            "sentiment_score":df_bus.iloc[0].sentiment,
            "reviews":[{"review_id":df_bus.iloc[i].review_id, "review":df_bus.iloc[i].text} for i,ind in enumerate(df_bus.index[0:5])]
        }

        data.append(bus_data)
      
    return {"content": data}
