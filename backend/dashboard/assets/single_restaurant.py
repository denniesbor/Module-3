from dashboard.models import Reviews
import pandas as pd

def return_rest(business_id):
    
    q = Reviews.objects.filter(business=business_id)\
        .select_related('business').order_by('business_id','-review_stars').\
            values_list('business_id','review_id','business__stars_avg',\
                'business__sentiment','text','business__name','business__city','business__latitude','business__longitude')

    columns=['business_id','review_id','stars_avg','sentiment','text','restaurant_name','city','latitude','longitude']
    df = pd.DataFrame(q, columns=columns)
    
    try:
        bus_data = {
                "business_id":df.iloc[0].business_id,
                "restaurant_name":df.iloc[0].restaurant_name,
                "stars_avg":df.iloc[0].stars_avg,
                "sentiment_score":df.iloc[0].sentiment,
                "location":{'city':df.iloc[0].city,'latitude':df.iloc[0].latitude,'longitude':df.iloc[0].longitude},
                "reviews":[{"review_id":df.iloc[i].review_id, "review":df.iloc[i].text} for i,ind in enumerate(df.index[0:5])]
            }
    except:
        bus_data = {
            
        }
    return {"content": bus_data}