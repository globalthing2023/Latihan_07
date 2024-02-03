funny = int( input("Please insert a number between(10-15, 20-25 or 35-40) :"))
good = "good"
bad = "bad"
while ( 16 <= funny <= 19 or 26 <= funny <= 34 or funny >= 41 ):
    print("Please try again, you are yet to authorise with the right number")
    funny = int( input("Please insert a number between :(10-15, 20-25 or 35-40) :"))
else:
    print("cool")