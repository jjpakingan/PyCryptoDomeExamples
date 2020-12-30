#Generated the private and public key using OpenSSL https://www.scottbrady91.com/OpenSSL/Creating-RSA-Keys-using-OpenSSL

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# Bob sends the public key to Alice.
# Now Alice starts to encrypt her message to Bob
message = b'I am Alice!'
key = RSA.importKey(open('public.pem').read())
cipher = PKCS1_OAEP.new(key)
ciphertext = cipher.encrypt(message)

# Bob will now decode the message he received from Alice
key = RSA.importKey(open('private.pem').read())
cipher = PKCS1_OAEP.new(key)
message = cipher.decrypt(ciphertext)
print(message)
