import random 

def gamewin(comp,you):
    if comp==you:
        return None
    if comp=='s':
        if you=='g':
            return True
        if you=='w':
            return False
    elif comp=='w':
        if you=='g':
            return False
        if you=='s':
            return True
    elif comp=='g':
        if you=='s':
            return False
        if you=='w':
            return True
    

print(f"Comp's Turn: Snake(s) Water(w) of Gun(g)? ")

randno=random.randint(1,3)


if randno==1:
    comp='s'
elif randno==2:
    comp='w'
else:
    comp='g'


you=input("your's Turn: Snake(s) Water(w) of Gum(g)?")
g=gamewin(comp,you)
print(f"computer chose {comp}")
print(f"you chose {you}")
if g==None:
    print("The game is a tie")
elif g:
    print("you won!")
else:
    print("you lose!")
