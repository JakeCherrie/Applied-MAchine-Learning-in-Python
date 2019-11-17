# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 13:50:59 2018

@author: Jake
"""

import pandas as pd
import numpy as np

# Vectors& Matracies
A = pd.DataFrame([[ 1,2,3],[4,5,6],[7,8,9],[10,11,12]])
V = pd.DataFrame([1,2,3])

M, n = A.shape

dim_A = A.shape

dim_V = V.shape

A_12 = A[1][2]

print(A)

# Vector and Matrix Operations

A = pd.DataFrame([[1,2,4],[5,3,2]])
B = pd.DataFrame([[1,3,4],[1,1,1]])

s = 2

add_AB = A + B

sub_AB = A - B

mult_As = A * s

div_As = A / s

add_As = A + s

dot_AB = A.dot(B.transpose())

# Multiplying house sizes by the function -40 +0.25x

hse_sze = pd.DataFrame([[1,1,1,1],[2104,1416,1534,852]]).transpose()

fnc_vec = pd.DataFrame([-40,0.25])

prd = hse_sze.dot(fnc_vec)

A = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])

v = pd.DataFrame([[1],[1],[1]])

Av = A.dot(v)

A = pd.DataFrame([[1,2],[3,4],[5,6]])

B = pd.DataFrame([[1],[2]])

mult_AB = A.dot(B)


A = pd.DataFrame([[1,2,0],[0,5,6],[7,0,9]])

# Using numpy for the inverse
A_inv = np.linalg.inv(A.values)

A = np.matrix([[1,2,0],[0,5,6],[7,0,9]])

x1 = np.array([89, 72, 94, 69])

(89-x1.mean())/(x1.ptp())

