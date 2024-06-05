import random

random_numbers = [random.randint(0, 1500) for _ in range(20)]

counter = 0

for i in random_numbers:
    if i >= 100 and i < 1000:
        counter += 1

print(random_numbers)
print(str(counter))