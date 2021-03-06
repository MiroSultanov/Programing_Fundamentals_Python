# Write a program that calculates the total cost of bought furniture. You will be given information about each purchase on separate lines until you receive the command 
# "Purchase". Valid information should be in the format: ">>{furniture_name}<<{price}!{quantity}". The price could be a floating-point or integer number.
# You should store the names of the furniture and the total price. In the end, print the name of each bought furniture and the total cost, formatted to the 
# second decimal point:
# "Bought furniture:
# {1st name}
# {2nd name}
# …
# {N name}


import re

furniture = []
total_cost = 0
expression = re.compile(r'^>>([a-zA-Z]+)<<(\d+(\.\d+)?)!(\d+)$')

while True:
    input_data = input()
    if input_data == "Purchase":
        break

    match = expression.search(input_data)
    if match:
        furniture.append(match.group(1))
        total_cost += float(match.group(2)) * int(match.group(4))

print("Bought furniture:")

for item in furniture:
    print(item)
print(f"Total money spend: {total_cost:.2f}")

