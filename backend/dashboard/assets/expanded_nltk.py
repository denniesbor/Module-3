import nltk
from nltk.corpus import wordnet
import pandas as pd
import re
import string
import numpy as np
import spacy
import pickle
from sklearn.preprocessing import LabelEncoder

# models
from dashboard.models import TrainDfLabels,Meals,Recipe

# import tokenizer
from .text_cleaning import text_data_cleaning
# nlt

# read  meals, recipe and impt columns
meals = pd.DataFrame(Meals.objects.all().values())
recipe = pd.DataFrame(Recipe.objects.all().values())
df = pd.DataFrame(TrainDfLabels.objects.values_list('business_id','choice','stars_avg','sentiment','review_id','text','name','latitude','longitude'), \
    columns=['business_id','choice','stars_avg','sentiment','review_id','text','restaurant_name','latitude','longitude'])

# load models

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


def expanded(inp):

    inpt = text_data_cleaning(' '.join(inp)) #tokenise input

    inputs=[]
    for i in inpt:
        for synset in wordnet.synsets(i):
            for lem in synset.lemmas():
                #input_n.append(lem.name())
                inputs.append(lem.name()) 
    #input_test= [','.join(inputs)]
    input_test= [','.join(inputs)]

    #  load models

    predm=course_model.predict(input_test) #classifies course or meal type
    predd=diet_model.predict(input_test) #classifies diet type
    predc=cuisine_model.predict(input_test) #classifies cuisine type

    #labels must be inverse_transformed to words for matching to our restaurant database
    categories = [' '.join(labelencoderCourse.inverse_transform(predm)), ''.join(labelencoderDiet.inverse_transform(predd)), ''.join(labelencoderCuisine.inverse_transform(predc))] 

    expand =[]
    for cat in categories:
        print(cat)
        for synset in wordnet.synsets(cat):
            for l in synset.lemmas():
                expand.append(l.name())
    return list(set(expand))