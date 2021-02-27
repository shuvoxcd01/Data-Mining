import numpy as np
import pandas as pd
from math import sqrt

training_data = pd.read_excel("Assesment2.xlsx","Sheet1")



def detect_attr_type(attr):
    _type = training_data[attr].dtype 
    if str(_type)[0:5] == 'float' or str(_type)[0:3] == 'int':
        return 'numeric'
    elif _type == 'object':
        return 'nominal'
    else:
        return None
    

def euclidean_distance(tuple1, test_tuple):
    #here, tuples are assumed to be of type pandas.Series
    
    distance = 0
    
    tuple1 = tuple1.drop(tuple1.index[len(tuple1)-1])
    attr_type_record = []
    for attr in tuple1.index:
        attr_type_record.append(detect_attr_type(attr))
    
    if None in attr_type_record:
        return "unknown attribute type detected"
    
    i = 0
    
    if len(tuple1) != len(test_tuple):
        return "length didn't match"
    
    while i < len(tuple1):
        x,y = tuple1[i],test_tuple[i]
        if attr_type_record[i] == 'numeric':
            single_distance = x - y
            single_distance = single_distance * single_distance
            distance = distance + single_distance
            
        elif attr_type_record[i] == 'nominal':
            if x == y:
                distance = distance + 1
            # no need to write else: distance = distance + 0
        else:
            pass
        i = i + 1
    
        distance = sqrt(distance)
        return distance
    
    
def min_max_normalization():
    pass
 
test_tuple = [9.1, 11.0]  

#path = raw_input("Enter path to 'training set' file: \n").rstrip('\n')
#training_data = pd.read_excel(path, "Sheet1")

#"initialization"
columns = training_data.columns.tolist()
_class = columns.pop()

def predict():
    
    k = 5
    
    distance = []
    
    for index in training_data.index:
        distance.append(euclidean_distance(training_data.loc[index], test_tuple));
    
    distance_class_matrix =pd.DataFrame(zip(distance, training_data[_class].tolist()), columns = ["distance", "class"])
    distance_class_matrix.sort_values(by = 'distance', inplace = True)
    
    print distance_class_matrix.head(k)
    
    prediction = distance_class_matrix['class'][:k].mode()
    
    print "prediction is : " , prediction
    
    
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    