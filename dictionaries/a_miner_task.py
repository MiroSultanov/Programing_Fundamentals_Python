# You will be given a sequence of strings, each on a new line until you receive the "stop" command. Every odd line on the console represents a 
# resource (e.g., Gold, Silver, Copper, and so on) and every even - quantity. Your task is to collect the resources and print them each on a new line.
# Print the resources and their quantities in the following format:
# "{resource} -> {quantity}"
# The quantities will be in the range [1 … 2 000 000 000].


resources = {}

while True:
    command = input()
    if command == "stop":
        break
    else:
        quantity = int(input())
        if command not in resources:
            resources[command] = 0
        resources[command] += quantity

for item, quantity in resources.items():
    print(f"{item} -> {quantity}")


resources = {}
command = input()

while command != 'stop':
    quantity = int(input())
    if command not in resources:
        resources[command] = 0
    resources[command] += quantity
    command = input()
for item, quantity in resources.items():
    print(f"{item} -> {quantity}")
