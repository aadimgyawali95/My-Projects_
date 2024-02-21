print("1) Substraction[-]")
print("2) Addition[+]")
print("3) Multiplication[*]")
print("4) Division")
a = int(input("Your choice: "))
if a==1:
    print("Substraction")
    b=int(input("Enter the minuend: "))
    c=int(input("Enter the subtrahend: "))
    d="Difference: %s"
    print(d % (b-c))
elif a==2:
    print("Addition")
    b=int(input("Enter the addend: "))
    c=int(input("Enter the addend: "))
    d="Sum: %s"
    print(d % (b+c))
elif a==3:
    print("Multiplication")
    b=int(input("Enter the multiplicand: "))
    c=int(input("Enter the multiplier: "))
    d="Product: %s"
    print(d % (b*c))
elif a==4:
    print("Division")
    b=int(input("Enter the dividend: "))
    c=int(input("Enter the divisor: "))
    d="Quotient: %s"
    e="Reminder: %s"
    print(d % (b/c))
    print(e % (b % c))

