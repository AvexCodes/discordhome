import base64, os

from cryptography.fernet import Fernet

def encryptToken(code):
    key = b'salt_', os.getenv('encryptionKey')
    code = code.encode()
    f = Fernet(key)
    return f.encrypt(code)