# README:
#  * Edit this file where noted to complete exercises.
#  * DO NOT change function names or your code will not pass test cases.
#  * Output must match the reference solution's output EXACTLY, examples of
#    reference solution output will be provided throughout the document.

# Exercise 2-6
# PROMPT(S) (Example user input of '100'):
'''
Enter the amount of the purchase: 100
'''
# OUTPUT:
'''
Purchase Amount: 100.00
State Tax: 5.00
County Tax: 2.50
Total Tax: 7.50
Sale Total: 107.50
'''
def sales_tax():
	_price = float(input("Enter the amount of the purchase: "))
	state_tax = 0.05
	county_tax = 0.025
	spt = _price * state_tax
	cpt = _price * county_tax
	print("County tax:",cpt)
	print("State tax:",spt)
	print("Total tax:",spt + cpt)
	print("Sale Total:",_price + spt + cpt)



# Exercise 2-14
# PROMPT(S) (Example user input of '100', '5', '12', and '10'):
'''
Enter the starting principal: 100
Enter the annual interest rate: 5
How many times per year is the interest compounded? 12
For how many years will the account earn interest? 10
'''
# OUTPUT:
'''
At the end of 10 years you will have $ 164.70
'''
def compound_interest():
	# your code here
	P = float(input("Enter the starting principal:"))
	r = float(input("Enter the annual interest rate:"))
	n = float(input("How many times per year is the interest compounded:"))
	t = float(input("For how many years will the account earn interest:"))
	_rate = r / 100
	_par = _rate/n
	_add = _par + 1
	_exponent = n * t
	_math = _add**_exponent
	A = _math * P
	print( "At the end of", t, "years you will have $", A,)


# Exercise 3-10
# PROMPT(S) (Example user input of '100', '5', '10', and '4'):
'''
Enter the number of pennies: 100
Enter the number of nickels: 5
Enter the number of dimes: 10
Enter the number of quarters: 4
'''
# OUTPUT (Less than one dollar):
'''
Sorry, the amount you entered was less than one dollar.
'''
# OUTPUT (More than one dollar):
'''
Sorry, the amount you entered was more than one dollar.
'''
# OUTPUT (Exactly one dollar):
'''
Congratulations!
The amount you entered was exactly one dollar!
You win the game!
'''
def dollar_game():
	_pennies = float(input("Enter the number of pennies: "))
	_nickels = float(input("Enter the number of nickels: "))
	_dimes = float(input("Enter the number of dimes: "))
	_quarters = float(input("Enter the number of quaters: "))
	xpen = 1 / 100
	xnick = 1 / 20
	xdime = 1 / 10
	xquart = 1 / 4
	ypen = _pennies * xpen
	ynick = _nickels * xnick
	ydime = _dimes * xdime
	yquart = _quarters * xquart
	total = yquart + ydime + ynick + ypen
	if total == 1:
		print('''Congratulations!
The amount you entered was exactly one dollar!
You win the game!''') 
	if total < 1:
		print("Sorry, the amount you entered was less than one dollar.")
	if total > 1:
		print("Sorry, the amount you entered was more than one dollar.")# your code here


# Exercise 3-12
# PROMPT(S) (Example user input of '10'):
'''
Enter the number of packages purchased: 10
'''
# OUTPUT:
'''
Discount Amount: $ 99.00
Total Amount: $ 891.00
'''
def quantity_discount():
	# your code here
	_price = 99
	_packages = float(input("Enter the number of packages purchased:"))
	_totalcost = _price * _packages
	if _packages < 10:
		_costnodiscount = _totalcost * _packages
		print("No discount")
		print("Total price: $",_costnodiscount)
	if _packages >= 10 and _packages <= 19:
		_discountA = 1 / 10
		_totaldiscountA = _discountA * _totalcost
		_newpriceA = _totalcost - _totaldiscountA
		print("Discount Amount: $",_totaldiscountA,)
		print("Total Price: $",_newpriceA)
	if _packages >= 20 and _packages <= 49:
		_discountB = 2 / 10
		_totaldiscountB = _discountB * _totalcost
		_newpriceB = _totalcost - _totaldiscountB
		print("Discount Amount: $",_totaldiscountB,)
		print("Total Price: $",_newpriceB)
	if _packages >= 50 and _packages <= 99:
		_discountC = 3 / 10
		_totaldiscountC = _discountC * _totalcost
		_newpriceC = _totalcost - _totaldiscountC
		print("Discount Amount: $",_totaldiscountC,)
		print("Total Price: $",_newpriceC)
	if _packages >= 100:
		_discountD = 4 / 10
		_totaldiscountD = _discountD * _totalcost
		_newpriceD = _totalcost - _totaldiscountD
		print("Discount Amount: $",_totaldiscountD,)
		print("Total Price: $",_newpriceD)

# Exercise 3-13
# PROMPT(S) (Example user input of '10'):
'''
Enter the weight of the package: 10
'''
# OUTPUT:
'''
Shipping charge: $ 4.00
'''
def shipping_charge():
	# your code here
	_weightofpackage = float(input("Enter the weight of the package:"))
	if _weightofpackage <= 2:
		_costA = _weightofpackage * 1.5
		print("Shipping charge: $", _costA)
	if _weightofpackage > 2 and _weightofpackage <= 6:
		_costB = _weightofpackage * 3
		print("Shipping charge: $",_costB)
	if _weightofpackage > 6 and _weightofpackage <= 10:
		_costC = _weightofpackage * 4
		print("Shipping charge $:",_costC)
	if _weightofpackage > 10:
		_costD = _weightofpackage * 4.75
		print("Shipping charge: $",_costD)

# Exercise 4-3
# PROMPT(S) (Example user input of '10', '5', and '0'):
'''
Enter amount budgeted for the month: 10
Enter an amount spent(0 to quit): 5
Enter an amount spent(0 to quit): 0
'''
# OUTPUT (Under budget):
'''
Budgeted: $ 10.00
Spent: $ 5.00
You are $ 5.00 under budget. WELL DONE!
'''
# OUTPUT (Matching budget):
'''
Budgeted: $ 10.00
Spent: $ 10.00
Spending matches budget. GOOD PLANNING!
'''
# OUTPUT (Over budget):
'''
Budgeted: $ 10.00
Spent: $ 15.00
You are $ 5.00 over budget. PLAN BETTER NEXT TIME!
'''
def budget_analysis():
	# your code here
	#assigning value to the budget
	_theBudget = input("Enter amount budgeted for the month: ")
	_theBudget = float(_theBudget)

	#assigning value to the expense and calling for input
	_theSpent = 1
	total = 0
	while _theSpent != 0:
		_theSpent = input("Enter an amount spent(0 to quit):")
		_theSpent = float(_theSpent)
		total = _theSpent + total
	#calculating the money leftover	 
	_Expense = _theBudget - total 
	#returning result from equation
	if _Expense == 0:
		print("Budgeted: $",_theBudget)
		print("Spent: $",_theBudget)
		print ("Spending matches budget. GOOD PLANNING!")
	if _Expense < 0:
		print("Budgeted: $",_theBudget)
		print("Spent: $",total)
		print("You are $",abs(_Expense)," over budget. PLAN BETTER NEXT TIME !")
	if _Expense > 0:
		print("Budgeted: $",_theBudget)
		print("Spent: $",total)
		print("You are $",_Expense," under budget. WELL DONE!")


# Exercise 4-5
# PROMPT(S) (Example user input of '1', '1', '2', '3', '4', '5', '6', '7',
# 	'8', '9', '10', '11', '12'):
'''
Enter the number of years: 1
For year  1 :
Enter the rainfall amount for the month: 1
Enter the rainfall amount for the month: 2
Enter the rainfall amount for the month: 3
Enter the rainfall amount for the month: 4
Enter the rainfall amount for the month: 5
Enter the rainfall amount for the month: 6
Enter the rainfall amount for the month: 7
Enter the rainfall amount for the month: 8
Enter the rainfall amount for the month: 9
Enter the rainfall amount for the month: 10
Enter the rainfall amount for the month: 11
Enter the rainfall amount for the month: 12
'''
# OUTPUT:
'''
For  12 months
Total rainfall:  78.00 inches
Average monthly rainfall:  6.50 inches
'''
def average_rainfall():
	# your code here
	totalMonths = 0
	_totalRainInches = 0

	userInputYears = int(input("Enter the number of years: "))

	for currentYear in range( 1, userInputYears + 1):
		print("For year: ", currentYear)
		for currentMonth in range( 1, 13):
			rainfallPerMonth =(input("Enter the rainfall amount for the month: ", ))
			rainfallPerMonth = float(rainfallPerMonth)
			_totalRainInches = _totalRainInches + rainfallPerMonth
			totalMonths = totalMonths + 1

	AverageRain = _totalRainInches / totalMonths
	print( "For ", totalMonths ," months" )
	print( "Total rainfall: ", _totalRainInches ,"inches")
	print( "Averege monthly rainfall: ", AverageRain ,"inches")
# Exercise 4-12
# PROMPT(S) (Example user input of '10'):
'''
Enter a nonnegative integer: 10
'''
# OUTPUT:
'''
The factoral of 10 is 3628800
'''
def factorial():
	# your code here
	number = int(input( "Enter a nonnegative integer: " ))

	factorial = 1

	for math in range(1, number + 1 ):
		factorial = factorial * math

	print( "The factorial of ", number, "is ", factorial) 

# Exercise 4-12
# PROMPT(S) (Example user input of 'python'):
'''
Enter the string to be converted to Morse code: python
'''
# OUTPUT:
'''
--.-,--..,..-,..,.--.,---,
'''
def morse_code():
	# your code here
	CODE ={ 'A': '.-',              'a': '.-',
        'B': '-...',            'b': '-...',
        'C': '-.-.',            'c': '-.-.',
        'D': '-..',             'd': '-..',
        'E': '.',               'e': '.',
        'F': '..-.',            'f': '..-.',
        'G': '--.',             'g': '--.',
        'H': '....',            'h': '....',
        'I': '..',              'i': '..',
        'J': '.---',            'j': '.---',
        'K': '-.-',             'k': '-.-',
        'L': '.-..',            'l': '.-..',
        'M': '--',              'm': '--',
        'N': '-.',              'n': '-.',
        'O': '---',             'o': '---',
        'P': '.--.',            'p': '.--.',
        'Q': '--.-',            'q': '--.-',
        'R': '.-.',             'r': '.-.',
        'S': '...',             's': '...',
        'T': '-',               't': '-',
        'U': '..-',             'u': '..-',
        'V': '...-',            'v': '...-',
        'W': '.--',             'w': '.--',
        'X': '-..-',            'x': '-..-',
        'Y': '-.--',            'y': '-.--',
        'Z': '--..',            'z': '--..',}
	name = input("Enter the string to be converted to Morse code: " )
	space = " "

	for char in name:
		if char in CODE:
			space +=CODE[char] + ""
		else: 
			space += " "
	
	print(space)


# *** DO NOT EDIT BELOW THIS POINT ***
# This part of the file is for testing purposes.
# Your code WILL FAIL the test cases if this is edited.
def main():
	# run each exercise
	sales_tax()
	compound_interest()
	dollar_game()
	quantity_discount()
	shipping_charge()
	budget_analysis()
	average_rainfall()
	factorial()
	morse_code()

if __name__=="__main__":
	main()