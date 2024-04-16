year = eval(input("Enter a 4-digit year: "))


# if year % 4 == 0 & year % 100 != 0 :
#     print("The year ", year, " is a Leap year.")
# else :
#     print("The year ", year, " is not a Leap year.")

if year % 4 == 0:
    print("The year ", year, " is a Leap year.")
else:
    print("The year ", year, " is not a Leap year,")