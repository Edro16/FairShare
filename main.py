print("FairShare: This program lets you split the bill, calculate the tip, and split it as well.")
print("-- Made by Edro ;) --")

bill = float(input("\n> How much is the bill?: $"))
bill_contributors = int(input("> How many people are going to contribute to the bill: "))
tip_contributors = 0
if input("> Would you like to tip? y or n: ") == "y":
    tip_contributors = int(input("> How many people are going to contribute to the tip as well: "))
    tip_percentage = float(input("> What tip percentage would you like to give (Example: 10, 15, 30): "))
    tip = bill * tip_percentage / 100
    tip_split = tip / tip_contributors
bill_split = bill / bill_contributors

if tip_contributors == 0:
    print(f"\nEach person should pay: ${bill_split}")
elif tip_contributors != bill_contributors:
    print(f"\nEach non-tipper should pay: ${bill_split}")
    print(f"Each tipper should pay: ${bill_split + tip_split}")
else:
    print(f"\nEach person should pay: ${bill_split + tip_split}")



