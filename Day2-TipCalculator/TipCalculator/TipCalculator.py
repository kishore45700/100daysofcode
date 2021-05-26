#greeting message
print("welcome to tip calculator!\n")
#get the total bill amount
bill_amount=float(input("What is the total bill amount? $"))
#get the percentage of the total bill they want to offer as a tip
tip_percent=int(input("What percentage tip would you like to give? 10, 12 or 15? " ))
#get the number of people to split the bill
person_count=int(input("How many people to split the bill? "))

total_bill_amount=bill_amount+(bill_amount*tip_percent/100);
result=total_bill_amount/person_count
#ouput the results
print(f"Each person should pay: {round(result,2)}")