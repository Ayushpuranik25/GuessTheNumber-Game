import random

target = random.randint(1,100)
print(target)


while True:
        
        userChoice = input("enter the number or Quit(Q): ")
        if(userChoice == "Q"):
              break
        
        userChoice = int(userChoice)
        if(userChoice == target):
          print("Success : correct ")
          break

        elif(userChoice < target):
               print("number is too small or take a larger guess")

        else:
              print("number is too large or take a smaller guess")



print("----Game End----")
