import random
def rcs():
    l=["Rock","Paper","Scissor"]
    
    
    print("******************************")
    print("   Rock Paper Scissor game")
    print("To choose rock paper scissor you must have\nto enter that is given below")
    print("For Rock u can enter 1")
    print("For Paper u can enter 2")
    print("For scissor u can enter 3")
    while True:
        choice=int(input("Enter Your Choice:"))
        if choice ==1:
           c=random.randint(0,2)
           if c==0:
               print("Your move:",l[choice-1])
               print("Computer move:",l[c])
               print("Tie! Play again")
           elif c==1:
               print("Your move:",l[choice-1])
               print("Computer move:",l[c])
               print("Computer Won ! you lose")
           else:
               print("Your move:",l[choice-1])
               print("Computer move:",l[c])
               print("You Win Congo!!!!")
        if choice==2:
            c=random.randint(0,2)
            if c==0:
                print("Your move:",l[choice-1])
                print("Computer move:",l[c])
                print("You win hurray!!!!")
            elif c==1:
                print("Your move:",l[choice-1])
                print("Computer move:",l[c])
                print("Match tie play again")
            else:
                print("Your move:",l[choice-1])
                print("Computer move:",l[c])
                print("You lose play again")
        if choice==3:
            c=random.randint(0,2)
            if c==0:
                print("Your move:",l[choice-1])
                print("Computer move:",l[c])
                print("You lose !!! play again good luck")     
            elif c==1:
                print("Your move:",l[choice-1])
                print("Computer move:",l[c])
                print("You win !!! smart move by you!")
            else:
                print("Your move:",l[choice-1])
                print("Computer move:",l[c])
                print("Match Tie!! pkayyyy againnn")
        
        
        
rcs()