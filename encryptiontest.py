import rsa

msg=str(88)
pubk=rsa.PublicKey(187,7)
enc=rsa.encrypt(msg.encode(),pubk)
print("enc=",enc)
hexenc=enc.hex()
print("hexenc=",hexenc)

pvtk=rsa.PrivateKey(187,7,23,17,11)
dec=(rsa.decrypt(enc,pvtk)).decode()
print("ddec=",dec)

hexdec=bytes.fromhex(hexenc)
hexdecres=rsa.decrypt(hexdec,pvtk).decode()
print("hexdecres=",hexdecres)