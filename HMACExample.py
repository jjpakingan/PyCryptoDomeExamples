'''
HMAC Example using Pycryptodome
https://pycryptodome.readthedocs.io/en/latest/src/hash/hmac.html

Environment:
Python 3.8.5 64-bit
LUbuntu 20.04 Linux
Visual Studio Code

Jeff P
'''

#  +-+-+-+-+-+-+-+
#  |I|m|p|o|r|t|s|
#  +-+-+-+-+-+-+-+
from Crypto.Hash import HMAC, SHA256

#  +-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+
#  |S|h|a|r|e|d| |H|M|A|C| |C|r|e|d|e|n|t|i|a|l|s|
#  +-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+-+-+-+-+

PRESHARED_SECRET = b'Swordfish'
DIGEST_MOD = SHA256

#  +-+-+-+-+-+-+-+ +-+-+-+
#  |S|e|n|d|e|r|:| |B|o|b|
#  +-+-+-+-+-+-+-+ +-+-+-+

h = HMAC.new(PRESHARED_SECRET, digestmod=DIGEST_MOD)
msgFromSender = b'Hello Alice'
h.update(msgFromSender)
macFromSender = h.hexdigest()

#### Now, Bob sends the message and MAC to Alice ...

#  +-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+
#  |R|e|c|e|i|v|e|r|:| |A|l|i|c|e|
#  +-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+

# Alice receives the msg and MAC from Bob

print(f"Alice: I received the message --> {msgFromSender}")
print(f"Alice: I received the MAC --> {macFromSender}")

h = HMAC.new(PRESHARED_SECRET, digestmod=DIGEST_MOD)
h.update(msgFromSender)
try:
   h.hexverify(macFromSender)
   print("The message '%s' is authentic" % msgFromSender)
except ValueError:
   print("The message or the key is wrong")
