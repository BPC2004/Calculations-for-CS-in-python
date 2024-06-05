print('G^a mod P = A')
print('Insert G value')
G = int(input())
print('Insert P value')
P = int(input())
print('Insert A value')
A = int(input())
print('a is smaller then:')
rangee = int(input())
for a in range(rangee):
    if G ** a % P == A:
        print('Value for a is: ' + str(a))