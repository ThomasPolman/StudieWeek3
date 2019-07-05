import random

money = 100

print("Welcome to Thomas' casino extravaganza!\n\nLose all your money here!\n\nPossibly you'll win some but we all know that's not very likely.\n")
print("This is no ordinary casino. We'll start you off with a 100 buckeroos. \nUse at your discretion.")
print("\nWe'll keep you posted on your credit line throughout, like this: ")
print("You have %s computermoneys left.\nOur purpose is to take this all away from you."%(money))
input("\nDon't resist too hard.")
input("\nYou'll lose eventually.")
input("\nIt's scientifically proven.")
input("\nIt'll be much less grindy if you just bet it all on the first go.")
input("\nDo a roullette.")
input("\nBet it all on 30.")
input("\nDone.")
input("\nGet on with our lives.")
input("\nHave fun!!")


def main_menu():
  choice = int(input("\nAt present we have four games available for you.\nPlease press the corresponding number to start your exciting journey to bankruptcy!\n1 - Flip a coin\n2 - Chõ-Han\n3 - Boxing day\n4 - Roullette.\nMake your choice here:  "))
  while choice != 1 and choice != 2 and choice != 3 and choice != 4:
    choice = int(input("Please choose from the provided list. "))

  if choice == 1:
    coinflip()
  if choice == 2:
    cho_han()
  if choice == 3:
    boxing_day()
  if choice == 4:
    roullette()

      
# Repeated functions

def again():
  global money
  if money == 0:
    return print("\nWe've warned you. Byebye and thank you for the computermoneys.")
  print("\nYou have %s computermoneys left."%(money))
  one_more_time = int(input("Would you like to play again?\nPress 1 to restart, 2 to quit or 3 to play another game. "))
  while one_more_time != 1 and one_more_time != 2 and one_more_time != 3:
    one_more_time = int(input("Please choose 1 to restart, 2 to quit or 3 for the main menu."))
  if one_more_time == 1:
    return True
  if one_more_time == 3:
    main_menu()
  else:
    print("\nYou quit the game with %s computermoneys left! We were supposed to have that!"%(money))
    return False

def bet():
  value = int(input("How much money would you like to bet? "))
  global money
  while value > money:
      value = int(input("\nYou don't have that kind of dough, my optimistic friend. Please choose again. "))
  return value

# Games

def coinflip():

  print("\nFlip a coin, win a prize!\n")
  global money
  bet_value = bet()
  
  choice = int(input("\nPress 1 for heads, 2 for tails. "))
  while choice != 1 and choice != 2:
      choice = int(input("\nPlease press 1 or 2. "))
  
  flip = random.randint(1,2)
  if flip == 1:
      print("\nIt fell to heads!")
  else:
      print("\nIt fell to tails!")
      
  if choice != flip:
    print("\nI'm sorry. You've lost %s computermoneys.\n"%(bet_value))
    money = money - bet_value
    if again():
      coinflip()
       
  else:
    
    print("\nYay! You've won %s computermoneys!\n"%(bet_value))
    money = money + bet_value
    if again():
      coinflip()

    
def cho_han():

  print("\nRoll the dice, get the prize! Bet on an even or odd number.\n")
  global money
  bet_value = bet()

  choice = int(input("\nPress 1 for even, 2 for odds. "))
  while choice != 1 and choice != 2:
      choice = int(input("\nPlease press 1 or 2. "))

  roll = random.randint(1,12)
  if roll % 2 == 0:
    print("\nIt rolled an even number!")
  else:
    print("\nIt rolled an odd number!")

  if choice == 1 and roll % 2 == 0:
    print("\nYou've won %s computermoneys!"%(bet_value))
    money = money + bet_value
    if again():
      cho_han()

  else:
    print("\nI'm sorry. You've lost %s computermoneys.\n"%(bet_value))
    money = money - bet_value
    if again():
      cho_han()


def boxing_day():
  print("\nTwo cards will be drawn. One for you, one for the dealer.\nThe highest card wins the bet.\n")
  global money
  bet_value = bet()
  
  deck_values = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
  deck_signs = ['Hearts', 'Tiles', 'Pikes', 'Clovers']
  deck = [[value, sign] for value in deck_values for sign in deck_signs]
  random.shuffle(deck)

  random_pick1 = deck.pop(0)
  random_pick2 = deck.pop(0)
  value1 = random_pick1[0]
  value2 = random_pick2[0]

  if value1 == 'Jack':
    value1 = int(11)
  elif value1 == 'Queen':
    value1 = int(12)
  elif value1 == 'King':
    value1 = int(13)
  elif value1 == 'Ace':
    value1 = int(14)
  else:
    value1 = int(random_pick1[0])

  if value2 == 'Jack':
    value2 = int(11)
  elif value2 == 'Queen':
    value2 = int(12)
  elif value2 == 'King':
    value2 = int(13)
  elif value2 == 'Ace':
    value2 = int(14)
  else:
    value2 = int(random_pick2[0])

  print("\nYou drew: %s"%(random_pick1))
  print("The dealer drew: %s"%(random_pick2))

  if value1 > value2:
    print("\nYou won! You get %s computermoneys!"%(bet_value))
    money = money + bet_value
    if again():
      boxing_day()
        
  elif value2 > value1:
    print("\nYou lost! You lose %s computermoneys!"%(bet_value))
    money = money - bet_value
    if again():
      boxing_day()
        
  else:
    print("\nIt's a tie! Lose nothing, gain nothing.")
    if again():
      boxing_day()

  
def roullette():

  print("\nGet ready for some roulette!\nYou can choose an odd or even number, and double your return on a win.")
  print("Ofcourse, you can also bet on any number between 1 and 36.\nYou'll return 35 times your bet on a win!")
  global money
  
  choice = int(input("\nPress 1 to bet on odd/even or 2 to bet on a number. "))
  while choice != 1 and choice != 2:
    choice = int(input("Please press 1 for odd/even or 2 for a specific number. "))

  if choice == 1:
    
    bet_value = bet()
    odd_even = int(input("\nPlease press 1 for even or 2 for odd. "))
    while odd_even != 1 and odd_even != 2:
      odd_even = int(input("Please press 1 or 2. "))
      
    roll = random.randint(1,36)
    if roll % 2 == 0:
      print("\nIt hit an even number!")
    else:
      print("\nIt hit an odd number!")

    if odd_even == 1 and roll % 2 == 0:
      print("\nYou've won %s computermoneys!"%(bet_value))
      money = money + bet_value
      if again():
        roullette()

    else:
      print("\nI'm sorry. You've lost %s computermoneys.\n"%(bet_value))
      money = money - bet_value
      if again():
        roullette()

  else:
    
    bet_value = bet()
    number = int(input("\nWhich number would you like to bet on? "))
    while number < int(1) or number > int(36):
      number = int(input("\nPlease choose between 1 and 36. "))

    roll = random.randint(1,36)
    print("\nIt rolled %s!"%(roll))
    if roll == number:
      money = money + (bet_value * 35)
      print("\nAmazing!!! You're rich, baby.")
      if again():
        roullette()
    else:
      money = money - bet_value
      print("\nToo bad. What were you expecting though? ")
      if again():
        roullette()
    
main_menu()

