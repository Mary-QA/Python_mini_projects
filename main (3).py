#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
	 
#Write the rest of your code below this line 👇
x= random.randint(0,1)
if x == 1:
    print(f"Heads")
else:
    print(x)
    print("Tails")