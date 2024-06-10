person = {'firstName': 'Oleg', 'lastName': 'Fedorov', 'age': '29', 'city': 'Saint-Petersburg'}

'''
for key, value in person.items():
    print(f'{key}: {value}')
'''

def data(list):
    for i, j in list.items():
        print(f'{i}: {j}')


data(person)

print("\n")

def data2(name, age):
    add = {name: age}
    return add


x = data2('Oleg', 29)


data(x)



