# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 12:31:26 2017

@author: Falguni Das Shuvo
"""
from math import log

_class = None

def  Entropy(df):
    s = df[_class]
    distinct_classes = s.unique().tolist()
    count_total = s.count()
    entropy = 0
    
    for _eachClass in distinct_classes:
        count_specific_value = s[s == _eachClass].count()
        p = count_specific_value/float(count_total)
        entropy = entropy - (p * log(p, 2))
    return entropy

def ExpectedInformationRequiredAfterPartition(df, by):
    distinct_attribute_values = df[by].unique().tolist()
    entropyAfterPartition = 0
    tupleNo,attributeNo = df.shape
    #print tupleNo
    
    for _eachValue in distinct_attribute_values:
        partition = df[df[by] == _eachValue]
        s = df[by]
        entropyAfterPartition = entropyAfterPartition + ((s[s==_eachValue].count()/float(tupleNo)) * Entropy(partition))
    return entropyAfterPartition

EntropyAfterPartition = ExpectedInformationRequiredAfterPartition

def Gain(df, attribute):
    return Entropy(df) - EntropyAfterPartition(df, attribute)



#gain_list = []z
def InformationGain(df,attribute_list, __class,  _print = True):
    global _class
    _class = __class
    gain_list = []
    for _each_attribute in attribute_list:
        gain_list.append(Gain(df, _each_attribute))
    
    attribute_and_gain_dict = dict(zip(gain_list,attribute_list))
    if _print:
       for key in attribute_and_gain_dict.keys():
           print "[Attribute:", attribute_and_gain_dict[key], " I.G.:", key, "]    ",
       print 
    return attribute_and_gain_dict[max(attribute_and_gain_dict.keys())]

