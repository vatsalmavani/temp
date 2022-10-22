# LC: https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/
# solution: https://youtu.be/IDv9yvQN3Uc

# gives TLE
# need to implement binary search instead of O(n) search in the last for loop
# for i in prefixSum:
def max_sum_submatrix(matrix, k):
    row = len(matrix)
    col = len(matrix[0])

    for i in range(row):
        for j in range(1, col):
            matrix[i][j] += matrix[i][j-1]
    
    res = float('-inf')
    for c1 in range(col):
        for c2 in range(c1, col):
            summ = 0
            prefixSum = {0:1}   # set works just fine
            for r in range(row):
                summ += matrix[r][c2] - (matrix[r][c1-1] if c1 > 0 else 0)
                for i in prefixSum:
                    if summ - k <= i:
                        res = max(res, summ - i)
                prefixSum[summ] = prefixSum.get(summ, 0) + 1    # put prefixSum.add(summ) if prefixSum is a set
    return res

matrix = [[1,0,1],[0,-2,3]]
print(max_sum_submatrix(matrix, 2))
matrix = [[2,2,-1]]
print(max_sum_submatrix(matrix, 0))
# time complexity: O(m^2 * n^2)


##############################################################################

from bisect import bisect_left, insort


def max_sum_submatrix(matrix, k):
    row = len(matrix)   # m
    col = len(matrix[0])    # n

    # make sure rows > columns, otherwise we should rotate the matrix by zip() function
    if row < col:
        matrix = [list(i) for i in zip(*matrix)]    # O(m + n) time complexity
    row, col = max(row, col), min(row, col)

    for i in range(row):
        for j in range(1, col):
            matrix[i][j] += matrix[i][j-1]
    
    res = float('-inf')
    for c1 in range(col):
        for c2 in range(c1, col):
            summ = 0
            # prefixSum = {0:1}
            arr = [0, float('inf')]   # sorted array whose values are prefix sums
            for r in range(row):
                summ += matrix[r][c2] - (matrix[r][c1-1] if c1 > 0 else 0)
                # for i in prefixSum:
                #     if summ - k <= i:
                #         res = max(res, summ - i)
                idx = bisect_left(arr, summ - k)    # O(logn) time
                res = max(res, summ - arr[idx])
                # prefixSum[summ] = prefixSum.get(summ, 0) + 1
                if res == k: return k
                insort(arr, summ)
    return res

matrix = [[1,0,1],[0,-2,3]]
print(max_sum_submatrix(matrix, 2))
matrix = [[2,2,-1]]
print(max_sum_submatrix(matrix, 0))
# time complexity: O(n^2 * m * log(m))
# m,n = row, col

m = [[1,2,3], [4,5,6]]
transpose = [list(i) for i in zip(*m)]
transpose[0][1] += 50
print(transpose)