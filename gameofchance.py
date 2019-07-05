import random

money = 100

def coinflip():
  bet = int(input("How much money would you like to bet on a coinflip? "))
  global money
  while bet > money:
      bet = int(input("\nYou don't have that kind of dough, my optimistic friend. Please choose again. "))
        
  
  choice = int(input("\nPress 1 for heads, 2 for tails. "))
  while choice != 1 and choice != 2:
      choice = int(input("\nPlease press 1 or 2. "))
  
  flip = random.randint(1,2)
  if flip == 1:
      print("\nIt fell to heads!")
  else:
      print("\nIt fell to tails!")
      
  if choice != flip:
    
    print("\nI'm sorry. You've lost %s computermoneys.\n"%(bet))
    
    money = money - bet
    again = int(input("Would you like to play again?\nPress 1 to restart, or 2 to quit. "))
    while again != int(1) and again != int(2):
      again = int(input("Please choose 1 to restart, or 2 to quit."))
    if again == 1:
      coinflip()
       
  else:
    
    print("\nYay! You've won %s computermoneys!\n"%(bet))
    money = money + bet
    again = int(input("Would you like to play again?\nPress 1 to restart, or 2 to quit. "))
    while again != int(1) and again != int(2):
      again = int(input("Please choose 1 to restart, or 2 to quit."))
    if again == 1:
      coinflip()
    
coinflip()
print(money)
