# import required module
from cryptography.fernet import Fernet

# take path of file as a input
keyfile = input(r'Enter file name to save your key : ')

# key generation
key = Fernet.generate_key()

# string the key in a file
with open(keyfile, 'wb') as filekey:
    filekey.write(key)

    print('key file generated')
