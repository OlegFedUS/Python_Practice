books = {"Dostoevsky": "Crime and Punishment", "Agatha Christi": "Murder on a Orient Express", "Kintaro Miura": "Berserk"}

valuesList = []
keysList = []

for i in books.values():
    valuesList.append(i)

for i in books.keys():
    keysList.append(i)

keysList.sort(reverse=True)
valuesList.sort()

print(f"Authors: {keysList}")
print(f"Books: {valuesList}")

print()

missed = books.pop("Dostoevsky")
print(missed)



