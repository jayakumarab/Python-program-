# Configuration
n_terms = 10 # Change this to the numberof terms you want

# Initialization
n1, n2 = 0, 1

print(f"Fibonacci sequence up to {n_terms} terms:")

if n_terms <= 0:
    print("Invalid number of terms. Please enter a positive integer.")
else:
    # The for loop iterates a fixed number of times
    for i in range(n_terms):
        print(n1, end=' ')
        
        # Calculate and update the terms
        n1,n2 =n2, n1 + n2
        