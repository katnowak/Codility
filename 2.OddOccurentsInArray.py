# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 22:18:14 2021

@author: Kasia
"""

def solution(A):
    
    N = len(A)

    if N >= 1 and N <= 1000000:
        for i in range(len(A)):
            if A[i] >= 1 and A[i] <= 1000000000:
                c = int(A.count(A[i]))

                if c%2 == 1:
                    return A[i]

    pass