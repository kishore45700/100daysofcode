#get the user's age as input
age=int(input("what's your age?\n"))

days=(90-age)*365
months=(90-age)*12
weeks=(90-age)*52

print(f"You have {days} days, {weeks} weeks, {months} months left.")