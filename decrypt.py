# import required module
from cryptography.fernet import Fernet

# opening the key
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()

# using the key
fernet = Fernet(key)

# opening the encrypted file
with open('rzp.csv', 'rb') as enc_file:
    encrypted = enc_file.read()

# decrypting the file
decrypted = fernet.decrypt(encrypted)

# opening the file in write mode and
# writing the decrypted data
with open('rzp.csv', 'wb') as dec_file:
    dec_file.write(decrypted)
