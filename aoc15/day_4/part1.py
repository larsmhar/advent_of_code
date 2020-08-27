import hashlib

data = list(map(lambda x: x.strip(), open('data.txt', 'r')))[0]
print(data)


for i in range(9999999999):
    hash = hashlib.md5((data + str(i)).encode()).hexdigest()
    if hash[0:5] == '00000':
        print(i)
        break
