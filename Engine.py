import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
import math
import pickle
import json

class RecommendationEngine :
    dataset_filename = 'Datasets/restaurants.xls'
    recommendation_name = 'menu item'
    
    def __init__(self, item, n, recommendation_name):
        self.item = item
        self.n = n
        self.recommendation_name = recommendation_name

    def set_Dataset_Filename(self, file):
        self.dataset_filename = file
        
    def getDistanceList(self, combined, x, y):
        distances = []
        n = len(combined[0])
        for i in range (n):
            d = math.sqrt((combined[1][i] - x)**2 + (combined[2][i] - y)**2)
            pair = [combined[0][i], d]
            distances.append(pair)
        distances.sort(key=lambda x: x[1])
        l = []
        for i in range (self.n) :
            ID = int(distances[i][0])
            l.append(ID)
        return l
    
    def run (self):
   
        '''
        # loading the data into lists
        df = pd.read_excel(self.dataset_filename)
        ids = df['id']
        longitudes = df['longitude']
        latitudes = df['latitude']
        combined = []
        combined.append(ids)
        combined.append(longitudes)
        combined.append(latitudes)
        with open('saved-geolocations.pkl', 'wb') as f:
            pickle.dump(combined, f) 
       '''
        with open('saved-geolocations.pkl', 'rb') as f:
            combined = pickle.load(f)
        
        #Get the top nearest N items
        d = self.getDistanceList(combined, self.item[0] , self.item[1])
        #print(nearestN)
        jsonData =  {
            'type' : 'nearby-restaurants',
            'IDs' : d
        }
        jsonStr = json.dumps(jsonData)
        return jsonStr

        











        
        
