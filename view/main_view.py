import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image


class MainView(ctk.CTk):
    def __init__(self, presenter):
        super().__init__()
        self.presenter = presenter
        self.title('gen a card')
        self.geometry('970x670')

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1, minsize=512)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1, minsize=512)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)

        self.image_frame = ctk.CTkFrame(self)
        self.image_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.control_frame = ctk.CTkFrame(self)
        self.control_frame.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

        # Configure grid weights for control_frame to center contents
        self.control_frame.grid_columnconfigure(0, weight=1)
        self.control_frame.grid_columnconfigure(1, weight=1)
        self.control_frame.grid_columnconfigure(2, weight=1)
        self.control_frame.grid_rowconfigure(0, weight=1)
        self.control_frame.grid_rowconfigure(1, weight=1)
        self.control_frame.grid_rowconfigure(2, weight=1)
        self.control_frame.grid_rowconfigure(3, weight=1)
        self.control_frame.grid_rowconfigure(4, weight=1)
        self.control_frame.grid_rowconfigure(5, weight=1)
        self.control_frame.grid_rowconfigure(6, weight=1)
        self.control_frame.grid_rowconfigure(7, weight=1)
        self.control_frame.grid_rowconfigure(8, weight=1)
        self.control_frame.grid_rowconfigure(9, weight=1)
        self.control_frame.grid_rowconfigure(10, weight=1)
        # self.control_frame.grid_rowconfigure(11, weight=1)
        # self.control_frame.grid_rowconfigure(12, weight=1)

        base_path = self.presenter.get_base_path()
        self.my_image = ctk.CTkImage(light_image=Image.open(base_path + "/../static/blank.png"), size=(512, 512))
        self.my_label = ctk.CTkLabel(self.image_frame, text='', image=self.my_image)
        self.my_label.place(relx=0.5, rely=0.5, anchor='center')

        self.loading_label = ctk.CTkLabel(self.image_frame, text='Generating...', font=('Arial', 24))

        self.gen_label = ctk.CTkLabel(self.control_frame, text="Generate an Image", font=('Arial', 24))
        self.gen_label.grid(row=2, column=0, columnspan=2, pady=5, padx=5, sticky="n")

        self.category_var = tk.StringVar(value="Flowers")
        self.category_menu = ctk.CTkOptionMenu(self.control_frame, variable=self.category_var, values=list(presenter.get_categories()))
        self.category_menu.grid(row=3, column=0, columnspan=2, pady=0, padx=5, sticky="n")

        self.custom_seed_var = tk.BooleanVar()
        self.custom_seed_check = ctk.CTkCheckBox(self.control_frame, text="Custom Seed", variable=self.custom_seed_var, command=self.toggle_seed_entry)
        self.custom_seed_check.grid(row=4, column=0, pady=0, padx=5, sticky="ne")

        self.seed_entry = ctk.CTkEntry(self.control_frame, placeholder_text="Enter seed", state='disabled')
        self.seed_entry.grid(row=4, column=1, pady=0, padx=5, sticky="nw")

        self.generate_button = ctk.CTkButton(self.control_frame, text='Generate', fg_color='#FF0', text_color='#000', hover_color='#AA0', command=self.generate_image)
        self.generate_button.grid(row=5, column=0, pady=5, padx=(15, 5), sticky="new")

        self.open_var = tk.StringVar(value="Select Image")
        self.open_menu = ctk.CTkOptionMenu(self.control_frame, variable=self.open_var, values=[], command=self.open_image)
        self.open_menu.grid(row=5, column=1, columnspan=2, pady=5, padx=(5, 15), sticky="new")
        self.update_open_menu()

        self.add_label = ctk.CTkLabel(self.control_frame, text="Add Text", font=('Arial', 24))
        self.add_label.grid(row=6, column=0, columnspan=2, pady=5, padx=5, sticky="n")


        self.text_entry = ctk.CTkEntry(self.control_frame, placeholder_text="Enter text here...")
        self.text_entry.grid(row=7, column=0, pady=5, padx=(15, 5), sticky="new")

        self.font_var = tk.StringVar(value="Arial")
        self.font_menu = ctk.CTkOptionMenu(self.control_frame, variable=self.font_var, values=list(presenter.get_fonts().keys()))
        self.font_menu.grid(row=7, column=1, columnspan=2, pady=5, padx=(5, 15), sticky="new")

        self.add_text_button = ctk.CTkButton(self.control_frame, text='Add Text', fg_color='#FF0', text_color='#000', hover_color='#AA0', command=self.add_text_to_image)
        self.add_text_button.grid(row=8, column=0, columnspan=2, pady=5, padx=5, sticky="n")

        self.save_button = ctk.CTkButton(self.control_frame, text='Save Image', fg_color='#FF0', text_color='#000', hover_color='#AA0', command=self.save_image)
        self.save_button.grid(row=9, column=0, columnspan=2, pady=5, padx=5, sticky="n")

    def toggle_seed_entry(self):
        if self.custom_seed_var.get():
            self.seed_entry.configure(state='normal')
        else:
            self.seed_entry.configure(state='disabled')

    def generate_image(self):
        selected_category = self.category_var.get()
        custom_seed = self.custom_seed_var.get()
        seed = self.seed_entry.get() if custom_seed else None
        self.presenter.generate_image(selected_category, seed)

    def add_text_to_image(self):
        text = self.text_entry.get()
        selected_font = self.font_var.get()
        self.presenter.add_text_to_image(text, selected_font)

    def save_image(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            self.presenter.save_image(file_path)

    def show_image(self, image_path):
        generated_image = Image.open(image_path)
        self.my_image = ctk.CTkImage(light_image=generated_image, size=(512, 512))
        self.my_label.configure(image=self.my_image)

    def show_loading(self):
        self.loading_label.place(relx=0.5, rely=0.5, anchor='center')
        self.update()

    def hide_loading(self):
        self.loading_label.place_forget()

    def show_error(self, message):
        messagebox.showerror("Error", message)

    def update_open_menu(self):
        files = self.presenter.get_generated_files()
        self.open_menu.configure(values=files)

    def open_image(self, filename):
        self.presenter.open_image(filename)
