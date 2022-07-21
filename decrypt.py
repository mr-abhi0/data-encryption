# import required module
from cryptography.fernet import Fernet

# take path of file as a input
keyfile = input(r'Enter key file : ')

# take path of file as a input
filepath = input(r'Enter path of encryption file : ')

# opening the key
with open(keyfile, 'rb') as filekey:
    key = filekey.read()

# using the key
fernet = Fernet(key)

# opening the encrypted file
with open(filepath, 'rb') as enc_file:
    encrypted = enc_file.read()

# decrypting the file
decrypted = fernet.decrypt(encrypted)

# opening the file in write mode and
# writing the decrypted data
with open(filepath, 'wb') as dec_file:
    dec_file.write(decrypted)


print('Decryption Done...')
