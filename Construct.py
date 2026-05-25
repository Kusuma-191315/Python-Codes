#if statemnet
age = 13 #if you give value as 18+ it will show o/p as eligible thankyou
if age>=18:
    print("Eligible to vote") 
print("ThankYou")

#else statemnet
age = 23 #if you give value as 18+ it will show o/p as eligible thankyou
if age>=18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")
print("ThankYou")

#elif statemant (if - elif - else)
marks = 75
if marks>=90:
    print("Grade A")
elif marks>=70:
    print("Grade B")
elif marks>=50:
    print("Grade C")
else:
    print("Fail")

#Nested if statement
free_tonight = True
friends_available = False

if free_tonight:
    if friends_available:
        print("Go out for dinner with friends!")
    else:
        print("Order food and watch movie.")
else:
        print("Continue with assignments.")

#Match statement
month = 15
match month:
    case 3 | 4 | 5:
        print("Summer")
    case 6 | 7 | 8:
        print("Rainy")
    case 9 | 10 | 11 | 12:
        print("Winter")
    case _ :
        print("Invalid season")

#Match 
day = 6
match day:
    case 1: print("Mon")
    case 2: print("Tue")
    case 3: print("Wed")
    case 4: print("Thurs")
    case 5: print("Fri")
    case 6: print("Sat")
    case _: print("Invalid day")