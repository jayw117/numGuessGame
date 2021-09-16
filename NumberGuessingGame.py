#Jason Wong
#Project 2 Guessing Game
#2-8-2019
#The program will give a random integer between the range that is assigned and YOU must
#guess the random integer. There will be multiple guesses and if you guess correctly, you
#may enter your name on the highscore list depending on how many guesses it took you.

import random
import webbrowser
import time
start=input("Do you want to Guess that Number? Press y to start or any other key to quit ")
if start.lower()=="y": #Huge If statement based off of whatever start() is and if they choose to quit it goes to bottom else:
    def game():

        
        guess_taken=0
        random_number=random.randint(0,100)
        name=input("What is your name? ")
        print("Hi",name,"I am thinking of a number between 0 and 100. Are you feeling lucky?")
        #print(random_number)
        while guess_taken<5: #Will allow the user to keep playing the same game as long as they don't have 5 or more guess taken
            guess_taken=guess_taken+1;
            while True:    
                try:
                    chosen_number=input("Enter a number: ")
                    val=int(chosen_number)
                    break
                except ValueError:      #Prevents answers such as "two" or "saldkgjasldgkj" to be accepted by program and makes them re enter an integer
                    print("You need to enter a whole integer. (Hint:The answer will never be a decimal). Please enter an integer")
            if int(chosen_number)==random_number:
                webbrowser.open_new("https://youtu.be/Jmd4OLzhQw0?t=33")
                print("Good Job, you guessed the correct number with", 5-guess_taken,"guesses left") #5-guess_taken is to show how many guesses are left since guess_taken = number of guess used        
                with open("high_score.txt", "a") as f:
                    f.write(str(guess_taken)+" "+ name+"\n") #Must convert guess_taken to string and then add name from beginning
                with open("high_score.txt","r") as f:
                    highscore=f.readlines()
                    highscore.sort()
                    print("Highscores")
                    if len(highscore)<3:
                        print(highscore)
                    if len(highscore)>=3:
                        print(highscore[0:3])  #Will only print the first three highscores
                    break
            if int(chosen_number)<random_number:    #These if statements will tell the user if the number entered is too low or too high and will subtract their guesses
                print("Too low")
                print("You have", 5-guess_taken ,"guesses left")
            if int(chosen_number)>random_number:
                print("Too High")
                print("You have", 5-guess_taken ,"guesses left")
            if guess_taken>=5:
                print("The number to guess was",random_number)
                break
        while True:
            restart=input("Want to play again? Press y to play again or any key to quit ") #After game has finished, gives the user option to quit or play again where it resets back to beginning
            if restart.lower()=="y":
                game()
            else:
                print("Thanks for playing!")
                time.sleep(3)
                webbrowser.open_new("www.youtube.com/watch?v=Uo2SNtFofWI&t=18s")
            break
    game()
else:
    print("Okay maybe another time.")
    time.sleep(3)
    webbrowser.open_new("https://i.redd.it/yw8xznyj0dy11.gif")
    
    



