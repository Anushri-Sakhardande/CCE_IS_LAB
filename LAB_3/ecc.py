#  Using ECC (Elliptic Curve Cryptography), encrypt the message "Secure Transactions" with the 
# public key. Then decrypt the ciphertext with the private key to verify the original message. 

from Crypto.PublicKey import ECC
import secrets

# Generate ECC private and public keys
private_key = ECC.generate(curve='P-256')
public_key = private_key.public_key()

# Display keys
print(f"Private key: {private_key.export_key(format='PEM')}")
print(f"Public key: {public_key.export_key(format='PEM')}")

# Elliptic Curve encryption (without hashing)
def ecc_encrypt(public_key, message):
    # Convert the message into an integer representation
    message_int = int.from_bytes(message.encode('utf-8'), 'big')
    
    # Generate a random number k
    k = secrets.randbelow(public_key.pointQ)
    
    # Ciphertext part 1: C1 = k * G (G is the base point on the curve)
    C1 = k * public_key._curve.g
    
    # Ciphertext part 2: C2 = M + k * Pub (Pub is the public key point)
    C2 = message_int + k * public_key.pointQ
    
    return C1, C2

# Elliptic Curve decryption (without hashing)
def ecc_decrypt(private_key, C1, C2):
    # Decrypt using the private key: M = C2 - priv * C1
    decrypted_message_point = C2 - private_key.d * C1
    
    # Convert the decrypted integer back into a string
    message_bytes = decrypted_message_point.to_bytes((decrypted_message_point.bit_length() + 7) // 8, 'big')
    
    return message_bytes.decode('utf-8')

# Example usage:
message = "Secure Transactions"
print(f"Original Message: {message}")

# Encrypt the message using the public key
C1, C2 = ecc_encrypt(public_key, message)
print(f"Ciphertext (C1, C2): {C1}, {C2}")

# Decrypt the ciphertext using the private key
decrypted_message = ecc_decrypt(private_key, C1, C2)
print(f"Decrypted Message: {decrypted_message}")
