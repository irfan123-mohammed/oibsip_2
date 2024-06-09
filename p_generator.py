import random
uppercase_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters=uppercase_letters.lower()
digits="0123456789"
symbols="!@#${}[](),.;:?"
upper, lower, nums, syms=True, True, True, True
all=""
if upper:
    all+=uppercase_letters
if lower:
    all+=lowercase_letters
if nums:
    all+=digits
if syms:
    all+=symbols
length=int(input("enter length of password:"))
amount=int(input("enter amount of passwords you want:"))
for i in range(amount):
    password="".join(random.sample(all,length))
    print(password)

