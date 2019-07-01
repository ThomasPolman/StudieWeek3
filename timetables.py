from random import randint

print("Hello! \n\nWe're practising some of your math skills here.\n\nThere'll be ten random multiplication questions using any number from 1 to 12. \n\nOr, if you'd like to practise a specific table, you can try your hand at that!\n\nWe'll keep a tally going.\n\nGood Luck!\n\n")
choice = input("Press 1 to do some random math, or 2 to practise a specific table: ")

good = 0
bad = 0

if choice == str(1):
    for n in range(10):
        x = randint(1, 12)
        y = randint(1, 12)
        answer = int(input("Question: " + str(x) + " x " + str(y) + " = "))
        if answer == x*y:
            print("Well done, next one\n")
            good += 1
        else:
            print("Oops\n")
            bad += 1

    print("\nYou answered %s questions correctly and %s wrong\n"%(good, bad))

elif choice == str(2):
    table = int(input("\nwhich table would you like to practise?\n"))
    print("Here we go!\n")
    for n in range(10):
        x = randint(1, 12)
        answer = int(input("Question: " + str(x) + " x " + str(table) + " = "))
        if answer == table*x:
            print("Well done, next one\n")
            good += 1
        else:
            print("Oops\n")
            bad += 1

    print("\nYou answered %s questions correctly and %s wrong.\n"%(good, bad))
