import random
pc=random.randint(0,100)
g=150
t=0
while g !=pc:
    g=int(input("give"))
    t=t+1
    if g>pc:
        print("down")
    elif g<pc:
        print("up")
    else :
        print("correct")
        print("tries=",t)


