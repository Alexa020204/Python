import numpy as np
figura=np.full((9,9),"-")


i=4
for j in range(0,9,1):
    figura[i][j]="o"

j=4
for i in range(0,9,1):
    figura[i][j]="o"

print(figura)

