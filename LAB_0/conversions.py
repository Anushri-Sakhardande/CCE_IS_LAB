def string_to_ascii(input_string):
    """Convert a string to a list of ASCII numbers."""
    return [ord(char) for char in input_string]

def hex_to_int(hex_string):
    """Convert a hex string to an integer."""
    return int(hex_string, 16)

def ascii_to_string(ascii_numbers):
    """Convert a list of ASCII numbers to a string."""
    return ''.join(chr(num) for num in ascii_numbers)

def int_to_hex(integer):
    """Convert an integer to a hexadecimal string."""
    return hex(integer)[2:]  # Remove the '0x' prefix

def int_to_string(integer):
    """Convert an integer to a string."""
    return str(integer)

def bin_to_int(bin_string):
    """Convert a binary string to an integer."""
    return int(bin_string, 2)

def int_to_bin(integer):
    """Convert an integer to a binary string."""
    return bin(integer)[2:]  # Remove the '0b' prefix

def string_to_bytes(input_string):
    """Convert a string to bytes."""
    return input_string.encode('utf-8')

def bytes_to_string(input_bytes):
    """Convert bytes to a string."""
    return input_bytes.decode('utf-8')

def int_to_bytes(input_int):
    """Convert an integer to bytes."""
    return input_int.to_bytes((input_int.bit_length() + 7) // 8, 'big') or b'\0'

def bytes_to_int(input_bytes):
    """Convert bytes to an integer."""
    return int.from_bytes(input_bytes, 'big')

def hex_to_bytes(hex_string):
    """Convert a hexadecimal string to bytes."""
    return bytes.fromhex(hex_string)

def bytes_to_hex(input_bytes):
    """Convert bytes to a hexadecimal string."""
    return input_bytes.hex()

# Example usage:
print(string_to_ascii("Hello"))  # Output: [72, 101, 108, 108, 111]
print(ascii_to_string([72, 101, 108, 108, 111]))  # Output: "Hello"

print(hex_to_int("FF"))  # Output: 255
print(int_to_hex(255))  # Output: "ff"

print(bin_to_int("101010"))  # Output: 42
print(int_to_bin(42))  # Output: "101010"

print(string_to_bytes("Hello"))  # Output: b'Hello'
print(bytes_to_string(b'Hello'))  # Output: "Hello"

print(int_to_bytes(42))  # Output: b'\x00*'
print(bytes_to_int(b'\x00*'))  # Output: 42

print(hex_to_bytes("FF"))  # Output: b'\xff'
print(bytes_to_hex(b'\xff'))  # Output: "ff"