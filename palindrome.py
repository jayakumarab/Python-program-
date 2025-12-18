# palindrome 

original_number = int(input("Enter a number: "))
reversed_number = 0
n = original_number
while n > 0 :
    digit = n % 10
    reversed_number = (reversed_number * 10) + digit
    n //= 10

if original_number== reversed_number :
    print(f"The given Number {original_number} is Palindrome")
else:
    print(f"The given Number{original_number} not palindrome")
