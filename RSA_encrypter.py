from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

def encrypt_message(public_key, message):
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

def decrypt_message(private_key, encrypted_message):
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    try:
        decrypted_message = cipher.decrypt(encrypted_message)
        return decrypted_message.decode()
    except ValueError as e:
        print("Error decrypting message:", e)
        return None


def gen_keys(seed):
    os.environ['PYTHONHASHSEED'] = seed
    rsa_key = RSA.generate(2048)
    private_key = rsa_key.export_key().decode('utf-8')
    public_key = rsa_key.publickey().export_key().decode('utf-8')
    return private_key, public_key

def get_public_key(seed):
    os.environ['PYTHONHASHSEED'] = seed
    rsa_key = RSA.generate(2048)
    return rsa_key.publickey().export_key().decode('utf-8')

if __name__ == "__main__":
    print("Let's simulate the scenario where A gives their public key to B")
    print("and B gives their public key to A. In a real-world scenario,")
    print("you'd use something like sockets or a messaging service to exchange keys. \n\n\n")

    # Generating A's key pair with seed "A_seed"
    private_key_A, public_key_A = gen_keys("A_seed")
    print(f"private key of A is = {private_key_A}")
    print(f"public key of A is = {public_key_A}\n\n")

    # Generating B's key pair with seed "B_seed"
    private_key_B, public_key_B = gen_keys("B_seed")
    print(f"private key of B is = {private_key_B}")
    print(f"public key of B is = {public_key_B}\n\n")

    # Let's simulate B sending a message to A
    message_from_B = "Hey A, it's me B. How are you?"
    print(f"message from B is = {message_from_B}\n")
    encrypted_message_for_A = encrypt_message(public_key_A, message_from_B)
    print(f"the encrypted message for A is = {encrypted_message_for_A}\n\n")

    print("Now, A decrypts the message from B")
    decrypted_message_by_A = decrypt_message(private_key_A, encrypted_message_for_A)
    print("Message from B decrypted by A:", decrypted_message_by_A,"\n\n")

    print("Simulating A sending a message to B")
    message_from_A = "Hey B, I'm doing great! How about you?"
    encrypted_message_for_B = encrypt_message(public_key_B, message_from_A)
    print(f"message from A: {message_from_A}\n\n")

    print("Now, B decrypts the message from A")
    decrypted_message_by_B = decrypt_message(private_key_B, encrypted_message_for_B)
    print("Message from A decrypted by B:", decrypted_message_by_B)
