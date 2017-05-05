import string
import numpy as np
import matplotlib.pyplot as plt

line=raw_input('Input the r1:').split()
r1=[]
for i in range(len(line)):
    r1.append(string.atof(line[i]))

line=raw_input('Input the r2:').split()
r2=[]
for i in range(len(line)):
    r2.append(string.atof(line[i]))
line=raw_input('Input the r3:').split()
r3=[]
for i in range(len(line)):
    r3.append(string.atof(line[i]))

line=raw_input('Input the r4:').split()
r4=[]
for i in range(len(line)):
    r4.append(string.atof(line[i]))

def minus(ra,rb):
    rab=[]
    for i in range(len(ra)):
        rab.append(ra[i]-rb[i])
    return rab
def dot(ra,rb):
    value=0.0
    for i in range(len(ra)):
        value+=ra[i]*rb[i]

    return value

def IsParallel(ra,rb):
    Parallel=False
    n=len(ra)
    if n==2:
        norma=np.sqrt(ra[0]**2+ra[1]**2)
        normb=np.sqrt(rb[0]**2+rb[1]**2)
        rate=normb/norma
        if ra[0]*rate==rb[0] and ra[1]*rate==rb[1]:
            Parallel=True
        elif ra[0]*rate==-rb[0] and ra[1]*rate==-rb[1]:
            Parallel=True
    elif n==3:
        norma = np.sqrt(ra[0]**2+ra[1]**2+ra[2]**2)
        normb = np.sqrt(rb[0]**2+rb[1]**2+rb[2]**2)
        rate = normb / norma
        if ra[0]*rate ==rb[0] and ra[1]*rate==rb[1] and ra[2]*rate==rb[2]:
            Parallel = True
        elif ra[0]*rate==-rb[0] and ra[1]*rate==-rb[1] and ra[2]*rate==-rb[2]:
            Parallel=True

    return Parallel


r12=minus(r2,r1)
r31=minus(r1,r3)
r34=minus(r4,r3)

if IsParallel(r12,r34):
    print 'parallel line!'
else:
    A=np.zeros((2,2))
    F=np.zeros((2,1))

    A[0][0]=dot(r12,r12)
    A[0][1]=-dot(r12,r34)
    A[1][0]=dot(r34,r12)
    A[1][1]=-dot(r34,r34)

    F[0]=-dot(r12,r31)
    F[1]=-dot(r34,r31)

    X=np.linalg.solve(A,F)
    alpha=X[0];beta=X[1]

    print 'alpha=',alpha
    print 'beta=',beta
