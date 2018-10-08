'''
Given a NxN image ( 2D Matrix )
Rotate the image by 90 degrees (clockwise).

I/p

[ [1, 2], [3, 4] ]

o/p

[ [3, 1], [4, 2] ]
'''

def rotate_matrix(arr):
    n = len(arr)
    arr.reverse()
    op = []
    for i in range(0, n):
        row = []
        for a in arr:
            row.append(a[i])
        op.append(row)
    return op
	
a = [[1,2],[3,4]]
b = [[1,2,3],[4,5,6],[7,8,9]]


print rotate_matrix(a)

print rotate_matrix(b)