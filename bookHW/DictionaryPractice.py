carB = {'mark': 'BMW', 'model': 7}
carV = {'mark': 'Volvo', 'model': '14B'}
carV2 = {'mark': 'Volvo', 'model': 'X'}
carB2 = {'mark': 'BMW', 'model': 5}

for i in carB:
    a = i + ": " + f'{carB["mark"]}'
    for j in carB:
        b = j + ": " + f'{carB["model"]}'
        break

#print(a + "\n" + b)

carV2['box'] = 'A'
carV['box'] = 'M'

#print(carV)
#print(carV2)

carB['model'] = 8

#print(carB)


carA = {}
carA['mark'] = 'Audi'
carA['model'] = 'Q7'

#print(carA)


