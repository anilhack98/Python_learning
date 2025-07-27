questions=[
    ["Which language is used to create fb?","Python","French","Javascript","PHP","None",4],
    ["Which language is used to create fb?","Python","French","Javascript","PHP","None",4],
    ["Which language is used to create fb?","Python","French","Javascript","PHP","None",4],
    ["Which language is used to create fb?","Python","French","Javascript","PHP","None",4],
    ["Which language is used to create fb?","Python","French","Javascript","PHP","None",4],
    ["Which language is used to create fb?","Python","French","Javascript","PHP","None",4],
]

levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money=0
i=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"a. {question[1]}   b.{question[2]}")
    print(f"c. {question[3]}   d.{question[4]}")
    reply=int(input("Enter Your Answer (1-4)"))
    if(reply==question[-1]):
        print(f"Correct answer, You have won Rs. {levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
         money=320000
        elif(i==14):
         money=10000000
    else:
        print("Wrong answer, Better luck next time")
        break
print(f"Your have won total {money}") 