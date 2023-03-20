import rsa
import voterid
import Cryptodome 
import hashlib


publicKey, privateKey = rsa.newkeys(512)
print(str(publicKey),"\n",str(privateKey))
print(type(publicKey),"\n",type(privateKey))
print("e=",publicKey.e)
print("p=",privateKey.p)
print("type of private key is-",type(privateKey.q))
print("hexa decimal equivalent is",str(hex(privateKey.p)))

hexe=hex(privateKey.e)
inee=int(hexe)
print("hexe=",hexe,"inte=",inee)
message = "88"


encMessage = rsa.encrypt(message.encode(),
						publicKey)
hexenc=encMessage.hex()

print("original string: ", message)
print("encrypted string: ",str(hexenc))
print(type(hexenc))

bytesdec=bytes.fromhex(hexenc)
print("hex-bytes=",str(bytesdec))
pvtk=rsa.PrivateKey(187,7,23,17,11)
'''pvtk.n=187
pvtk.p=17
pvtk.q=11
pvtk.d=23
pvtk.e=7'''

decMessage = rsa.decrypt(bytesdec, privateKey).decode()


print("decrypted string: ", decMessage)
