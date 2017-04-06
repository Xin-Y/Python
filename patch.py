import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
x=[0.0,1.0,1.0,0.0]
x1=[1.0,2.0,2.0,1.0]
y=[0.0,0.0,1.0,1.0]
z=[1.0,2.0,3.0,4.0]
z1=[2.0,5.0,6.0,3.0]
X=np.zeros((2,2))

X[0][0]=0.0;X[0][1]=1.0
X[1][0]=-1.0;X[1][1]=2.0

plt.hold()
plt.tricontourf(x,y,z,100)
plt.tricontourf(x1,y,z1,100)
plt.colorbar(label='Stress')
plt.show()