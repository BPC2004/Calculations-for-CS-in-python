turbo = 1
regular = 1
year = 0
tur = False
while turbo <= regular:
    if tur == True:
        turbo = turbo * 1.05
    regular = regular * 1.045
    tur = True
    year += 1
print(str(year))