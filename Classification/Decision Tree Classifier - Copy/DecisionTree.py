# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 13:24:23 2017

@author: Falguni Das Shuvo
"""

import pandas as pd

from Node import Node,Leaf
from copy import deepcopy
from InformationGain import InformationGain



dt = None
path = raw_input("Enter path to 'training set' file: \n").rstrip('\n')
training_data = pd.read_excel(path, "Sheet1")
#trainingData = pd.read_excel("TestSet1.xlsx","Sheet1")
#training_data = pd.read_csv("Set2.csv")
#"initialization"

columns = training_data.columns.tolist()
_class = columns.pop()



def Generate_decision_tree(D, attribute_list, Attribute_selection_method = InformationGain, binary = False, space = 0):
    space = space + 4
    N = Node()
    if len(D[_class].unique()) == 1:
        N = Leaf()
        N.label = D[_class].unique()
        print " "*space, "leaf:", N.label
        return N
    if len(attribute_list) == 0:
        N = Leaf()
        N.label = max(D[_class])
        print " "*space,"leaf:",N.label
        return N
    best_splitting_attribute = Attribute_selection_method(D, attribute_list[:], __class = _class)
    #print "attribute list -> ", attribute_list
    N.label = best_splitting_attribute
    print " "*space,"Node:",N.label
    #print "best_splitting_attribute -> ", best_splitting_attribute
    
    if not binary: #to be changed
        attribute_list.remove(best_splitting_attribute)
        
    for outcome in D[best_splitting_attribute].unique():
        print " "*space,"if ", best_splitting_attribute, " == ", outcome, " then"
        Dj = D[D[best_splitting_attribute] == outcome]
        if len(Dj) == 0:
            temp = Leaf()
            temp.label = max(D[_class])
            N.outcome[outcome] = temp
            
            print " "*space,"leaf:", temp.label
        else:
            N.outcome[outcome] = Generate_decision_tree(Dj, attribute_list[:], space = space) # Should '[:]' be here???
    return N
        


        
def Classify():
    
    
   
    #_class = "class"
    #attrl = trainingData.columns.delete(trainingData.columns.get_loc(_class)).tolist()
    
    dt = Generate_decision_tree(training_data,columns[:])
    

def Predict():
    query = raw_input("Enter query:  \n")
    query = query.rsplit(' ')
    
    test_attributes = dict(zip(columns, query))
    
    n = deepcopy(dt)
    
    while True:
        if isinstance(n,Leaf):
            print n.label
            break
        elif isinstance(n, Node):
            n = n.outcome[test_attributes[n.label]]
        else:
            print Error
        
    
    
    