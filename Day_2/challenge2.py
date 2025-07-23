first_name = input("What is your first name?\n")

last_name = input("What is your last name?\n")

full_name = first_name + ' ' + last_name

amount_sold = round(float(input("How much have you sold this month?\n")),2)

print()

print(f"{full_name}... You are entitled to ${amount_sold*0.13}")