import random
print("..................Guess the Number Game.................")
r=random.randint(1,100)
print(r)
cs=int(input("Enter number of changes: " ))
print(f" You have {cs} changes \n ..........Best of luck............")
l=10*cs
p=10*cs
def check(r,nm):
    if(nm<r):
        # print(r,nm)
        print(f"guess no is Greater than {nm}")
    else:
        # print(r,nm)
        print(f" guess no is lessser than {nm}  ")
for i in range(1,cs+1):
    nm=int(input("Guess Number : "))
    c=cs-i
    if(nm==r):
        print("you gueesed correct")
        print("you earn ",p," points outoff ",l)
        break
    else:
        p=p-10
        check(r,nm)
        if(c==0):
            print(f"...............Game over the number was {r}................. ")
        print( f"Try Again  changes left are {c}")
        continue



