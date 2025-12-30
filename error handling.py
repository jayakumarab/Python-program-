# 1. List is renamed to 'l' (lowercase L) as '1' (the number) is not a valid variable name.
l = [10, [20, 30], 15, 20, 67, 89, 95, 98, "ab"]

env_1 = []
odd_1 = []
err_items = []

try: # 2. 'try' must appear before the block of code it protects.
    for item in l: # Iterate over the corrected list name 'l'
        if type(item) == int:
            if item % 2 == 0:
                env_1.append(item)
            else:
                odd_1.append(item)
        else:
            err_items.append(item)

# 3. 'except' and 'else' blocks must be at the same indentation level as 'try'
except Exception as err:
    # 4. Corrected f-string formatting
    print(f"ERROR is: {err}")

else:
    # 5. The loop finishes without error, so the 'else' block runs.
    print("Exec is smooth!")

finally:
    # 6. Corrected f-string formatting and closing brace in the last print statement
    if err_items:
        print(f"Found bad values: {err_items}")
    print(f"Env list is: {env_1} odd list is: {odd_1}")
    