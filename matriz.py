import math

A = [[1,-1,1],[2,2,3],[-2,-3,-1]]
B = [[1,0,4],[0,2,5],[1,3,0]]

C = [[[A[0][0]*B[0][0]],[A[0][1]*B[1][0]],[A[0][2]*B[2][0]]]]
C1= [C[0][0]+C[0][1]]
print(C)
print(C1)
