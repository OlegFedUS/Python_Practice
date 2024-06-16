forNames = ["Bllly", "Van", "Kazua"]
forNames.append("Obama")
forNames.insert(0, "Biollante")

j = 0

for i in forNames:
    j = len(i)
    print(i)

print(j)

#print(forNames[0])

################

myData = ["oleg fedorov", 29, "5404 Bentgrass Dr."]
myData.append(555-21-341)
myData.insert(1, 'M')

for cycles in myData:
    cycles = f"{cycles}"
    #print(f"{cycles.lower()}" + " - lower")
    #print(f"{cycles.upper()}" + " ;UPPER;\n")


###############

randomNum = [12, 41, 2, 62, 1]

for i in range(len(randomNum) - 1):
    for j in range(len(randomNum) - i - 1):
        if randomNum[j] > randomNum[j + 1]:
            randomNum[j], randomNum[j + 1] = randomNum[j + 1], randomNum[j]

#print(randomNum)

x = 12
y = 6







