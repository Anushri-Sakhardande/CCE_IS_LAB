import random
import math

class AsymmetricEncryption:
    def __init__(self, p, g):
        self.p = p  # prime number
        self.g = g  # generator

    def generate_keys(self):
        """Generate public and private keys for Elgamal and Schnorr"""
        self.private_key = random.randint(2, self.p - 2)
        self.public_key = pow(self.g, self.private_key, self.p)
        return self.public_key, self.private_key

    def elgamal_encrypt(self, message, public_key):
        """Elgamal encryption"""
        k = random.randint(2, self.p - 2)
        c1 = pow(self.g, k, self.p)
        c2 = (message * pow(public_key, k, self.p)) % self.p
        return c1, c2

    def elgamal_decrypt(self, c1, c2, private_key):
        """Elgamal decryption"""
        message = (c2 * pow(c1, self.p - 1 - private_key, self.p)) % self.p
        return message

    def schnorr_sign(self, message, private_key):
        """Schnorr signature"""
        k = random.randint(2, self.p - 2)
        r = pow(self.g, k, self.p)
        e = hash(str(message) + str(r)) % (self.p - 1)
        s = (k - private_key * e) % (self.p - 1)
        return r, s

    def schnorr_verify(self, message, r, s, public_key):
        """Schnorr signature verification"""
        e = hash(str(message) + str(r)) % (self.p - 1)
        v1 = pow(self.g, s, self.p)
        v2 = (r * pow(public_key, e, self.p)) % self.p
        return v1 == v2