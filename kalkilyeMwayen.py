listNot = []
som = 0

konbyenNot = int(input('Konbyen not wap antre : '))

for i in range(0, konbyenNot):
    note = int(input(f'Antre not # {i + 1} : '))
    listNot.append(note)
print(listNot)

for i in listNot:
    som += i

print(som)
mwayen = som / konbyenNot
print(mwayen)
if mwayen >= 90:
    print('A')
elif mwayen >= 80 and mwayen < 90:
    print('B')
elif mwayen >= 70 and mwayen < 80:
    print('C')
elif mwayen >= 60 and mwayen < 70:
    print('D')
else:
    print('F')
