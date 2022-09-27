# No need to install
import hashlib

# Text input
strHash = str(input("Please enter your text: \n"))

# SHA-2 is a set of cryptographic functions, including SHA-224, SHA-256, SHA-384, SHA-512

# 224 bits
resultsha224 = hashlib.sha224(strHash.encode())

# 256 bits
resultsha256 = hashlib.sha256(strHash.encode())

# 384 bits
resultsha384 = hashlib.sha384(strHash.encode())

# 512 bits
resultsha512 = hashlib.sha512(strHash.encode())

# Hash method that generates a 128-bit hash from a string of data of any length
resultmd5 = hashlib.md5(strHash.encode())

# Some printing
print(f'\nSHA-224 \n {resultsha224.hexdigest()}')
print(f'\nSHA-256 \n {resultsha256.hexdigest()}')
print(f'\nSHA-384 \n {resultsha384.hexdigest()}')
print(f'\nSHA-512 \n {resultsha512.hexdigest()}')
print(f'\nMD5 \n {resultmd5.hexdigest()}')