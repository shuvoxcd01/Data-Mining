# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 13:24:23 2017

@author: Falguni Das Shuvo
"""

import pandas as pd

from Node import Node,Leaf
from copy import deepcopy
from GiniIndex import Gini_Index



dt = None
path = raw_input("Enter path to 'training set' file: \n").rstrip('\n')
training_data = pd.read_excel(path, "Sheet1")
#trainingData = pd.read_excel("TestSet1.xlsx","Sheet1")
#training_data = pd.read_csv("Set2.csv")
#"initialization"

columns = training_data.columns.tolist()
_class = columns.pop()



def Generate_decision_tree(D, attribute_list, Attribute_selection_method = Gini_Index, binary = True, space = 0):
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
    N.label = "Value of " + str(best_splitting_attribute.keys().pop()) + " is in " + str(best_splitting_attribute.values().pop()) + " ?"
    print " "*space,"Node:",N.label
    #print "best_splitting_attribute -> ", best_splitting_attribute
    
    if not binary: #to be changed
        attribute_list.remove(best_splitting_attribute)
        
 #########################   
    p = D[best_splitting_attribute.keys().pop()]
    spliting_subset = best_splitting_attribute.values().pop()

    i_list = []
    neg_i_list = []
    
    for x in p:
        i_list.append(x in spliting_subset)
        neg_i_list.append(x not in spliting_subset)
        
    D1 = D[i_list]
    D2 = D[neg_i_list]  # to be changed    
    
 ########################   
    
   # for outcome in D[best_splitting_attribute.keys().pop()]:
    outcome = 'yes'
    print " "*space,"if yes then"
    Dj = D1
    if len(Dj) == 0:
        temp = Leaf()
        temp.label = max(D[_class])
        N.outcome[outcome] = temp
        
        print " "*space,"leaf:", temp.label
    else:
        N.outcome[outcome] = Generate_decision_tree(Dj, attribute_list[:], space = space) # Should '[:]' be here???
        
    outcome = 'no'
    print " "*space,"if no then"
    Dj = D2
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
        
    
    
    