import random

def generate_key(n):
    return bytes([random.randrange(0, 256) for i in range(n)])

def xor(key, message):
    length = min(len(key), len(message))
    return bytes([key[i] ^ message[i] for i in range(length)])

message = input("Type your message.....")
message = message.encode()
#key = generate_key(len(message))
key = generate_key(int(input("Enter the key")) % 256)
cipher = xor(key, message)
print(key)
print(cipher)
print(xor(key, cipher))