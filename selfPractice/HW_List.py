
#Домашка по теме Список и манипулирование им.

guestList = ["Van", "Billy", "Steve"]
inviteMessage = ", wollen Sie kommen zu meinem GeburtTag?"

for i in guestList:
    print(f"{i}{inviteMessage}")

print("\n")

missing = guestList.pop(1)
print(f"{missing.title()}, kann nicht zum GeburtTeg kommen")

print()

for i in guestList:
    print(f"{i}{inviteMessage}")

    print()

guestList.insert(0, "Obama")
guestList.insert(2, "Bogdan")
guestList.append("Titpig")

for i in guestList:
    print(f"{i}{inviteMessage}")

print()
print("Der Tish ist nicht hier da!")
print()


while len(guestList) != 2:
    missing = guestList.pop()
    print(f"{missing} not gonna be on the party.")


print()

print(f"{guestList} are final guests!")

print()

del guestList[0]
del guestList[0]

print(len(guestList))


