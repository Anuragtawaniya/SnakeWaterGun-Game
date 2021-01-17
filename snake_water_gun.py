import random
#input from user
i = 0
user_score = 0
com_score = 0
chance = 10
pc_random = ['SNAKE','WATER','GUN']
print('Enter "S" for selecting Snake\nEnter "w" for selecting water\nEnter "G" for selecting gun')
while i<=chance:
    user_input = input().capitalize()
    ram_pc = random.choice(pc_random)
    print(ram_pc)
    if user_input == 'S':
        if ram_pc == 'SNAKE':
            print("Match drwa")
        
        elif ram_pc == 'WATER':
            print('You won match')
            user_score+=1
        elif ram_pc == "GUN":
            print("computer won")
            com_score+=1     
        else:
            print("please enter valid key")    
        #water      
    elif user_input == 'W':
        if ram_pc == 'WATER':
            print("MATCH DRAW")
        elif ram_pc == 'SNAKE':
            print('COMPUTER WON')
            com_score+=1
        elif ram_pc == "GUN":
            print("YOU WON")
            user_score+=1
        else:
             print("please enter valid key") 
        #gun         
    elif user_input == 'G':
        if ram_pc == "GUN":
            print("MATCH DRAW")
        elif ram_pc == "WATER":
            print("COMPUTER WON")
            com_score+=1
        else:
            print("You won")
            user_score+=1

    
    i+=1
print('MATCH END')
print(f'user score is {user_score}')
print(f'computer score is {com_score}')
if user_score > com_score:
    print("You won this match")
elif user_input < com_score:
    print("COMPUTER WON")    
else:
    print("MATCH DRAW")    