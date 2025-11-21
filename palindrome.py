number = int(input())
n=number
reverse_num = 0
while number>0:
	digit = number%10
	reverse_num = (reverse_num *10)+digit
	number//=10
print(f" {n == reverse_num}")