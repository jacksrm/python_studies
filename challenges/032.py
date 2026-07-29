year = int(input("Input a year: "))
div_4 = year % 4 == 0
div_100 = year % 100 == 0
div_400 = year % 400 == 0
leap_year = div_4 and (not div_100 or div_400)


print(f"{year} is {'not ' if not leap_year else ''}a Leap Year!")
