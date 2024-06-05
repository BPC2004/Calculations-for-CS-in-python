def count_numbers_with_13(limit):
    count = 0
    for i in range(limit + 1):
        if '13' in str(i):
            count += 1
    return count

upper_limit = 10**5
result = count_numbers_with_13(upper_limit)
print(f"The number of integers containing '13' from 0 to {upper_limit} is: {result}")