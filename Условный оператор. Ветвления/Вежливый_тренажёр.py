print("Identify yourself, please!")
name = input()

print("Enter the text.")

text = input()

print("Repeat the text.")

if input() == text:
    print(f"{name}, entered correctly!")
    
else:
    print(f"{name}, it didn't work out yet, try again!")