import pandas as pd
name=input("ENTER THE NAME OF THE STUDENT>>>")
reg=input("ENTER REGISTER NUMBER OF THE STUDENT>>>")
isub=int(input("\n""ENTER THE NUMBER OF SUBJECTS"))
sub=[]
lsub=len(sub)
wm=[]
im=[]
total=[]
q=1
while q<isub+1:
    n=input(f"\n"f"ENTER THE NAME OF SUBJECT.{q}>>>")
    sub.append(n)
    wmm=int(input("\n"f"ENTER THE MARKS OBTAINED IN SUB({n}) /80>>>"))
    wm.append(wmm)
    if wmm>80:
        print("INVALID MARKS")
        break
    imm=int(input(f"ENTER THE INTERNAL MARKS OBTAINED IN SUB({n})  /20>>>"))
    im.append(imm)
    if imm>20:
        print("INVALID MARKS")
        break
    c=wmm+imm
    total.append(c)
    q+=1
print("\n""\n""\n""\n"">>>>> THE BOARD OF TECHNICAL EDUCATION 2022-23<<<<<")
print("_."*9,"MARKS CARD","._"*9)
print(f"NAME: {name}")
print(f"REGISTER NO: {reg}")
det={"SUBJECTS":[x for x in sub],"EXTERNAL MARKS/80":[x for x in wm],
         "INTERNAL MARKS/20":[x for x in im],"TOTAL MARKS/100":[x for x in total]}
ones=pd.DataFrame(det,index=[x for x in range(1,isub+1)])
print(ones)
sum=sum(total)
iisub=isub*100
print(f"THE TOTAL MARKS OBTAINED>>>{sum}/{iisub}")
p=sum/isub
print(f"PERCNTAGE>>>{p}%<<<")
if p>90:
    print("GRADE>>>A+")
    print("RESULT>>>DISTINCTION")
elif p<90 and p>80:
    print("GRADE>>>B+")
    print("RESULT>>>FIRST CLASS")
elif p<70 and p<80:
    print("GRADE>>>C+")
    print("SECOUND CLASS>>>SECOUND CLASS")
else:
    print("RESULT>>>FAIL")