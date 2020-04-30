import random

def Rand(start, end, num): 
    res = [] 
  
    for j in range(num): 
        res.append(random.randint(start, end)) 
  
    return res 


print("select two numbers from 1 to 6")

bet = input("Enter bet amount: ")
number1 = input("Enter value and press enter: ")
number2 = input("Please enter second number: ")

print("Ok, now lets randomize!")

print("your values are: " + number1 + " and " + number2)

values = Rand(1,6,6)

print("random values generated: " ,values)

def doub(t):
	lst =[]
	for i in range(0,len(t)):
		for j in range(i+1, len(t)):
			if t[i] ==t[j]:
				lst.append(t[i])
	print(lst)

doub(values)

for k in lst:
	if k == number1 or k==number2:
		profit = 2 * bet
		print("You won ",profit)
	elif k == number1 and k == number2:
		profit = 4 * bet
		print("you won ",profit)
	
	print("No one wins!")


