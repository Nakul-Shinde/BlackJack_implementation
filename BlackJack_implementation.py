import random

print("Welcome to BlackJack game")

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                



def extra_card(add_card,initial_user_score,com_card1):
    while add_card=='y':
        user_extra_card=random.choice(card_list)
        user_cards.append(user_extra_card)
        print("Your cards are:",user_cards)
        extra_score=initial_user_score+user_extra_card
        print("Your current score is:",extra_score)
        print("Computer's first Card:",com_card1)
        add_card=input("Type 'y' to add another card or 'n' to pass:")
        
        if add_card=='y':
            initial_user_score=extra_score
            
        else:
            return extra_score
         
def computer_card(com_card1,com_card2):
        score=com_card1+com_card2
        while score<17:
            computer_extra_card=random.choice(card_list)
            computer_cards.append(computer_extra_card)
            total_score=score+computer_extra_card
            if total_score>=17:
                return total_score
            else:
                score= total_score
        return score


def compare_player(user,computer):
    if user>21:
        print("You Lost")

    elif user<=21 and user>computer:
        print("You Won")

    elif user<=21 and computer>21:
        print("You Won")
    
    elif user<computer and user<=21 and computer<=21:
        print("You Lost")
        
    else:
        print("Game is draw")

start='y'

start=input("Do you want to splay the BlackJack (y/n)")

if (start=='n'):
    print("\t")
else:
        
    print(logo)    
    repeat='y'        
    while repeat=='y':
        card_list=[1,2,3,4,5,6,7,8,9,10,10,10,10]
        user_cards=[]
        computer_cards=[]
        user_card1=random.choice(card_list)
        user_card2=random.choice(card_list)
        initial_user_score=user_card1+user_card2
        user_cards.append(user_card1)
        user_cards.append(user_card2)
        
        print("Your cards are:",user_cards)
        print("Your Current Score is :",initial_user_score)
        
        com_card1=random.choice(card_list)
        com_card2=random.choice(card_list)
        initial_com_score=com_card1+com_card2
        computer_cards.append(com_card1)
        computer_cards.append(com_card2)
        
        print("Computer's first card is:",com_card1)
        
        
        add_card=input("Type 'y' to add another card or 'n' to pass:")
        
        if add_card=='y':
            total_user_score=extra_card(add_card,initial_user_score,com_card1)
            print("Your final Cards are:",user_cards)
            print("Your Final Score is:",total_user_score)
            total_computer_score=computer_card(com_card1,com_card2)
            print("Computer's final Cards are:",computer_cards)
            print("Computer's Final Score is:",total_computer_score)
            compare_player(total_user_score,total_computer_score)
        else:
            print("Your final Cards are:",user_cards)
            print("Your Final Score is:",initial_user_score)
            print("Computer's final Cards are:",computer_cards)
            print("Computer's Final Score is:",initial_com_score)
            compare_player(initial_user_score,initial_com_score)
            
        repeat=input("Do you want to play one more round of BlackJack (y/n)")
    

    
    
    
    
    
