print('Insert G value')
G = int(input())
print('Insert P value')
P = int(input())
for q in range(1000):
    if G ** q % P == 1:
        print('Value for q is: ' + str(q))