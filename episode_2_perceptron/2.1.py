# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 11:37:08 2018

@author: HeLi
"""

"""
Perceptron
"""

import numpy as np

def train(X_train, y_train):
      #initial w, b, eta, max_train_times
      w = np.array([0, 0])
      b = 0
      eta = 1
      max_iter_times = 1000
      iter_times = 0
      
      while iter_times <= max_iter_times:
            for x, y in zip(X_train, y_train):
                  x = np.array(x)
                  tmp = y * (np.dot(w, np.transpose(x)) + b)
                  if tmp <= 0:
                        break
            else:
                  break
            
            w = np.add(w, np.multiply(eta*y, x))
            b = b + eta*y
            iter_times += 1
            print('w=',w,' b=',b,' x=',x, sep='')
            
      return

X_train = [[4, 3], [3, 3], [1, 1]]
y_train = [1, -1, -1]
train(X_train, y_train)
                  
      