#User greeting

print("Welcome to the tip calculator!")

# Inputs

bill_to_pay = input("What was the total bill? $")
tip_perc = input("What percentage tip would you like to give?:\n")
people = input("How many people to split the bill?:\n")

# Format inputs to corresponding data type

bill_num = float(bill_to_pay)
tip_num = int(tip_perc)
people_num = int(people)

#Each person should pay (bill / people) * tip percentage = bill with the tip

full_tip = bill_num * tip_num / 100
bill_with_tip = bill_num + full_tip
each_person = bill_with_tip / people_num

#Format the result to 2 decimal places = 33.60

final_amount = round(each_person, 2)
final_amount = "{:.2f}".format(each_person)

# Show the result to the user

print(f"Each person should pay: {final_amount} dollars.")