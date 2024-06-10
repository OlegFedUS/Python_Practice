text = input().title()
text2 = input().title()
text3 = input().title()

typeIn = input().title()


if text == "Billy":
    print("Boss Of The Gym")
else:
    print("loser")

nameList = [text, text2, text3]

if typeIn not in nameList:
    print("Name not found!")
else:
    print("Accepted.")





