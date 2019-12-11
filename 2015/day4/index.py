import hashlib

hash_key = 'ckczppom'

def five_zero_leading_hash(n):
    m = hashlib.md5()
    str_to_hash = hash_key + str(n)
    m.update(str_to_hash.encode('utf-8'))
    val = m.hexdigest()
    return val[0:5] != '00000'

def find_five_hash():
    num = 1
    while five_zero_leading_hash(num):
        num += 1
    return num

def six_zero_leading_hash(n):
    m = hashlib.md5()
    str_to_hash = hash_key + str(n)
    m.update(str_to_hash.encode('utf-8'))
    val = m.hexdigest()
    return val[0:6] != '000000'

def find_six_hash():
    num = 1
    while six_zero_leading_hash(num):
        num += 1
    return num



print(find_five_hash())
print(find_six_hash())