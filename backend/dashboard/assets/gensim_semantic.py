import pickle
import gensim
import numpy as np
import pandas as pd
from gensim import corpora
from operator import itemgetter

#generate a similarity matrix
from gensim.similarities import MatrixSimilarity
from .text_cleaning import text_data_cleaning

# tokenizer
tokenizer = text_data_cleaning

#load indexed corpus
tfidf_corpus = gensim.corpora.MmCorpus('tfidf_model_mm')
lsi_corpus = gensim.corpora.MmCorpus('lsi_model_mm')

tfidf_model= pickle.load(open('tfidf_model.sav', 'rb'))
lsi_model= pickle.load(open('lsi_model.sav', 'rb'))

dictionary = gensim.corpora.Dictionary.load('categories.dict')
business_index = MatrixSimilarity(lsi_corpus, num_features = lsi_corpus.num_terms)

# models
from dashboard.models import BusinessRestaurants,Reviews


def return_reviews(businesses):
    '''This function will return the dataframe of the most 
    relevant restaurants based on the semantic search   
    '''
    q = Reviews.objects.filter(business__in=businesses)\
        .select_related('business').order_by('-business__stars_avg','-business__sentiment','-review_stars').values_list('business_id','review_id','business__stars_avg','business__sentiment','text','business__name')
    
    columns=['business_id','review_id','stars_avg','sentiment','text','restaurant_name']
    df = pd.DataFrame(q, columns=columns)
    
    return df

resto = pd.DataFrame(BusinessRestaurants.objects.values_list('business_id','categories_mod'), \
    columns=['business_id','categories_mod'])

# split categories as a list of tokens
resto['categories_mod'] = resto['categories_mod'].apply(lambda x: x.split(' '))

def search_similar(search_term):
    
    print(search_term)
    
    query_bow = dictionary.doc2bow(tokenizer(search_term))
    query_tfidf = tfidf_model[query_bow]
    query_lsi = lsi_model[query_tfidf]

    business_index.num_best = 50 #get the 50 most similar categories to our query
    business_list = business_index[query_lsi]

    business_list.sort(key=itemgetter(1), reverse=True)
    business_names = []

    for j, business in enumerate(business_list):

        # business_names.append (
        #     {
        #         'Relevance': round((business[1] * 100),2),
        #         'business_id': resto['business_id'][business[0]],
        #         'categories': resto['categories_mod'][business[0]]
        #     }

        # )
        business_names.append(resto['business_id'][business[0]])
        if j == (business_index.num_best-1):
            break
   
    names = business_names[:10]
    
    return names, return_reviews(names)