from cryptography.fernet import Fernet
import os

def write_safe_key():
    """
    Generates and writes a new encryption key to 'key.key' file.
    """
    key = Fernet.generate_key()
    with open('key.key', 'wb') as keyFile:
        return keyFile.write(key)
    
def read_safe_key():
    """
    Reads and returns the encryption key stored in 'key.key' file.
    """
    with open('key.key', 'rb') as readKey:
        data = readKey.read()
        return data

def encrypt_pw(password):
    """
    Encrypts the given password using the encryption key stored in 'key.key'.
    
    Args:
    - password (str): The password to encrypt.
    
    Returns:
    - str: The encrypted password as a UTF-8 decoded string.
    """
    key = read_safe_key()
    cipher = Fernet(key)
    return cipher.encrypt(password.encode()).decode("utf-8")

def decrypt_pw(password):
    """
    Decrypts the given encrypted password using the encryption key stored in 'key.key'.
    
    Args:
    - password (str): The encrypted password to decrypt.
    
    Returns:
    - str: The decrypted password as a UTF-8 decoded string.
    """
    key = read_safe_key()
    cipher = Fernet(key)
    return cipher.decrypt(password.encode()).decode('utf-8')

def check_key_exist():
    """
    Checks if the 'key.key' file exists. If not, generates a new encryption key and saves it.
    """
    if os.path.exists('key.key'):
        None
    else:
        write_safe_key()

check_key_exist()
