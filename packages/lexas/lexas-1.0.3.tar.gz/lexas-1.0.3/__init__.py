# Lexas 1.0.3 By CShark
# Remake from zwer answer in stackoverflow(https://stackoverflow.com/a/44212550/17681550)
# LastUpdate: 11.9.2022
# Update Details: Use PyCryptoDome inthread of PyCrypto, Make function esier to use
# pip install pycryptodome
import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
valid_type = str,bytes
def encrypt(key, source, encode=True):
    if type(key) in valid_type:
        if type(key) == str:
            key = key.encode("latin-1")
    else:
        raise ValueError("Invalid type(Key must be bytes or str)")
    if type(source) in valid_type:
        if type(source) == str:
            source = source.encode("latin-1")
    else:
        raise ValueError("Invalid type(Source must be bytes or str)")

    key = SHA256.new(key).digest()  # use SHA-256 over our key to get a proper-sized AES key
    IV = Random.new().read(AES.block_size)  # generate IV
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    padding = AES.block_size - len(source) % AES.block_size  # calculate needed padding
    source += bytes([padding]) * padding  # Python 2.x: source += chr(padding) * padding
    data = IV + encryptor.encrypt(source)  # store the IV at the beginning and encrypt
    return base64.b64encode(data).decode("latin-1") if encode else data

def decrypt(key, source):
    if type(source) in valid_type:
        if type(source) == str:
            source = base64.b64decode(source.encode("latin-1"))
    else:
        raise ValueError("Invalid type(Source must be bytes or str)")

    if type(key) in valid_type:
        if type(key) == str:
            key = key.encode("latin-1")
    else:
        raise ValueError("Invalid type(Key must be bytes or str)")
    key = SHA256.new(key).digest()  # use SHA-256 over our key to get a proper-sized AES key
    IV = source[:AES.block_size]  # extract the IV from the beginning
    decryptor = AES.new(key, AES.MODE_CBC, IV)
    data = decryptor.decrypt(source[AES.block_size:])  # decrypt
    padding = data[-1]  # pick the padding value from the end; Python 2.x: ord(data[-1])
    if data[-padding:] != bytes([padding]) * padding:  # Python 2.x: chr(padding) * padding
        raise ValueError("Invalid padding...")
    return data[:-padding]  # remove the padding
if __name__ == '__main__':
    Example = b"Hello World"
    Password = b"Hard Password"
    encrypted = encrypt(Password,Example)
    decrypted = decrypt(Password,encrypted)
    print(f"Origin Content: {Example}, Encrypted Content: {encrypted}, Decrypted Content: {decrypted}")
