def fibonacci_series(n):
       first, second = 0, 1
       print("Fibonacci series:", end=" ")
       for _ in range(n):
            print(first, end=" ")
       first, second = second, first + second
       print()

num = int(input("Enter the number of terms: "))
if num <= 0:
   print("Please enter a positive integer.")
else:
   fibonacci_series(num)