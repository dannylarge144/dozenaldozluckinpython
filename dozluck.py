import math
import random

def dozenalise(intDec):
  strdoz = ""
  intpow = 3
  boolfsf = True
  while intpow > -1:
    intdigit = (math.floor(intDec/12**intpow))
    strdigit = str(intdigit)
    if (intdigit != 0) or (not boolfsf) or (intpow == 0):
      if intdigit == 10:
        strdigit = "X"
      if intdigit == 11:
        strdigit = "E"
      intDec -= intdigit*(12**intpow)
      strdoz += strdigit
      boolfsf = False
    intpow -= 1
  return strdoz

print("Are you more lucky than a computer?")
print("Let's find out.")
input("Press enter to continue")
print('')
print("All numbers in this game are represented in dozenal.")
print("I am going to roll a dice with 100 sides. Each round I will roll it twice, once for me and once for you.")
print("Scores will be accumulative, your roll will be added to your other rolls.")
print("We will play 10 rounds, the highest score at the end of the 10 rounds will win.")
print("If you roll a prime number, you will be awarded an extra roll.")
print("If your final score is divisible by 10, your total score will double.")
input("Press enter to indicate your readiness:")
print("Good. Now we begin:")
print('')
intLives=12
intPlayT=0
intCompT=0
listPrimes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139]
while intLives != 0:
 intComp=int(random.randint(1, 144))
 intPlay=int(random.randint(1,144))
 print("I have rolled " + dozenalise(intComp) + ", and you have rolled " +dozenalise(intPlay)+".")
 intCompT += intComp
 intPlayT += intPlay
 boolPrimeC=False
 boolPrimeP=False
 for x in listPrimes:
  if x==intComp:
   boolPrimeC=True
  if x==intPlay:
   boolPrimeP=True
 if boolPrimeC and boolPrimeP:
  print("As both of our numbers are prime, we both get an additional roll.")
  intCompB=int(random.randint(1, 144))
  intPlayB=int(random.randint(1,144))
  print("I have rolled " + dozenalise(intCompB) + ", and you have rolled " + dozenalise(intPlayB) +".")
  intPlayT += intPlayB
  intCompT += intCompB
  intPlay += intPlayB
  intComp += intCompB
 elif boolPrimeC:
  print("As my number is prime, that neans I get an extra roll.")
  intCompB=int(random.randint(1,144))
  print("I have rolled " + dozenalise(intCompB) +".")
  intCompT=intCompT+intCompB
  intComp=intComp+intCompB
 elif boolPrimeP:
  print("As your number is prime, that means you get an extra roll.")
  intPlayB=int(random.randint(1,144))
  print("You have rolled " + dozenalise(intPlayB) +".")
  intPlayT += intPlayB
  intPlay += intPlayB
 if intPlay>intComp:
  print("Which, of course, means you have won this round.")
 elif intPlay<intComp:
  print("That means I have won this round.")
 else:
  print("It appears to be a draw this time.")
 print("This means in total, I have " + dozenalise(intCompT) +" points, and you have " + dozenalise(intPlayT) +" points.")
 if intPlayT > intCompT:
  print("Which puts you in the lead.")
  print("For now.")
 elif intPlayT<intCompT:
  print("Which means that I am winning.")
 else:
  print("Which means that we are currently drawing.")
 intLives -= 1
 input("Press enter to continue:")
 print('')
print("And thus, the 10 rounds are over.")
boolTwelveP=False
boolTwelveC=False
if (intPlayT % 12) == 0:
  boolTwelveP=True
if (intCompT % 12) == 0:
  boolTwelveC=True
if boolTwelveP and boolTwelveC:
 print("Consider both our scores doubled.")
 intPlayT=intPlayT*2
 intCompT=intCompT*2
elif boolTwelveP:
 print("Consider your score doubled.")
 intPlayT=intPlayT*2
elif boolTwelveC:
 print("Consider my score doubled.")
 intCompT=intCompT*2
print("")
if intCompT == intPlayT:
 print("And, as both you and I have "+ dozenalise(intCompT) + " points, it appears that we have drawn.")
 print("Unnacceptable.")
 print('')
 intComp=int(random.randint(1,144))
 print("I have rolled "+ dozenalise(intComp) +".")
 input("Press enter to decide your fate.")
 intPlay=int(random.randint(1,144))
 print("You have rolled "+ dozenalise(intPlay)+".")
 print("")
 intCompT += intComp
 intPlayT += intPlay
 if intPlay==intComp:
  print("So it appears we truly have drawn.")
if intCompT>intPlayT:
 print("And as you have "+dozenalise(intPlayT) +" and I have "+ dozenalise(intCompT)+", that means I have won")
 print("So, no, you are not luckier than a computer.")
elif intCompT<intPlayT:
 print("And as you have "+ dozenalise(intPlayT)+" and I have " + dozenalise(intCompT)+", that means you have won.")
 print("So I suppose you are luckier than a computer.")
 print("Congrats.")
print("")
print("Good game, player.")