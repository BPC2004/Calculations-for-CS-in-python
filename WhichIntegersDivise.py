print('What integer can be divided by: ', end = '')
I = int(input())
print('If you do not want to check for integers type the same integer: ', end = '')
I2 = int(input())
count = 0
for i in range(1000,10000):
    if i % I == 0 and i % I2 != 0:
        count += 1
print()
print(str(count))