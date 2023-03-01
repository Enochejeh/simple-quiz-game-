print("welcome to my quiz game? ")

playing = input("do you want to play? ")

if playing != "yes": 
    quit()

print ("ok! let do this ")
score = 0



answer =input("what does CPU stands for? ").lower()
if answer == "central processing unit":
    print("correct")
    score += 3

else:
    print("incorrrect")  

answer =input("what does RSU stands for? ").lower()
if answer == "power supply":
    print("correct")
    score += 4

else:
    print("incorrrect")        

answer =input("what does GPU stands for? ").lower()
if answer == "graphics processing unit":
    print("correct")
    score += 2   
else:
    print("incorrrect")   

answer =input("what does RAM stands for? ").lower()
if answer == "random access memory":
    print("correct")
    score += 3
else:
    print("incorrrect")  


print ("you got " + str(score) + "questions correct!")                