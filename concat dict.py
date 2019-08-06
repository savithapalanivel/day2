dic1={1:2,5:6}
dic2={2:6,9:7}
dic3={7:8,5:7}
dic4={}
for x in(dic1,dic2,dic3):
    dic4.update(x)
print(dic4)  
