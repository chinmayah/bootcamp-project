import hashlib
user = input("Enter string : ")
h = hashlib.md5(user.encode())
h2 = h.hexdigest()
print(h2)
