#coin sorting challenge

#The country of Examplania has coins that are worth 1, 5, 10, 25, 100, and 500 currency units. At the Zeroth Bank of Examplania, you are trained to make various amounts of money by using as many ¤500 coins as possible, then as many ¤100 coins as possible, and so on down.

#For instance, if you want to give someone ¤468, you would give them four ¤100 coins, two ¤25 coins, one ¤10 coin, one ¤5 coin, and three ¤1 coins, for a total of 11 coins.

#Write a function to return the number of coins you use to make a given amount of change.

#change(0) => 0
#change(12) => 3
#change(468) => 11
#change(123456) => 254

change_1 = 0
change_2 = 12
change_3 = 468
change_4 = 123456

coin_list = [500, 100, 25, 10, 5, 1]

def coinSorter(change):
    number_of_coins = 0
    for coin in coin_list:
        number_of_coins = number_of_coins + (change // coin)
        change = (change % coin)
    print(number_of_coins)

coinSorter(change_1)
coinSorter(change_2)
coinSorter(change_3)
coinSorter(change_4)