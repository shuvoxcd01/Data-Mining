# -*- coding: utf-8 -*-
"""
Created on Fri Oct 06 09:35:20 2017

@author: Falguni Das Shuvo
"""

#import numpy as np
import pandas as pd
#from matplotlib import pyplot as plt


def P(attribute, value, given_attribute = None, given_value = None):
    "probability function"
    
    if given_attribute == None and given_value == None:
        s = training_data[attribute]
        count_total = s.count()
        count_specific_value = s[s == value].count()
        return count_specific_value/float(count_total)
    else:
        df = training_data[training_data[given_attribute] == given_value]
        count_total = df[given_attribute].count()
        count_specific_value = df[df[attribute] == value][attribute].count()
        return count_specific_value/float(count_total)
    

path = raw_input("Enter path to 'training set' file: \n").rstrip('\n')
training_data = pd.read_excel(path, "Sheet1")

#"initialization"
columns = training_data.columns.tolist()
_class = columns.pop()

_probability_collection_dict_main = {}

for value in training_data[_class].unique():
    _probability_collection_dict_main[value] = P(_class,value)
        


def predict():
    query = raw_input("Enter query:  \n")
    query = query.rsplit(' ')
    
    _attributes = dict(zip(columns, query))
    
    _probability_collection_dict = _probability_collection_dict_main.copy()    
    
    for keyP in _probability_collection_dict.keys():
        for keyA in _attributes:
            _probability_collection_dict[keyP] = _probability_collection_dict[keyP] * P(keyA, _attributes[keyA], _class, keyP)
        
    for key in _probability_collection_dict.keys():
        if _probability_collection_dict[key] == max(_probability_collection_dict.values()):
            prediction = key
        
    print "Prediction : " , prediction
    
    for key in _probability_collection_dict.keys():
       print key, "  ", _probability_collection_dict[key]




    

    

