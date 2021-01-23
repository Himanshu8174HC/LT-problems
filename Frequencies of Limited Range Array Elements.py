def frequencycount(A,N):
    # code here
    d = {}
    for i in A:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in range(1,N + 1):
        if i in d:
            A[i - 1] = d[i]
        else:
            A[i - 1] = 0
