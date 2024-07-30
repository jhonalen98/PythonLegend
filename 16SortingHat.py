# Write code below 💖

gryffindor=0
ravenclaw=0
hufflepuff=0
slytherin=0
print("Q1) Do you like Dawn or Dusk?")
print("     1) Dawn")
print("     2) Dusk")
while True:
    answer=int(input("Enter your answer (1-4): "))
    if answer == 1:
        gryffindor +=1
        ravenclaw = ravenclaw +1
        break
    elif answer ==2:
        hufflepuff +=1
        slytherin +=1
        break
    else:
        print("Wrong input")  
print("Q2) When I’m dead, I want people to remember me as:")
print("     1) The Good")
print("     2) The Great")
print("     3) The Wise")
print("     4) The Bold")
while True:
    answer=int(input("Enter your answer (1-4): "))
    if answer == 1:
        hufflepuff +=2
        break
    elif answer == 2:
        slytherin +=2
        break
    elif answer == 3:
        ravenclaw += 2
        break
    elif answer == 4:
        gryffindor += 2
        break
    else:
        print ("Wrong input")
print("Q3) Which kind of instrument most pleases your ear?")
print("     1) The violin")
print("     2) The trumpet")
print("     3) The piano")
print("     4) The drum")    
while True:
    answer=int(input("Enter your answer (1-4): "))
    if answer == 1:
        slytherin +=4
        break
    elif answer == 2:
        hufflepuff +=4
        break
    elif answer == 3:
        ravenclaw +=4
        break
    elif answer == 4:
        gryffindor +=4
        break
    else:
        print ("Wrong input")
if slytherin >4:
    print("You belong in Slitherin")
elif hufflepuff >4:
    print("You belong in Hufflepuff")
elif ravenclaw >4:
    print("You belong in Ravenclaw")
else:
    print("You belong in Gryffindor")