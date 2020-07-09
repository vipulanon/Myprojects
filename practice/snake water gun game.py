import random
n=10
lst=['s','w','g']
score_a=0
score_b=0
while n>0:
    a=input("your turn: ")
    b=random.choice(lst)
    print("commputer's turn: ",b)
    if a=='s' and b=='w':
        score_a=score_a+1
    elif a=='s' and b=='g':
        score_b=score_b+1
    elif a=='w' and b=='s':
        score_b=score_b+1
    elif a=='w' and b=='g':
        score_a=score_a+1
    elif a=='g' and b=='s':
        score_a=score_a+1
    elif a=='g' and b=='w':
        score_b=score_b+1
    n=n-1
if score_b<score_a:
    print("You won!")
    print("score of a: "+str(score_a)+"\nscore of b: "+str(score_b))
elif score_b>score_a:
    print("computer won!")
    print("score of a: "+str(score_a)+"\nscore of b: "+str(score_b))
else:
    print("Its a tie!")
    print("score of a: "+str(score_a)+"\nscore of b: "+str(score_b))
