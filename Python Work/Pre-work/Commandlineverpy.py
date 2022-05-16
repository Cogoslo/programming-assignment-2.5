import math
import decimal
paperprice = [0, 3, 35]
mincount = 10
count = int(input("How many posters do you want, above 10  :"))
iterationcount = 1
while count < 10:
    {
print (count),
count := int(input("Must be above 10, how many do you need :"))
    }
areaW = int(input("How Width are your posters?"))
areaH = int(input("How High are your posters"))
paperchoice =int(input("what material do you want, paper is 1, 2 is laminated, and 3 is pvc:"))
paperchoice -= 1
area = decimal
price = decimal
area = 0
price = 0
while iterationcount < count:

    while iterationcount <= 10:
        price = price + (((areaH+areaW)*0.03)+paperprice[paperchoice])
        iterationcount += 1
    if count >= 9:
        price = price + (((areaH+areaW)*0.0075)+paperprice[paperchoice])
        iterationcount += 1


print ("the price in total is", (round(price, 1)))
