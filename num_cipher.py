import string

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYS1234567890!? '
chars += string.punctuation
num = 1
cipher = {}
for i in chars:
    cipher[i] = str(num)
    num += 1

def encrypt(text):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYS1234567890!? '
    chars += string.punctuation
    num = 1
    cipher = {}
    for i in chars:
        cipher[i] = str(num)
        num += 1

    num = 1
    decipher = {}
    for i in chars:
        decipher[str(num)] = str(i)
        num += 1

    return '_'.join([cipher[str(i)] for i in text])

def decrypt(text):

    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYS1234567890!? '
    num = 1
    cipher = {}
    for i in chars:
        cipher[i] = str(num)
        num += 1

    decipher = {num : key for key, num in cipher.items()}

    return ''.join([decipher[str(i)] for i in str(text).split('_')])


