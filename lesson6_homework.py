# 1.change
def change(total, cash, discount):
    return cash - (total - (total * discount / 100))

total = float(input("Enter total>>>"))
cash = float(input("Enter cash>>>"))
discount = float(input("Enter discount (%)>>>"))
print("change =", change(total, cash, discount))



# 2. fan mode
def fan(mode):
    if mode == 0:
        print("switched off")
    if mode == 1:
        print("speed 1")
    if mode == 2:
        print("speed 2")
    if mode == 3:
        print("turbo mode")

mode = int(input("Enter mode (0-3)>>>"))
fan(mode)



# 3. my age
def my_age(age):
    if age < 18:
        print("child")
    if age >= 18 and age <= 67:
        print("adult")
    if age > 67:
        print("senior")

age = int(input("Enter age>>>"))
my_age(age)
