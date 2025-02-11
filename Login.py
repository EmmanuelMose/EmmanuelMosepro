import tkinter as tk
from tkinter import messagebox

def login():
    username = username_entry.get()
    password = password_entry.get()
    user_type = user_type_var.get()

    if username == "" or password == "" or user_type == "":
        messagebox.showerror("Error", "All fields are required.")
        return

    if user_type == "admin":
        if username == "admin" and password == "password":
            admin_window()
        else:
            messagebox.showerror("Error", "Invalid admin credentials.")
    elif user_type == "student":
        if username == "student" and password == "password":
            student_window()
        else:
            messagebox.showerror("Error", "Invalid student credentials.")

def register():
    register_window = tk.Toplevel(root)
    register_window.title("Register")
    register_window.configure(bg="light blue")
    resize_and_center(register_window, 305, 205)

    frame = tk.Frame(register_window, bg="light blue", padx=15, pady=15)
    frame.pack(fill="both", expand=True)

    label_font = ("TkDefaultFont", 10)
    entry_font = ("TkDefaultFont", 10)

    tk.Label(frame, text="Username:", bg="light blue", fg="blue", font=label_font).grid(row=0, column=0, padx=5, pady=3, sticky="w")
    reg_username_entry = tk.Entry(frame, font=entry_font)
    reg_username_entry.grid(row=0, column=1, padx=5, pady=3, sticky="ew")

    tk.Label(frame, text="Password:", bg="light blue", fg="blue", font=label_font).grid(row=1, column=0, padx=5, pady=3, sticky="w")
    reg_password_entry = tk.Entry(frame, show="*", font=entry_font)
    reg_password_entry.grid(row=1, column=1, padx=5, pady=3, sticky="ew")

    tk.Label(frame, text="ConfirmPassword:", bg="light blue", fg="blue", font=label_font).grid(row=2, column=0, padx=5, pady=3, sticky="w")
    reg_confirm_password_entry = tk.Entry(frame, show="*", font=entry_font)
    reg_confirm_password_entry.grid(row=2, column=1, padx=5, pady=3, sticky="ew")

    def register_user():
        username = reg_username_entry.get()
        password = reg_password_entry.get()
        confirm_password = reg_confirm_password_entry.get()

        if not username or not password or not confirm_password:
            messagebox.showerror("Error", "All fields are required.")
            return

        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match.")
            return

        messagebox.showinfo("Success", "Registration successful!")
        register_window.destroy()

    tk.Button(frame, text="Register", command=register_user, bg="green", fg="white", font=label_font).grid(row=3, column=0, columnspan=2, pady=5)

    login_frame = tk.Frame(register_window, bg="light blue", padx=5, pady=5)
    login_frame.pack()

    tk.Label(login_frame, text="Already have an account?", bg="light blue", fg="blue", font=label_font).pack(side="left")
    back_to_login_button = tk.Label(login_frame, text="Sign in", bg="light blue", fg="green", cursor="hand2", font=(label_font[0], label_font[1], 'underline'))
    back_to_login_button.pack(side="left")
    back_to_login_button.bind("<Button-1>", lambda e: register_window.destroy())

def admin_window():
    admin = tk.Toplevel(root)
    admin.title("Admin Window")
    admin.configure(bg="light blue")
    resize_and_center(admin, 305, 255)
    label_font = ("TkDefaultFont", 10)
    tk.Label(admin, text="Welcome Admin", bg="light blue", fg="blue", font=label_font).pack(expand=True)

def student_window():
    student = tk.Toplevel(root)
    student.title("Student Window")
    student.configure(bg="light blue")
    resize_and_center(student, 305, 255)
    label_font = ("TkDefaultFont", 10)
    tk.Label(student, text="Welcome Student", bg="light blue", fg="blue", font=label_font).pack(expand=True)

def resize_and_center(window, width, height):
    window.geometry(f"{width}x{height}")
    window.resizable(False, False)
    window.update()
    x = (window.winfo_screenwidth() - width) // 2
    y = (window.winfo_screenheight() - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

root = tk.Tk()
root.title("Online Voting System")
root.configure(bg="light blue")
resize_and_center(root, 255, 205)

top_frame = tk.Frame(root, bg="blue", height=40)
top_frame.pack(fill="x")

title_label = tk.Label(top_frame, text="Login Page", bg="blue", fg="white", font=("TkDefaultFont", 14))
title_label.pack(pady=8, fill="x")

content_frame = tk.Frame(root, bg="light blue", padx=15, pady=8)
content_frame.pack(fill="both", expand=True)

label_font = ("TkDefaultFont", 10)
entry_font = ("TkDefaultFont", 10)

username_label = tk.Label(content_frame, text="Username:", bg="light blue", fg="blue", font=label_font)
username_label.grid(row=0, column=0, sticky="w", padx=3, pady=3)
username_entry = tk.Entry(content_frame, font=entry_font)
username_entry.grid(row=0, column=1, sticky="ew", padx=3, pady=3)

password_label = tk.Label(content_frame, text="Password:", bg="light blue", fg="blue", font=label_font)
password_label.grid(row=1, column=0, sticky="w", padx=3, pady=3)
password_entry = tk.Entry(content_frame, show="*", font=entry_font)
password_entry.grid(row=1, column=1, sticky="ew", padx=3, pady=3)

user_type_var = tk.StringVar(value="student")
admin_radio = tk.Radiobutton(content_frame, text="Admin", variable=user_type_var, value="admin", bg="light blue", font=label_font)
admin_radio.grid(row=2, column=0, sticky="w", padx=3, pady=3)
student_radio = tk.Radiobutton(content_frame, text="Student", variable=user_type_var, value="student", bg="light blue", font=label_font)
student_radio.grid(row=2, column=1, sticky="w", padx=3, pady=3)

login_button = tk.Button(content_frame, text="Login", command=login, bg="green", fg="white", font=label_font)
login_button.grid(row=3, column=0, columnspan=2, pady=3)

register_frame = tk.Frame(root, bg="light blue", padx=8, pady=3)
register_frame.pack()

no_account_label = tk.Label(register_frame, text="Don't have an account?", bg="light blue", fg="blue", font=label_font)
no_account_label.pack(side="left", padx=3)
register_button = tk.Label(register_frame, text="Sign up", bg="light blue", fg="green", cursor="hand2", font=(label_font[0], label_font[1], 'underline'))
register_button.pack(side="left")
register_button.bind("<Button-1>", lambda e: register())

root.mainloop()
