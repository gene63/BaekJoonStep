ham = []
drink = []
minham = 3000
mindrink = 2000
for i in range(0,3):
    ham.append(int(input()))
for i in range(0,2):
    drink.append(int(input()))
for i in range(0,3):
    if minham > ham[i]:
        minham = ham[i]
for i in range(0,2):
    if mindrink > drink[i]:
        mindrink = drink[i]

print(minham+mindrink-50)