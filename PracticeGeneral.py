user_0 = {
    'username': 'ozymbeg',
    'firstname': 'Oleg',
    'lastname': 'Fedorov',
}


def printDictionary(data):
    for i, j in sorted(data.items()):
        print(f'{i}: {j}')


printDictionary(user_0)
