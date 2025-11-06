# roach_fernet.py
from cryptography.fernet import Fernet
import base64

def inside_out(data: bytes) -> bytes:
    """Flip halves of the byte string."""
    mid = len(data) // 2
    return data[mid:] + data[:mid]

def roach_encrypt(plaintext: str, key: bytes) -> str:
    """
    Encrypt plaintext using Fernet with an optional inside-out flip.
    Output is base64 for readability.
    """
    f = Fernet(key)
    data = plaintext.encode("utf-8")
    data = inside_out(data)      # optional Roach-style flip
    encrypted = f.encrypt(data)
    return base64.b64encode(encrypted).decode("utf-8")

def roach_decrypt(ciphertext_b64: str, key: bytes) -> str:
    """
    Decrypt ciphertext using Fernet and reverse the inside-out flip.
    """
    f = Fernet(key)
    encrypted = base64.b64decode(ciphertext_b64)
    data = f.decrypt(encrypted)
    data = inside_out(data)      # reverse flip
    return data.decode("utf-8")

if __name__ == "__main__":
    # Generate a secure Fernet key (do this once and save it)
    key = Fernet.generate_key()

    plaintext = "the roach survives"
    encrypted = roach_encrypt(plaintext, key)
    decrypted = roach_decrypt(encrypted, key)

    print("Key       :", key.decode())
    print("Original  :", plaintext)
    print("Encrypted :", encrypted)
    print("Decrypted :", decrypted)
