# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
print(names)
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
names_len = len(names)

choice_name = random.randint(0, names_len -1)
whopays = names[choice_name]
print(whopays+ " will pay for our meal today")