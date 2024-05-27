X=list(input("ادخل رقم ثنائي:"))
Y=0
for i in range(len(X)):
    digit=X.pop()
    if digit=='1':
       Y=Y+pow(2,i)
print("الرقم العشري المكافئ:",Y)