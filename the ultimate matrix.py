import numpy as np

n , m = input().split()
n = int(n)
m = int(m)

x , y , z = input().split()
x = int(x)
y = int(y)
z = int(z)

arr = []  
for i in range(n):
    inp = ""
    for j in range(m):
        inp = inp + input() + " "
        
    inp = inp.split()    
    for k in range(m*m):
        inp[k] = float(inp[k])
    
    inp = np.array(inp).reshape(m,m)
    arr.append(inp)

for i in range(n):
    for j in range(n-i-1):
        if np.linalg.det(arr[j]) > np.linalg.det(arr[j+1]):
            arr[j],arr[j+1] = arr[j+1],arr[j]

    
result = np.dot(arr[x].transpose(),arr[y]) + np.linalg.inv(arr[z])
print(format(np.sum(result), ".3f"))
        