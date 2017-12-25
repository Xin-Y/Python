import numpy as np
import matplotlib.pyplot as plt
import sys

Rmin=0.1;Rmax=1.0
Width=10.0;Height=10.0

np.random.seed()
def GenerateCircle():
    cx=Width*np.random.rand(1)[0]
    cy=Height*np.random.rand(1)[0]
    radius=Rmin+(Rmax-Rmin)*np.random.rand(1)[0]

    return cx,cy,radius



def IsOverlap(subcircle,Circles):
    cx=subcircle[0]
    cy=subcircle[1]
    radius=subcircle[2]
    tol=1.e-5
    nOverlap=0
    for i in range(len(Circles)):
        cxi=Circles[i][0]
        cyi=Circles[i][1]
        ri =Circles[i][2]
        if np.sqrt((cx-cxi)**2+(cy-cyi)**2)<=radius+ri+tol:
            nOverlap+=1
            return True
    if nOverlap==0:
        return False

Circles = [];MaxTry=10000
def GenerateSet(MaxCircle):
    subcircle = GenerateCircle()
    Circles.append(subcircle)
    subcircle=GenerateCircle()
    for nCircle in range(MaxCircle-1):
        iTry=0
        while iTry<MaxTry:
            subcircle=GenerateCircle()
            if not IsOverlap(subcircle,Circles):
                break
            iTry+=1
            print 'iTry=',iTry
        if iTry<MaxTry:
            Circles.append(subcircle)
        else:
            print 'In the process of ',nCircle+1,' circle, generation failed!'
            sys.exit()

GenerateSet(50)

for i in range(len(Circles)):
    print '%3d-th circle: radius=%.5f, cx=%.5f, cy=%.5f\n'%(i+1,Circles[i][2],Circles[i][0],Circles[i][0])

###################################
### Plot circle
###################################

theta=np.linspace(0,2.0*np.pi,60)

plt.figure(1)
plt.hold
for i in range(len(Circles)):
    r=Circles[i][2]
    x=Circles[i][0]
    y=Circles[i][1]
    X=x+r*np.cos(theta)
    Y=y+r*np.sin(theta)
    plt.plot(X,Y)

plt.axis('equal')
#plt.axis([0.0,Width,0.0,Height])
plt.savefig('Result.png',dpi=800,bbox_inches='tight')
plt.show()
