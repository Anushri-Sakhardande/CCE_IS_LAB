import random

class DiffieHellman:
    def __init__(self, p, g):
        self.p = p  # prime number
        self.g = g  # generator

    def generate_keys(self):
        """Generate public and private keys for Diffie-Hellman"""
        self.private_key = random.randint(2, self.p - 2)
        self.public_key = pow(self.g, self.private_key, self.p)
        return self.public_key

    def compute_shared_key(self, other_public_key):
        """Compute the shared secret key"""
        shared_key = pow(other_public_key, self.private_key, self.p)
        return shared_key