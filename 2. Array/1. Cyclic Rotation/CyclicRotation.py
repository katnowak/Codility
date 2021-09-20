# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 19:37:25 2021

@author: Kasia
"""

def solution(A, K):
    
    if len(A)==K:
        return A   
    
    retArray = []

    for i in range (K-1,len(A)):
        retArray.append(A[i])


    for i in range (0,K-1):
        retArray.append(A[i])

     
    return retArray

if(solution([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]):
    print("OK")
else:
    print(":c")
    
if(solution([0, 0, 0], 2) == [0, 0, 0]):
    print("OK")
else:
    print(":c")
    
if(solution([1, 2, 3, 4], 4) == [1, 2, 3, 4]):
    print("OK")
else:
    print(":c")