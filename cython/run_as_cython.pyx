cpdef int factorial(int n):
    cdef int ans
    ans = 1
    cdef int i
    for i in range(1, n + 1):
        ans *= i
    return ans
