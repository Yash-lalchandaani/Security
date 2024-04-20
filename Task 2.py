from PIL import Image
import tkinter as tk
from tkinter import filedialog

def encrypt_image(image_path):
    img = Image.open(image_path)
    width, height = img.size
    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            img.putpixel((x, y), (b, r, g))
    encrypted_path = image_path.split('.')[0] + '_encrypted.png'
    img.save(encrypted_path)
    status_label.config(text=f"Image encrypted successfully. Encrypted image saved as {encrypted_path}")

def decrypt_image(image_path):
    img = Image.open(image_path)
    width, height = img.size
    for x in range(width):
        for y in range(height):
            b, r, g = img.getpixel((x, y))
            img.putpixel((x, y), (r, g, b))
    decrypted_path = image_path.split('_encrypted')[0] + '_decrypted.png'
    img.save(decrypted_path)
    status_label.config(text=f"Image decrypted successfully. Decrypted image saved as {decrypted_path}")

def select_file():
    filepath = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, filepath)

def encrypt():
    image_path = entry.get()
    encrypt_image(image_path)

def decrypt():
    encrypted_image_path = entry.get()
    decrypt_image(encrypted_image_path)

root = tk.Tk()
root.title('Image Encryption Tool')

label = tk.Label(root, text='Select Image File:')
label.pack()

entry = tk.Entry(root, width=50)
entry.pack()

browse_button = tk.Button(root, text='Browse', command=select_file)
browse_button.pack()

encrypt_button = tk.Button(root, text='Encrypt', command=encrypt, bg='green', fg='white')
encrypt_button.pack()

decrypt_button = tk.Button(root, text='Decrypt', command=decrypt, bg='blue', fg='white')
decrypt_button.pack()

status_label = tk.Label(root, text='')
status_label.pack()

root.mainloop()
