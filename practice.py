import random
balance=100
def spin_row():
    symbols=['🍕','🍔','🍟','🌭']
    return[random.choice(symbols) for _ in range(3)]
def print_row(row):
     print(row)

def get__payout(bet,row):
    if row[0]==row[1]==row[2]:
        if row[0]=='🍕':
            return bet *3
        if row[0]=='🍔':
            return bet*4
        if row[0]=='🍟':
            return bet*5
        if row[0]=='🌭':
            return bet*6
    return 0        
while balance!=0:
    print()
    print("...........................")
    print("WELCOME TO PYTHON SLOT GAME")
    print("............................")
    print(f"YOUR CURRENT BALANCE IS RS{balance}")
    bet=input("ENTER THE AMOUNT YOU WANT TO BET :")
    bet=int(bet)
    if bet>balance:
        print("THIS ACTION CANT BE DONE!")
    elif bet<0:
        print("CAN'T TAKE NEGATIVE AMOUNT!")
    else:
         balance-=bet
    print("...SPINNING...")
    row=spin_row()
    print_row(row)
    get__payout(bet,row)
    payout=get__payout(bet,row)
    if payout>0:
        print(f"YOU WON RS.{payout}!")
    else:
        print("SORRY YOU HAVE LOST !")
    balance+=payout
    play_again=input("DO YOU WANT TO PLAY AGAIN ? (Y OR N)").lower()
    if play_again=='n':
        break
print("THANKS FOR PLAYING !")


  
    