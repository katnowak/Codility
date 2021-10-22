def solution(X, A):
    for i in range(len(A)):
        if A[i] == X:
            return i
        elif max(A) < X:
            return -1
    
    pass