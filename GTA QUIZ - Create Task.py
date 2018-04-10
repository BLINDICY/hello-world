# GTA Trivia quiz
while True:
    print("This is a quiz that tests your knowledge on the GTA Series")

    '''
    '''

    name = input("Enter your name: ")
    print("Hi there,", name, "Are you ready to start the GTA quiz?")

    print("I will ask you 8 questions and give you four choices")
    print("Select which choice is the correct answer, A, B, C, or D")
    print("----------------------------")


    # set the score of the quiz to 0
    score = 0
    score = int(score)

    def test(A , B, C, D):
        print("A."+A)
        print("B."+B)
        print("C."+C)
        print("D."+D)
        print("")

    # question 1
    print("Question 1: What year was the 1st Grand Theft Auto released?")

    test("1997", "1999", "2001", "2002")

    Q1answer="A" # the right answer to question 1
    Q1response= input("Your answer: ")

    if Q1response =="A" or Q1response=='a':
        print("correct answer", Q1answer)
        score= score+1
    elif Q1response != "A" or Q1response != 'a':
        print("Sorry, incorrect")
        score= score+0
    
    print("Your current score is ",score, "out of 8")
    print("")

    print("This is a score of " +str((score*100)/8)+  "percent")
    print("")

        
    # question 2
    print("Question 2: In GTA3, who is Claude betrayed by?")

    test("Miguel", "8-Ball", "Catalina", "Kenji Kasen")

    Q2answer="C" # the right answer to question 2
    Q2response= input("Your answer: ")

    if Q2response =="C" or Q2response=='c':
        print("correct answer", Q2answer)
        score= score+1
    elif Q2response != "C" or Q2response != 'c':
        print("Sorry, incorrect")
        score= score+0

    print("Your current score is ",score, "out of 8")
    print("")

    print("This is a score of " +str((score*100)/8)+  "percent")
    print("")
    

    # question 3
    print("Question 3: In GTA Vice City, Tommy Vercetti is also known as the")
    print("__________ Butcher")
    print("")

    test("Vinewood","Harwood", "Downtown", "Trenton")

    Q3answer="B" # the right answer to question 3
    Q3response= input("Your answer: ")

    if Q3response =="B" or Q3response=='b':
        print("correct answer", Q3answer)
        score= score+1
    elif Q3response != "B" or Q3response != 'b':
        print("Sorry, incorrect")
        score= score+0

    print("Your current score is",score, "out of 8")
    print("")

    print("This is a score of " +str((score*100)/8)+  "percent")
    print("")

    
    # question 4
    print("Question 4: Which of the four children of Beverly Johnson died")
    print("before the events of GTA San Andreas?")
    print("")
    
    test("Sean Johnson", "Carl Johnson", "Kendl Johnson", "Brian Johnson")

    Q4answer="D" # the right answer to question 4
    Q4response= input("Your answer: ")

    if Q4response =="D" or Q4response=='d':
        print("correct answer", Q4answer)
        score= score+1
    elif Q4response != "D" or Q4response != 'd':
        print("Sorry, incorrect")
        score= score+0

    print("Your current score is",score, "out of 8")
    print("")

    print("This is a score of " +str((score*100)/8)+  "percent")
    print("")
    
    
    # question 5
    print("Question 5: In GTA Liberty City Stories, Toni Cipriani is the Capo")
    print("of which family?")
    print("")
    
    test("The Forellis", "The Sindaccos", "The Leones", "The Johnsons")

    Q5answer="C" # the right answer to question 5
    Q5response= input("Your answer: ")

    if Q5response =="C" or Q5response=='c':
        print("correct answer", Q5answer)
        score= score+1
    elif Q5response != "C" or Q5response != 'c':
        print("Sorry, incorrect")
        score= score+0

    print("Your current score is ",score, "out of 8")
    print("")

    print("This is a score of " +str((score*100)/8)+  "percent")
    print("")
    
    
    # question 6
    print("Question 6: In GTA Vice City Stories, you play as _______ Vance")
    print("")
    
    test("Janet", "Lance", "Pete", "Victor")

    Q6answer="D" # the right answer to question 6
    Q6response= input("Your answer: ")

    if Q6response =="D" or Q6response=='d':
        print("correct answer", Q6answer)
        score= score+1
    elif Q6response != "D" or Q6response != 'd':
        print("Sorry, incorrect")
        score= score+0

    print("Your current score is",score, "out of 8")
    print("")

    print("This is a score of " +str((score*100)/8)+  "percent")
    print("")
    
    
    # question 7
    print("Question 7: In GTA4, which borough do you start the game in?")
    print("")
    
    test("Broker", "Dukes", "Bohan", "Algonquin")

    Q7answer="A" # the right answer to question 7
    Q7response= input("Your answer: ")

    if Q7response =="A" or Q7response=='a':
        print("correct answer", Q7answer)
        score= score+1
    elif Q7response != "A" or Q7response != 'a':
        print("Sorry, incorrect")
        score= score+0

    print("Your current score is ",score, "out of 8")
    print("")

    print("This is a score of " +str((score*100)/8)+  "percent")
    print("")
    
    
    # question 8
    print("Question 8: In GTA5, how many protagonists can you play as? \n")
    print("")
    
    test("4", "3", "2", "1")

    Q8answer="B" # the right answer to question 8
    Q8response= input("Your answer: ")

    if Q8response =="B" or Q8response=='b':
        print("correct answer", Q8answer)
        score= score+1
    elif Q8response != "B" or Q8response != 'b':
        print("Sorry, incorrect")
        score= score+0

    print("Your current score is",score, "out of 8")
    print("")

    print("This is a score of " +str((score*100)/8)+  "percent")
    print("")

    
    # percentage score

    final_score=(score*100)/8
    print("Your final socre is " +str(final_score)+  "percent")

    user_input = input("Would you like to retake the quiz? Y/N:")
    if user_input == "Y" or user_input == "y":
        continue
    elif user_input == "N" or user_input == "n":
        print("Adios, Thanks for Playing!")
        break



