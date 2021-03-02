import random
import numpy as np
X= input("Dwste X diastash orthogwniou:")
Y= input("Dwste Y diastash orthogwniou:")
x=int(X)
y=int(Y)
array1=[]
for i in range(x*y//2):
    array1.append("S")
for j in range(x*y//2,x*y):
    array1.append("O")
random.shuffle(array1)
array = np.reshape(array1, (x, y))
print(array)
horizontalsos=0
verticalsos=0
diagonalsos=0
for i in range(x):
    for j in range(y):
        if(array[i][j]=="S"):
            if not j>=len(array[i])-3:
                if array[i][j+1]=="O" and array[i][j+2]=="S":
                    horizontalsos+=1
            if (not j>=len(array[i])-3)and(not i>=len(array)-3):
                if array[i+1][j+1]=="O" and array[i+2][j+2]=="S":
                    diagonalsos+=1
            if (not i>=len(array[i])-3)and(not j>=len(array)-3):
                if array[i-1][j-1]=="O" and array[i-2][j-2]=="S":
                    diagonalsos+=1

            if not i>=len(array)-3:
                if array[i+1][j]=="O" and array[i+2][j]=="S":
                    verticalsos+=1

print(horizontalsos)
print(verticalsos)
print(diagonalsos)