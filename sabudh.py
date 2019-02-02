# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 12:40:34 2019

@author: PANKUSH
"""

from flask import Flask,request,jsonify
import pandas as pd
a=pd.read_csv("app1.csv")
#a.__delitem__("Unnamed: 0")
print(a)
list1=a.to_dict("records")
print(list1)
ob=Flask(__name__)
@ob.route("/",methods=["Get"])
def get():
    return jsonify({"dataframe":list1})
@ob.route("/post",methods=["Post"])
def posting():
    user=request.get_json()
    dict1={}
    dict1["index"]=list1[-1]["index"]+1
    dict1.update(user)
    list1.append(dict1)
    a=pd.DataFrame(list1)
    a.to_csv(r"app1.csv",header=True,index=None)
    return jsonify({"index":dict1["index"]})
@ob.route("/put",methods=["PUT"])
def puting():
    user=request.get_json()
    a.loc[a["index"]==user["index"],["Name","RollNO.","class"]]=user["Name"],user["RollNO."],user["class"]
    a.to_csv("app1.csv",header=True,index=None)
    return jsonify({"index":user["index"]})
@ob.route("/delete",methods=["DELETE"])
def deleting():
    user=request.get_json()
    new_df=a[a["index"]!=user["index"]]
    new_df.to_csv("app1.csv",header=True,index=None)
    return jsonify({"index":user["index"]})
ob.run(port=2002)
                  
    
ob.run(port=2001) 
   
    
    