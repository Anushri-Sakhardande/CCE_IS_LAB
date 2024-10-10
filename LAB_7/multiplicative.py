from Crypto.PublicKey import RSA

# Generates a public/private key pair
def generate_keypair(nlength=1024):
    key = RSA.generate(nlength)
    pub_key = key.publickey()
    return pub_key, key

# Encrypts a message using the public key
def encrypt(pub_key, message):
    e = pub_key.e
    n = pub_key.n
    ciphertext = pow(message, e, n)
    return ciphertext

# Decrypts a ciphertext using the private key
def decrypt(priv_key, ciphertext):
    d = priv_key.d
    n = priv_key.n
    message = pow(ciphertext, d, n)
    return message


# Generate key pair
pub_key, priv_key = generate_keypair()

# Encrypt integers
a = 7
b = 3
ciphertext_a = encrypt(pub_key, a)
ciphertext_b = encrypt(pub_key, b)

# Perform multiplicative homomorphic operation (multiply ciphertexts)
ciphertext_product = (ciphertext_a * ciphertext_b) % pub_key.n

# Decrypt the result
decrypted_product = decrypt(priv_key, ciphertext_product)

# Print results
print(f"Ciphertext of a: {ciphertext_a}")
print(f"Ciphertext of b: {ciphertext_b}")
print(f"Ciphertext of a * b: {ciphertext_product}")
print(f"Decrypted product: {decrypted_product}")
print(f"Expected product: {a * b}")
