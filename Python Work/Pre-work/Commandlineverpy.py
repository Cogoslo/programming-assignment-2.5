import math
import decimal
paperprice = [0, 3, 25]
mincount = 10
count = int(input("How many posters do you want, above 10  :"))
iterationcount = 0
while count < 10:
    {
print (count),
count := int(input("Must be above 10, how many do you need :"))
    }
areaH = int(input("How Tall are your posters?"))
areaW = int(input("How High are your posters"))
paperchoice =int(input("what material do you want, paper is 1, 2 is laminated, and 3 is pvc"))
paperchoice -= 1
area = 0.1
price = 0.1



while iterationcount < count:
    
    while iterationcount <= 10:
        price += (((areaH+areaW)*3)+paperprice[paperchoice])
        iterationcount += 1
    if count != 10:
        price += (((areaH+areaW)* 0.0075)+paperprice[paperchoice])
        print (price)
        iterationcount += 1


print ("the price in total is", price)

