from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes


def GetHashedPassword(password,salt):
    key = scrypt(password, salt, 16, N=2**14, r=8, p=1)
    return key

# User registers and creates a password
password = b'my super secret'
salt = get_random_bytes(16)
key = GetHashedPassword(password, salt)

# Salt and Key will be stored to DB
storedHashedPassword = key
storedSalt = salt

print(f'storedHashedPassword {storedHashedPassword}')
print(f'storedSalt {storedSalt}')

# User logs in again
# Password Authentication

enteredPassword =  b'my super secret'
hashedFromEnteredPassword = GetHashedPassword(enteredPassword,storedSalt)

print(f'hashedFromEnteredPassword {hashedFromEnteredPassword}')
print(f'{storedHashedPassword == hashedFromEnteredPassword}')

enteredWrongPassword =  b'wroong secret'
hashedFromEnteredWrongPassword = GetHashedPassword(enteredWrongPassword,storedSalt)

print(f'hashedFromEnteredWrongPassword {hashedFromEnteredWrongPassword}')
print(f'{storedHashedPassword == hashedFromEnteredWrongPassword}')
