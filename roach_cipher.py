# roach_cipher.py
# Reversible "inside-out" cipher (toy symmetric encryption)

import base64

def invert_bits(data: bytes) -> bytes:
    """Bitwise invert (flip 0<->1)."""
    return bytes(b ^ 0xFF for b in data)

def inside_out(text: str) -> str:
    """Flip structure: reverse halves."""
    mid = len(text) // 2
    return text[mid:] + text[:mid]

def xor_with_key(data: bytes, key: bytes) -> bytes:
    """XOR data with repeating key bytes."""
    key_len = len(key)
    return bytes([b ^ key[i % key_len] for i, b in enumerate(data)])

def roach_cipher(payload: str, key: str) -> str:
    """
    Apply the reversible Roach cipher.
    Run this function twice with the same key to get the original text back.
    """
    # Inside-out structural flip
    flipped = inside_out(payload)

    # XOR + bitwise invert
    data = flipped.encode("utf-8")
    data = xor_with_key(data, key.encode("utf-8"))
    data = invert_bits(data)

    # Encode for readability
    return base64.b64encode(data).decode("utf-8")

def roach_decipher(payload_b64: str, key: str) -> str:
    """
    Decrypt (identical to encryption reversed).
    """
    data = base64.b64decode(payload_b64)
    data = invert_bits(data)
    data = xor_with_key(data, key.encode("utf-8"))
    flipped = data.decode("utf-8")
    return inside_out(flipped)  # re-flip halves

if __name__ == "__main__":
    text = "the roach survives"
    key = "roachkey"

    encrypted = roach_cipher(text, key)
    decrypted = roach_decipher(encrypted, key)

    print("Original :", text)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)
