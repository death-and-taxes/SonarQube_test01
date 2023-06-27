'''
Author: Dylan Crites
Class: CSC 252 w/ David Claveau
Description: This program creates two matrixes and then multiplies together
then it prints the result.
'''

def matrixMulitiplication(m1, m2):

#creates empty matrix, x is equivalent to p, y is equivlant to m
    mf =[[0 for x in range(len(m2[0]))] for y in range(len(m1))]

#3 nested for loops to fill in the empty mf, variable names are
# based on the mxn + nxp = mxp equation
    for m in range(len(m1)):
        for p in range(len(m2[0])): 
            for n in range(len(m2)):
                #result
                mf[m][p] += m1[m][n] * m2[n][p]
    return mf
    
 
m1= [1]
m2 = [[2],[3]]


print (matrixMulitiplication(m1, m2))
