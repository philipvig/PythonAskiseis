import random
import numpy as np
X= input("Dwste X diastash orthogwniou:")
Y= input("Dwste Y diastash orthogwniou:")
x=int(X)
y=int(Y)
array1=[]
for i in range(x*y//2):
    array1.append(1)
for j in range(x*y//2,x*y):
    array1.append(0)
random.shuffle(array1)
array = np.reshape(array1, (x, y))
print(array)
counterh=0
counterv=0
counterd1=0
counterd2=0
for i in range(x):
    c=0
    for j in range(y):
        if array[i][j]==1: #horizontal
            c=c+1
        else:
            c=0
        if c==4:
            counterh=counterh+1
        elif c>=5:
            counterh=c//2 + c%2
#vertical
for i in range(x):
    for j in range(y):
        if array[i][j]==1:
            if i<=len(array)-4:
                if array[i+1][j]==1 and array[i+2][j]==1 and array[i+3][j]==1:
                    counterv+=1

#diagonal
for i in range(x):
    for j in range(y):
        if array[i][j]==1:
            if (not j>=len(array[i])-4)and(not i>=len(array)-4):
                if array[i+1][j+1]==1 and array[i+2][j+2]==1 and array[i+3][j+3]==1:
                    counterd1+=1
            if (not i>=len(array[i])-4)and(not j>=len(array)-4):
                if array[i-1][j-1]==1 and array[i-2][j-2]==1 and array[i-3][j-3]==1:
                    counterd2+=1

print(counterh)
print(counterv)
print(counterd1+counterd2)





