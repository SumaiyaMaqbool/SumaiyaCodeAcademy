

Amount_Iron = int(input("Please enter how much iron you want to purchase? Please know that one iron costs 1 R.O. and 5% VAT are included in the total cost"))

Iron_Cost = float(1 * Amount_Iron)

VAT = Iron_Cost * float(5/100)

Total_cost = Iron_Cost + VAT

print("Your iron cost is: ", format((Iron_Cost), '.3f') + " R.O." + "Tax Cost is: ",format((VAT), '.3f')+ " You total cost is: ", format((Total_cost), '.3f'))