from dashboard.models import Meals
import itertools

def get_data():
    meals = list(set(Meals.objects.values_list('Food_Category')))
    meal_data = list(itertools.chain(*meals))
  
    # data = ['Extra virgin olive oil','Garlic','Pasta sauce','Oregano','Capers','Basil']
    
    return {"available_food":meal_data}

