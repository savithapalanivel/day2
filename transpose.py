x=[[3,8],
   [5,8],
   [7,8]]
result=[[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[j][i]=x[i][j]
for r in result:
    print(r)
