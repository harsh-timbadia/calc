n = int(input("enter the 1st number: "))
m = int(input("enter the 2nd number: "))
#only for 2 numbers 
print('what you want to do ?')
choice = input('choose an opreator (+,-,*,/,//,%): ')

if choice == '+':
    print(f"n + m = {n + m}")
elif choice == '-':
    print(f"n - m = {n - m}")
elif choice == '*':
    print(f"n * m = {n * m}")
elif choice == '/':   # Fixed: added '=='
    print(f"n / m = {n / m}")
elif choice == '//':  # Fixed: added '=='
    print(f"n // m = {n // m}")
elif choice == '%':
    print(f"n % m = {n % m}")
else:
    print("enter valid input ")