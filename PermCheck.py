# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 14:48:08 2021

@author: Kasia
"""

def solution(A):
    N = len(A)

    for i in range(N):
        if i in A:

            return 1
        
        elif i not in A:
            return 0

        else:
            return 0

    pass