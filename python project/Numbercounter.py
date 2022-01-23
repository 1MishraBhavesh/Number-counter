import  random

print ("Number guessing game")

number=random.randint(1,9)

chances=0

print ("Guess a number{Between 1 to 9}:")

while chances <5 :


   guess=int(input("Enter your guess:- "))


   if guess == number :

       print("Congratulation you Won!!")
       break

   elif guess < number :
        print("Your Number is to low: Guess a Number Higher than", guess)


   else :
        print("Your Number is to high: Guess a Number Lower than", guess)

    

if not chances <5 :
        print("you lose 😭😭 !!! The Number is",number)




        
         



