
Number = 100
prime = []
Nonprime = []
for num in range(2,Number+1):
    flag = True
    for i in range(2,num):
        if num % i == 0:
            flag = False
    if flag:
        prime.append(num)
    else:
        Nonprime.append(num)
print("The prime Numbers",prime)
print("The non-prime Numbers",Nonprime)





