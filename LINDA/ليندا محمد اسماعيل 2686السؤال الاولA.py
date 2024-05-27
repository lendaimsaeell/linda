d= {  }
L1=['HTTP','HTTPS','FTP','DNS']
L2=[80,443,21,53]
for x,y in zip(L1,L2):
     d[x]=y
print(d)