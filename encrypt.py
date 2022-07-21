# import required module
from cryptography.fernet import Fernet

# take path of file as a input
keyfile = input(r'Enter key file : ')

# take path of file as a input
filepath = input(r'Enter path of encryption file : ')

# opening the key
with open(keyfile, 'rb') as filekey:
    key = filekey.read()

# using the generated key
fernet = Fernet(key)

# opening the original file to encrypt
with open(filepath, 'rb') as file:
    original = file.read()

# encrypting the file
encrypted = fernet.encrypt(original)


# opening the file in write mode and
# writing the encrypted data
with open(filepath, 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

    print('Encryption Done...')
