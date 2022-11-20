import hashlib as hash

x= "yzbqklnj"
print(x.encode())
y = hash.md5(x.encode())
print(y.hexdigest())

num = 0

while True:
    num += 1
    y = hash.md5((x+str(num)).encode())
    if y.hexdigest()[:6] == '000000':
        break
print(y.hexdigest())
print(num)
#get the string back from the hash
