from Crypto.Cipher import DES3
from Crypto import Random
import time
import os
from struct import pack


# get the PID
print "PID = " + str(os.getpid())
raw_input("continue...")
#-----------------------#

f_time = "%.20f" % time.time()
bs = DES3.block_size
key = 'Sixteen byte key'
iv = Random.new().read(DES3.block_size) #DES3.block_size==8
cipher= DES3.new(key, DES3.MODE_CBC, iv)
with open("plain_text_1MB.txt", "r") as f:
    plaintext = f.readlines()

plaintext = ''.join(plaintext)

plen = bs - divmod(len(plaintext),bs)[1]
padding = [plen]*plen
padding = pack('b'*plen, *padding)
#----------------------------

msg = iv + cipher.encrypt(plaintext + padding)

#----------------------------
l_time = "%.20f" % time.time()

done_time = float(l_time) - float(f_time)

f= open("encrypt_16MB.txt","w+")
f.write(msg)
f.close()

print "Encrypt time : " + str(done_time)
raw_input("continue...")
"""encrypted_text = cipher_encrypt.encrypt(plaintext)

cipher_decrypt = DES3.new(key, DES3.MODE_OFB, iv) #you can't reuse an object for encrypting or decrypting other data with the same key.
cipher_decrypt.decrypt(encrypted_text)
cipher_decrypt.decrypt(encrypted_text) #you cant do it twice

"""


