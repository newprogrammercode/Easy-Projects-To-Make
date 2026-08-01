import random
import string as s
def generate_password(length):
    if not isinstance(length , int):
        return "Invalid argument."
    chars = s.ascii_letters + s.digits + s.punctuation
    rs = ''
    for i in range(length):
        rs += random.choice(chars)
    return rs
print(generate_password(12))