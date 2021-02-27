# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 15:26:19 2017

@author: Falguni Das Shuvo
"""

import pandas as pd   
import math
import itertools                                            

_class = 'Class'

df = pd.read_excel("Assesment3.xlsx", "Sheet1")

def Gini(df):
    s = df[_class]
    distinct_classes = s.unique().tolist()
    count_total = s.count()
    sum_of_probability_squared = 0
    
    for _eachClass in distinct_classes:
        count_specific_value = s[s == _eachClass].count()
        p = count_specific_value/float(count_total)
        sum_of_probability_squared = sum_of_probability_squared + (p * p)
        
    gini = 1 - sum_of_probability_squared
    
    return gini



def Get_All_Combinations(a):
    length = len(a)
    
    length = int(math.ceil(length/2.0))
    
    mega_list = []
    
    for r in range(1,(length+1))[:]:
        mega_list.extend(list(itertools.combinations(a,r)))
        
    
    #print mega_list
        
    return mega_list


def Select_from_Gini_of_Attribute(attribute, df):  # returns a dictionary containing a single element
    combination = Get_All_Combinations(df[attribute].unique().tolist())
    candidate_gini_list = []
    
    for spliting_subset in combination:
        i_list = []
        neg_i_list = []
        for x in df[attribute]:
            i_list.append(x in spliting_subset)
            neg_i_list.append(x not in spliting_subset)
            
        D1 = df[i_list]
        D2 = df[neg_i_list]  # to be changed
        temp = ((D1.shape[0]/float(df.shape[0])) * Gini(D1)) + ((D2.shape[0]/float(df.shape[0])) * Gini(D2)) 
        candidate_gini_list.append(temp)
        
        
    #print len(combination)
    #print len(candidate_gini_list)  
    
    t_list = [combination[:], candidate_gini_list[:]]
    print "Gini Index values of ", attribute
    for i in range(len(combination)):
        print t_list[0][i], "   ", t_list[1][i]
        
  
       
    
    attCombo_candidateGini_dict = dict(zip(candidate_gini_list, combination))
    
    #print attCombo_candidateGini_dict
    
    key = min(attCombo_candidateGini_dict.keys())
    value = attCombo_candidateGini_dict[key]
    
    return {key:value}


def Select_Best_Spliting_Criterion_Based_On_Gini_Index(df,attribute_list, __class,  _print = True):
    global _class
    _class = __class
    
    gini_index_dict = {}
    for _each_attribute in attribute_list:
        temp = Select_from_Gini_of_Attribute(_each_attribute, df.copy())
        #print temp.keys().pop() , "   ", temp[temp.keys().pop()] 
        gini_index_dict[temp.keys().pop()] = {_each_attribute : temp[temp.keys().pop()]}
        #gini_index_dict[_each_attribute] = temp
        
        
    print "Attributes and split criterion and their Gini Index Values: "    
    for key in gini_index_dict.keys():
        print gini_index_dict[key] , "    " , key
    
    key = min(gini_index_dict.keys())
    value = gini_index_dict[key]
    
    #print value
    
    return value

    
    
Gini_Index = Select_Best_Spliting_Criterion_Based_On_Gini_Index   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    