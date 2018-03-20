# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 16:58:00 2018

@author: HeLi
"""

import numpy as np

def train(X_train, y_train):
      #transform X_trian and y_train to np.array
      X_train = np.array(X_train)
      y_train = np.array(y_train)
      
      #intialize the variables
      max_iter_times = 1000
      iter_times = 0
      alpha = np.array([0, 0, 0])
      b = 0
      eta = 1
      len_X = len(X_train)
      
      #calculate the Gram matrix
      G = []
      for i in range(len_X):
            for j in range(len_X):
                  G.append(X_train[i].dot(X_train[j]))
                  
      G = np.array(G).reshape(len_X, len_X)
      
      #the main algorithm
      while iter_times <= max_iter_times:
            for i in range(len_X):
                  tmp = b
                  for j in range(len_X):
                        tmp += alpha[j] * y_train[j] * G[j][i]
                  if y_train[i]*tmp <= 0:
                        alpha[i] = alpha[i] + eta
                        b = b + eta*y_train[i]
                        iter_times += 1
                        print('alpha=',alpha,' b=',b,' x=',i, sep='')
                        break
            else:
                  break
                  
X_train = [[3, 3], [4, 3], [1, 1]]
y_train = [1, 1, -1]
train(X_train, y_train)