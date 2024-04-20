import tkinter as tk
from tkinter import messagebox

def caesar_cipher_encrypt(plaintext, shift):
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                ciphertext += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                ciphertext += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            ciphertext += char  # Handle non-alphabetic characters
    return ciphertext

def caesar_cipher_decrypt(ciphertext, shift):
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                plaintext += chr((ord(char) - 97 - shift) % 26 + 97)
            else:
                plaintext += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            plaintext += char  
    return plaintext

def encrypt_message():
    plaintext = plaintext_entry.get()
    shift = int(shift_entry.get())
    encrypted_text = caesar_cipher_encrypt(plaintext, shift)
    encrypted_text_label.config(text="Encrypted message: " + encrypted_text)

def decrypt_message():
    ciphertext = ciphertext_entry.get()
    shift = int(shift_entry.get())
    decrypted_text = caesar_cipher_decrypt(ciphertext, shift)
    decrypted_text_label.config(text="Decrypted message: " + decrypted_text)

root = tk.Tk()
root.title("Caesar Cipher Encryption and Decryption")
root.geometry("400x200")

plaintext_label = tk.Label(root, text="Enter the message to encrypt:")
plaintext_label.pack()
plaintext_entry = tk.Entry(root, width=40)
plaintext_entry.pack()

shift_label = tk.Label(root, text="Enter the shift value (a positive integer):")
shift_label.pack()
shift_entry = tk.Entry(root, width=40)
shift_entry.pack()

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_message, bg="green", fg="white")
encrypt_button.pack()

encrypted_text_label = tk.Label(root, text="")
encrypted_text_label.pack()

ciphertext_label = tk.Label(root, text="Enter the message to decrypt:")
ciphertext_label.pack()
ciphertext_entry = tk.Entry(root, width=40)
ciphertext_entry.pack()

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_message, bg="blue", fg="white")
decrypt_button.pack()

decrypted_text_label = tk.Label(root, text="")
decrypted_text_label.pack()

root.mainloop()
