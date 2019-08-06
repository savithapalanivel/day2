x=[[1,3,8],
   [5,8,9],
   [7,0,8]]
y=[[5,2,7],
   [8,6,5],
   [6,3,5]]
result=[[0,0,0],
        [0,0,0],
        [0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j]=x[i][j]+y[i][j]
for r in result:
    print(r)
