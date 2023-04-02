def solution(A):
    N = len(A)

    if N < 0:
        return 0

    elif N == 1:
        return 1

    else:
        dist_values = []

        for i in range(1, N -1):
            if A[i] < -1000000 or A[i] > 1000000:
                break

        for j in range(1, N):
            number = A.count(j)
            dist_values.append(number)
            j += 1

        max_value = max(dist_values)

        for k in range(1, N):
            if A[k] != max_value:
                k += 1
            else:
                result = k - 1


    return result


    pass