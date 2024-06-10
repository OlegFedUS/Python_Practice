person1 = {'name': 'Van', 'age': '30', 'salary': 0}
person2 = {'name': 'Billy', 'age': '51', 'salary': 0}
person3 = {'name': 'Ivan', 'age': '19', 'salary': 0}

print("Please add your age information: ")
ageData = {'age': int(input())}

print("Please add your name information: ")
mainPerson = {'name': input(), 'salary': 0}

if ageData['age'] <= 25:
    mainPerson['salary'] = 950
elif ageData['age'] <= 29:
    mainPerson['salary'] = 3000
elif ageData['age'] <= 49:
    mainPerson['salary'] = 6000
else:
    mainPerson['salary'] = 0

print(mainPerson)


