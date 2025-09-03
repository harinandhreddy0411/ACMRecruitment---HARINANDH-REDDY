n = 100
sum_n = n * (n + 1) // 2
square_of_sum = sum_n ** 2
sum_of_squares = n * (n + 1) * (2 * n + 1) // 6
difference = square_of_sum - sum_of_squares
print("Difference:", difference)

total = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print("Sum:", total)

