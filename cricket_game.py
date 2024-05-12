import random

def main():
    print("\n\n\t\t\t\tWELCOME TO GULLY CRICKET")
    input("\nPress enter to start the game _ _ _")

    print("This game requires two users.")
    
    
    print("\n\nOvers options = 5, 10, or 20.")
    while True:
        over_choice = input(("How many overs do you want to play? "))
        if over_choice.isdigit():
            
            while True:
                match over_choice:
                    case "5":
                        five_overs()


                    case "10":
                        ten_overs()
                    
                    
                    case "20":
                        twenty_overs()
                        
                    
                    case _:
                        print(over_choice,"overs not available.")
                        break

            
        
        else:
            print("Please type a valid option. Thank you!")
            continue

   
    



def five_overs():
    while True:
    
        print("\n")
        print("\t\t\t  -----------------------------------------------")
        print("\t\t\t\tWELCOME TO FIVE OVERS GULLY CRICKET")
        print("\t\t\t  -----------------------------------------------")
        print("\nRules:\n1. Total Overs = 5\n2. Total wickets = 5\n3. Everything is randomized.")
        

        input("\nThe weather looks fine. It's toss time. Press Enter to continue.\n")
        toss = input("One of you choose heads and the other choose tails and Press Enter to continue.\n")

        toss_list = ["Heads", "Tails"]
        random_number1 = random.randint(0,1)
        toss = toss_list[random_number1]
        print("It's", toss,".")
        print("The toss winner decides who bats first.\n")

        batter = input("\tName of the batter = ")
        bowler = input("\tName of the bowler = ")
        
        print("\n\t\t\t\t",batter,"is batting.")
        print("\t\t\t  ------------------------------")
        input("Press enter to sim the first over.")

        overs = 0
        balls = 0
        wickets = 0
        first_score = 0
        temp_runs = 0
        while True:
            print("----------------------------------------")
            print("----------------------------------------")
            random_number2 = random.randint(0,7)
            if random_number2 == 7:
                
                balls += 1
                wickets += 1

            
            else:
                
                first_score = first_score + random_number2
                balls += 1
                
            
            if balls == 6:
                print("That's an over.")
                overs += 1
                balls = 0
                print("Score =",first_score,"for",wickets,"in",overs,"overs")
                print("You scored", int(first_score - temp_runs),"runs in the last over.")
                temp_runs = first_score
                input("\nPress enter to sim the next over.")
            
            if overs == 5:
                print("All overs completed")
                print("----------------------------------------\n")
                print("End of first Innings.")
                break

            if wickets == 5:
                print("----------------------------------------\n")
                print("You are all out!! End of first Innings.")
                break
        
        print("\n")
        input("Press Enter to continue.")
        print("\n",batter, "scored", first_score, "runs.")
        print("\n")
        print("Target for",bowler,"is",first_score+1,"runs in 5 overs with 5 wickets in hand.")
        print("\n\n")
        input("Press Enter to Continue to the Second Innings")

        print("\n\t\t\t\t",bowler,"is batting.")
        print("\t\t\t  ------------------------------")
        input("Press enter to sim the first over.")

        overs = 0
        balls = 0
        wickets = 0
        second_score = 0
        temp_runs = 0
        
        while True:
            print("----------------------------------------")
            
            print("----------------------------------------")
            random_number2 = random.randint(0,7)
            if random_number2 == 7:
                
                balls += 1
                wickets += 1
                
            elif random_number2 == 5:
                
                second_score = second_score + random_number2
                balls += 1
                
            
            else:
                
                second_score = second_score + random_number2
                balls += 1
                
            
            if second_score > first_score:
                print("\n")
                print("\n",batter,"scored", first_score,"runs.")
                print("\n")
                print(bowler,"scored", second_score,"runs.")
                print("\n")
                print(bowler,"won the game by",5 - int(wickets),"wickets.")
                print("\n\n")
                break
        
            if balls == 6:
                print("That's an over.")
                overs += 1
                balls = 0
                print("Score =",second_score,"for",wickets,"in",overs,"overs")
                print("You scored", int(second_score - temp_runs),"runs in the last over.")
                temp_runs = second_score
                print("You need ",int(first_score+1)-int(second_score),"runs to win the game.")
                input("\nPress enter to skip the next over.")
            
            if overs == 5:
                print("All overs completed")
                print("----------------------------------------\n")
                print("End of second Innings.")
                input("Press Enter to sim the next over.")
                break

            if wickets == 5:
                print("----------------------------------------\n")
                input("You are all out!! End of second Innings.")
                break
        
        if first_score > second_score:
            print("\n")
            print("\n",batter,"scored", first_score,"runs.")
            print("\n")
            print(bowler,"scored", second_score,"runs.")
            print("\n")
        print(batter,"won the game by",int(first_score) - int(second_score),"runs.")
        print("\n\n")

def ten_overs():
    while True:
    
        print("\n")
        print("\t\t\t  -----------------------------------------------")
        print("\t\t\t\tWELCOME TO TEN OVERS GULLY CRICKET")
        print("\t\t\t  -----------------------------------------------")
        print("\nRules:\n1. Total Overs = 10\n2. Total wickets = 7\n3. Everything is randomized.")
        

        input("\nThe weather looks fine. It's toss time. Press Enter to continue.\n")
        toss = input("One of you choose heads and the other choose tails and Press Enter to continue.\n")

        toss_list = ["Heads", "Tails"]
        random_number1 = random.randint(0,1)
        toss = toss_list[random_number1]
        print("It's", toss,".")
        print("The toss winner decides who bats first.\n")

        batter = input("\tName of the batter = ")
        bowler = input("\tName of the bowler = ")
        
        print("\n\t\t\t\t",batter,"is batting.")
        print("\t\t\t  ------------------------------")
        input("Press enter to sim the first over.")

        overs = 0
        balls = 0
        wickets = 0
        first_score = 0
        temp_runs = 0
        while True:
            print("----------------------------------------")
            print("----------------------------------------")
            random_number2 = random.randint(0,7)
            if random_number2 == 7:
                
                balls += 1
                wickets += 1

            
            else:
                
                first_score = first_score + random_number2
                balls += 1
                
            
            if balls == 6:
                print("That's an over.")
                overs += 1
                balls = 0
                print("Score =",first_score,"for",wickets,"in",overs,"overs")
                print("You scored", int(first_score - temp_runs),"runs in the last over.")
                temp_runs = first_score
                input("\nPress enter to sim the next over.")
            
            if overs == 10:
                print("All overs completed")
                print("----------------------------------------\n")
                print("End of first Innings.")
                break

            if wickets == 5:
                print("----------------------------------------\n")
                print("You are all out!! End of first Innings.")
                break
        
        print("\n")
        input("Press Enter to continue.")
        print("\n",batter, "scored", first_score, "runs.")
        print("\n")
        print("Target for",bowler,"is",first_score+1,"runs in 10 overs with 7 wickets in hand.")
        print("\n\n")
        input("Press Enter to Continue to the Second Innings")

        print("\n\t\t\t\t",bowler,"is batting.")
        print("\t\t\t  ------------------------------")
        input("Press enter to sim the first over.")

        overs = 0
        balls = 0
        wickets = 0
        second_score = 0
        temp_runs = 0
        
        while True:
            print("----------------------------------------")
            
            print("----------------------------------------")
            random_number2 = random.randint(0,7)
            if random_number2 == 7:
                
                balls += 1
                wickets += 1
                
            elif random_number2 == 5:
                
                second_score = second_score + random_number2
                balls += 1
                
            
            else:
                
                second_score = second_score + random_number2
                balls += 1
                
            
            if second_score > first_score:
                print("\n")
                print("\n",batter,"scored", first_score,"runs.")
                print("\n")
                print(bowler,"scored", second_score,"runs.")
                print("\n")
                print(bowler,"won the game by",5 - int(wickets),"wickets.")
                print("\n\n")
                break
        
            if balls == 6:
                print("That's an over.")
                overs += 1
                balls = 0
                print("Score =",second_score,"for",wickets,"in",overs,"overs")
                print("You scored", int(second_score - temp_runs),"runs in the last over.")
                temp_runs = second_score
                print("You need ",int(first_score+1)-int(second_score),"runs to win the game.")
                input("\nPress enter to skip the next over.")
            
            if overs == 10:
                print("All overs completed")
                print("----------------------------------------\n")
                print("End of second Innings.")
                input("Press Enter to sim the next over.")
                break

            if wickets == 5:
                print("----------------------------------------\n")
                input("You are all out!! End of second Innings.")
                break
        
        if first_score > second_score:
            print("\n")
            print("\n",batter,"scored", first_score,"runs.")
            print("\n")
            print(bowler,"scored", second_score,"runs.")
            print("\n")
        print(batter,"won the game by",int(first_score) - int(second_score),"runs.")
        print("\n\n")

def twenty_overs():
    while True:
    
        print("\n")
        print("\t\t\t  -----------------------------------------------")
        print("\t\t\t\tWELCOME TO TWENTY OVERS GULLY CRICKET")
        print("\t\t\t  -----------------------------------------------")
        print("\nRules:\n1. Total Overs = 20\n2. Total wickets = 10\n3. Everything is randomized.")
        

        input("\nThe weather looks fine. It's toss time. Press Enter to continue.\n")
        toss = input("One of you choose heads and the other choose tails and Press Enter to continue.\n")

        toss_list = ["Heads", "Tails"]
        random_number1 = random.randint(0,1)
        toss = toss_list[random_number1]
        print("It's", toss,".")
        print("The toss winner decides who bats first.\n")

        batter = input("\tName of the batter = ")
        bowler = input("\tName of the bowler = ")
        
        print("\n\t\t\t\t",batter,"is batting.")
        print("\t\t\t  ------------------------------")
        input("Press enter to sim the first over.")

        overs = 0
        balls = 0
        wickets = 0
        first_score = 0
        temp_runs = 0
        while True:
            print("----------------------------------------")
            random_number2 = random.randint(0,7)
            if random_number2 == 7:
                print("Crap!!That's a wicket.",overs,".",int(balls)+1,"overs")
                balls += 1
                wickets += 1

            elif random_number2 == 5:
                print("You scored 5 runs off of byes.",overs,".",int(balls)+1,"overs")
                first_score = first_score + random_number2

            else:
                print("You scored",random_number2,"runs.",overs,".",int(balls)+1,"overs")
                first_score = first_score + random_number2
                balls += 1
                
            
            if balls == 6:
                print("----------------------------------------")
                print("That's an over. Completion of over",int(overs+1))
                print("----------------------------------------")
                print("----------------------------------------")
                overs += 1
                balls = 0
                print("Score =",first_score,"for",wickets,"in",overs,"overs")
                print("You scored", int(first_score - temp_runs),"runs in the last over.")
                temp_runs = first_score                
                print("----------------------------------------")
                input("\nPress enter to sim the next over.")
            
            if overs == 20:
                print("All overs completed")
                print("----------------------------------------\n")
                print("End of first Innings.")
                break

            if wickets == 10:
                print("----------------------------------------\n")
                print("You are all out!! End of first Innings.")
                break
        
        print("\n")
        input("Press Enter to continue.")
        print("\n",batter, "scored", first_score, "runs.")
        print("\n")
        print("Target for",bowler,"is",first_score+1,"runs in 20 overs with 10 wickets in hand.")
        print("\n\n")
        input("Press Enter to Continue to the Second Innings")

        print("\n\t\t\t\t",bowler,"is batting.")
        print("\t\t\t  ------------------------------")
        input("Press enter to sim the first over.")

        overs = 0
        balls = 0
        wickets = 0
        second_score = 0
        temp_runs = 0
        
        while True:
                       
            print("----------------------------------------")
            random_number2 = random.randint(0,7)
            if random_number2 == 7:
                print("Crap!!That's a wicket.")
                balls += 1
                wickets += 1
                
            elif random_number2 == 5:
                print("You scored 5 runs off of byes.\n")                
                second_score = second_score + random_number2
                balls += 1
                
            
            else:
                print("You scored",random_number2,"runs.")
                second_score = second_score + random_number2
                balls += 1
                
            
            if second_score > first_score:
                print("\n")
                print("\n",batter,"scored", first_score,"runs.")
                print("\n")
                print(bowler,"scored", second_score,"runs.")
                print("\n")
                print(bowler,"won the game by",5 - int(wickets),"wickets.")
                print("\n\n")
                break
        
            if balls == 6:
                print("----------------------------------------")
                print("That's an over.")
                print("----------------------------------------")
                print("----------------------------------------")
                overs += 1
                balls = 0
                print("Score =",second_score,"for",wickets,"in",overs,"overs")
                print("You scored", int(second_score - temp_runs),"runs in the last over.")
                temp_runs = second_score
                print("----------------------------------------")
                print("You need ",int(first_score+1)-int(second_score),"runs to win the game.")
                print("----------------------------------------")
                input("\nPress enter to skip the next over.")
            
            if overs == 20:
                print("All overs completed")
                print("----------------------------------------\n")
                print("End of second Innings.")
                input("Press Enter to complete the game.")
                break

            if wickets == 10:
                print("----------------------------------------\n")
                input("You are all out!! End of second Innings.")
                break
        
        if first_score > second_score:
            print("\n")
            print("\n",batter,"scored", first_score,"runs.")
            print("\n")
            print(bowler,"scored", second_score,"runs.")
            print("\n")
            print(batter,"won the game by",int(first_score) - int(second_score),"runs.")
            print("\n\n")



main()

            

