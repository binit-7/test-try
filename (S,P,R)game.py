import random
options=["scissors","paper","rock"]
while True:
    user=input("Enter any (Scissors,Paper,Rock) :").lower()
    if user not in options:
        print ("INVALID OPTION !")
        continue
    computer=random.choice(options)
    print(f"USER: {user}")
    print(f"COMPUTER: {computer}")
    if user==computer:
        print("TIE !")
    if user=='rock' and computer=='scissors':
        print("YOU WON 😉!")
    if user=='paper' and computer=='rock':
        print("YOU WON 😉!")
    if user=='scissors' and computer=='paper':
        print("YOU WON 😉!")
    else:
        print("YOU LOSE 😔!")
    play_again=input("DO YOU WANT TO PLAY AGAIN (Y/N) ?").lower()
    if play_again=='n':
        break
print("THANKS FOR PLAYING..😊")