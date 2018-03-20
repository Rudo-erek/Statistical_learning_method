# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 20:32:20 2018

@author: Rudo-erek
"""
import math as mt
import numpy as np

      
def Construct_KDTree(X_train, k, d):
      #initialize the variables
      X_left = []  #the branch of the left child node
      X_right = []  #the branch of the right child node 
      X = X_train
      
      if len(X) == 0: return  #the node has no samples
      
      l = d % k  #select the l-th axis as the split axis
      X = np.array(sorted(X, key=lambda x: x[l]))  #sort the samples by the l-th axis
      
      #split the left and right child zooms by the middle point
      mid = mt.floor(len(X)/2)
      KDT.append(X[mid])
      
      i = mid - 1
      while i>=0 and X[i][l] == X[mid][l]:
            i -= 1
      if i>=0:
            X_left = X[0:(i+1),0:k+1]
      Construct_KDTree(X_left, k, d+1)
      
      i = mid + 1
      while i<=len(X)-1 and X[i][l] == X[mid][l]:
            i += 1
      if i<=len(X)-1:
            X_right = X[i:len(X),0:k+1]      
      Construct_KDTree(X_right, k, d+1)


KDT = []  #save the result of the kd-Tree
X_train = np.array([[8, 1], [7, 2], [2, 3], [5, 4], [9, 6], [4, 7]]) #the train samples
k = int(X_train.size / len(X_train))  #the number of the train samples
Construct_KDTree(X_train, k, 0)  #construct the kd-Tree
