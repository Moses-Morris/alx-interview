#!/usr/bin/python3
'''
Pascal's Triangle
'''


def pascal_triangle(n):
    '''
    returns a list of lists of integers representing
    the Pascal’s triangle of n:
    ****Returns an empty list if n <= 0
    '''
    triangle = []
    if n <= 0:
        return triangle
    triangle = [[1]]
    for i in range(1, n):
        tmpT = [1]
        for j in range(len(triangle[i - 1]) - 1):
            current = triangle[i - 1]
            tmpT.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
        tmpT.append(1)
        triangle.append(tmpT)
    return triangle
