
#This program calculates the end of year bonus a customer receives on their loyalty card. The bonus is calculated with the following formula:

#If there are less than a hundred points on the card, the bonus is 10 % In any other case the bonus is 15 % The program should work like this:

#Sample output How many points are on your card? 55 Your bonus is 10 % You now have 60.5 points

#But there is a problem with the program, so with some inputs it doesn't work quite right:

#Sample output How many points are on your card? 95 Your bonus is 10 % Your bonus is 15 % You now have 120.175 points
points = float(input("How many points are on your card? "))
bonus = float(input("Your bonus is "))

if points < 100 :
  bonus = .1 * points
  totalInCard = points + bonus
  print(f"You now have {totalInCard} points ")


else:
  bonus = .15* points
  totalInCard = points + bonus
  print(f"You now have {totalInCard} points ")









