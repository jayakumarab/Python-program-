#password authentication programming
password = "Abc@123"
ul=0
lo =0
so =0

for item in password:
    if  item.isdigit():
        ul += 1
    elif  item.isalpha():
        lo += 1
    elif not item.isalnum():
        so += 1
if ul>=1 and lo>=1 and so>=1:
    print("password set successfully")
else:
    print("password not set successfully")
