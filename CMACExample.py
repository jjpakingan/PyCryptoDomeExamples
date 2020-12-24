'''
CMAC Example using Pycryptodom

Environment:
Python 3.8.5 64-bit
LUbuntu 20.04 Linux
Visual Studio Code

Jeff P
'''

#  +-+-+-+-+-+-+-+
#  |I|m|p|o|r|t|s|
#  +-+-+-+-+-+-+-+
from Crypto.Hash import CMAC
from Crypto.Cipher import AES


#  +-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+
#  |S|h|a|r|e|d| |C|M|A|C| |C|r|e|d|e|n|t|i|a|l|s|
#  +-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+

PRESHARED_SECRET = b'Sixteen byte key'
CIPHER_MOD = AES

#  +-+-+-+-+-+-+-+ +-+-+-+
#  |S|e|n|d|e|r|:| |B|o|b|
#  +-+-+-+-+-+-+-+ +-+-+-+

cobj = CMAC.new(PRESHARED_SECRET, ciphermod=CIPHER_MOD)
msgFromSender = b'Hello'
cobj.update(msgFromSender)
macFromSender = cobj.hexdigest()

#### Now, Bob sends the message and MAC to Alice ...

#  +-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+
#  |R|e|c|e|i|v|e|r|:| |A|l|i|c|e|
#  +-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+

# Alice receives the msg and MAC from Bob

print(f"Alice: I received the message --> {msgFromSender}")
print(f"Alice: I received the MAC --> {macFromSender}")

cobj = CMAC.new(PRESHARED_SECRET, ciphermod=CIPHER_MOD)
cobj.update(msgFromSender)
try:
   cobj.hexverify(macFromSender)
   print("The message '%s' is authentic" % msgFromSender)
except ValueError:
   print("The message or the key is wrong")
