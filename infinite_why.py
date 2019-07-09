# Infinite why program
# Demonstrates the while loop

print("Welcome to the'Infinite Why program'\n")
print("This program keeps asking you why until you can't answer anymore")
print("Happy thinking!\n\n")

# Input your own question here
statement = input("Enter your statement: ")
print(statement)

response = ""

# The exit phrase is the word Just
while response != "Just":
	response = input("Why?\n")

print("Oh,Okay")

input("\n\nPress the enter key to exit.")
