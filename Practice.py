
# Example 1: User Input
name = input("Enter your name: ")
print("Hello, " + name + "!")

# Example 2: Integer Input
age = int(input("Enter your age: "))
print("Next year, you will be", age + 1)

# Example 3: Multiple Inputs
x, y = input("Enter two values: ").split()
print("You entered:", x, "and", y)

# Example 4: Type Casting
num = float(input("Enter a number: "))
print("You entered:", num)

# Example 5: Addition
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum is:", a + b)

# Example 6: Subtraction
print("Difference is:", a - b)

# Example 7: Multiplication
print("Product is:", a * b)

# Example 8: Division
print("Division is:", a / b)

# Example 9: Floor Division
print("Floor Division is:", a // b)

# Example 10: Modulus
print("Remainder is:", a % b)

# Example 11: Exponentiation
print("Power is:", a ** b)

# Example 12: Comparison
print("a > b:", a > b)

# Example 13: Logical
print("a > 0 and b > 0:", a > 0 and b > 0)

# Example 14: Identity
print("a is b:", a is b)

# Example 15: Membership
print("'x' in 'example':", 'x' in 'example')

# Example 16: if-else
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# Example 17: elif
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("A grade")
elif marks >= 80:
    print("B grade")
else:
    print("C grade")

# Example 18: for loop
for i in range(3):
    print("Hello", i)

# Example 19: while loop
i = 0
while i < 3:
    print("Loop", i)
    i += 1

# Example 20: break
for i in range(5):
    if i == 3:
        break
    print(i)

# Example 21: continue
for i in range(5):
    if i == 2:
        continue
    print(i)

# Example 22: pass
for i in range(3):
    pass
print("Pass executed")

# Example 23: String indexing
s = "Hello"
print(s[1])

# Example 24: String slicing
print(s[1:4])

# Example 25: String methods
print(s.upper())

# Example 26: List methods
lst = [1, 2, 3]
lst.append(4)
print(lst)

# Example 27: Dictionary
d = {"a": 1, "b": 2}
print(d["a"])

# Example 28: Function
def greet(name):
    print("Hi", name)

greet("Alice")


# ------------------------------
#       Exercise Solutions
# ------------------------------

# Exercise 1: Sum of first N natural numbers
N = int(input("Enter a number: "))
total = 0
for i in range(1, N + 1):
    total += i
print("Sum of first", N, "natural numbers is:", total)

# Exercise 2: Reverse a string using a for loop
text = input("Enter a string: ")
reversed_text = ''
for char in text:
    reversed_text = char + reversed_text
print("Reversed string:", reversed_text)

# Exercise 3: Function to sum two lists element-wise
def sum_lists(list1, list2):
    return [a + b for a, b in zip(list1, list2)]

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("Summed list:", sum_lists(list1, list2))

# Exercise 4: Function to split full name into first and last name
def get_first_last(full_name):
    parts = full_name.strip().split()
    return parts[0], parts[-1]

full_name = input("Enter your full name: ")
first, last = get_first_last(full_name)
print("First Name:", first)
print("Last Name:", last)
