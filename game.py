#Ra7oox
import random
lst=["rock","paper","scissors"]

score_comupter=0
score_user=0
username=str(input("what's ur name?"))


while True:
    
    computer=lst[random.randint(0,2)]
    user=str(input("rock,paper,scissors?"))
    print(computer)
    if computer=="rock" and user=="scissors":
        score_comupter=score_comupter+1
    elif user=="rock" and computer=="scissors":
        score_user=score_user+1
    if computer=="paper" and user=="rock":
        score_comupter=score_comupter+1
    elif user=="paper" and computer=="rock":
        score_user=score_user+1
    if computer=="scissors" and user=="paper":
        score_comupter=score_comupter+1
    elif user=="scissors" and computer=="paper":
        score_user=score_user+1
    if score_user==3 or score_comupter==3:
        print(f"score final is  {score_comupter} for computer and  {score_user} for {username}")
        break

