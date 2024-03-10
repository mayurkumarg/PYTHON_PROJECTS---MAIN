import random as ran
list=[]
for a in range (1,101):
    list.append(a)
d=ran.choice (list)
print ('Guess the no 1 to 100')
sc=10
while True:
    b=int (input ("\nenter the no>>"))
    sc=sc-1
    if b>100:
        print(f"{b} is > than 100")
        break
    if b>d:
        print ("it is a bigger no")
    elif b==d:
        print('it is a right no')
        break
    elif sc==0:
        print ("BETTER LUCK NXT TIME")
        break
    else:
        print("it iS smaller")
    print (f"\n{sc}..chances left")
sc2=int()
if b<100:
    sc2=sc*10
    print(f"your score is>>>>{sc2}/100")