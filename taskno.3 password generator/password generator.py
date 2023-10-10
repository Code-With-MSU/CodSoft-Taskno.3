import tkinter as tk
import random
import string
from tkinter import messagebox 
from PIL import Image, ImageTk

def generate_password():
    password_length = length_entry.get()
    
    if not password_length.isdigit() or int(password_length) < 6:
        messagebox.showerror("Error", "Password length should be a numeric value and at least 6 characters")
        return
    
    password_length = int(password_length)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def toggle_password_visibility():
    current_password_state = password_entry.cget("show")
    if current_password_state:
        password_entry.config(show="")
        show_password_button.config(text="Hide")
    else:
        password_entry.config(show="*")
        show_password_button.config(text="Reveal")

root = tk.Tk()
root.title("Password Generator App")
root.geometry("400x315")

bg_image = Image.open("background.png")
bg_photo = ImageTk.PhotoImage(bg_image)
background_label = tk.Label(root, image=bg_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)  

label = tk.Label(root, text="Password Generator", font="Helvetica 30 bold", bg="black", fg="goldenrod")
label.pack(pady=10)

length_label = tk.Label(root, text="Length", font="Helvetica 15 bold", bg="black", fg="goldenrod")
length_label.pack(pady=5)  

length_entry = tk.Entry(root, width=4)
length_entry.pack(pady=5)  
length_entry.insert(0, "8") 

generate_button = tk.Button(root, text="Generate", font="Helvetica 10", bg="black", fg="goldenrod", command=generate_password)
generate_button.pack(pady=5)

password_label = tk.Label(root, text="Password", font="Helvetica 15 bold", bg="black", fg="goldenrod")
password_label.pack(pady=5)

password_entry = tk.Entry(root, show='*')  
password_entry.pack(pady=5)

show_password_button = tk.Button(root, text="Reveal", width=7, bg="black", fg="goldenrod", command=toggle_password_visibility)
show_password_button.pack(pady=5)

developer_label = tk.Label(root, text="Developed by: Muhammad Samiullah", font="Helvetica 10", bg="black", fg="goldenrod")
developer_label.pack(side=tk.BOTTOM, pady=5)

root.mainloop()
