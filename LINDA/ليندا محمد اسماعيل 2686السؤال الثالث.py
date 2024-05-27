import json
questions = {}
scores = 0
number = 1 
f = open("questions.txt", 'r') 
questions = json.load(f)
f.close() 
print("اختبر برنامج بايثون")
print("ادخل خ للخطأ وص للصح")
name = input("ادخل اسمك الكامل")
    for ques in questions.keys():
        print("",number,":",ques)
    ans = input("الإجابة هي ") 
    if ans.upper() == questions[ques].upper():
        scores += 1
        print("صحيح")
    else:
          print("خطأ")
    number+=1 
result = {name: scores}
m = open("score.txt", 'w') 
json.dump(result, m)
m.close()