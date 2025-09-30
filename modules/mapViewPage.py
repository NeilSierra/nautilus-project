import tkinter as tk
import customtkinter as ctk
import tkintermapview as tkm
import os as os

from tkinter import ttk
from PIL import Image

class MapViewPage(ctk.CTkFrame):  # Page 1
    def __init__(self, master, control):
        super().__init__(master)
        self.configure(fg_color="#790B0C")

        self.places = ["C201", "C202",]

        # Frame to hold all contents
        self.center_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="#790B0C")
        self.center_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Configure row and columns
        self.center_frame.grid_rowconfigure(0, weight=1)
        self.center_frame.grid_columnconfigure(0, weight=1)  # Left side widget
        self.center_frame.grid_columnconfigure(1, weight=4)  # Right side widget

        """ Left Side Widget """
        # Frame to hold all widgets for left side
        self.wrap_frame = ctk.CTkFrame(self.center_frame, fg_color="#790B0C")
        self.wrap_frame.grid(row=0, column=0, sticky="nsew")

        # Nautilus logo
        self.nautilus_logo = Image.open("/".join([os.getcwd().replace("\\", "/"), "sources/logo_text_horizontal.png"]))
        self.logo = ctk.CTkLabel(
            self.wrap_frame, text="",
            image=ctk.CTkImage(light_image=self.nautilus_logo, dark_image=self.nautilus_logo, size=(198, 50))
        )
        self.logo.pack(pady=(10, 0))

        # Label frames
        self.page_section = tk.LabelFrame(
            self.wrap_frame, text=" Pages ",
            font=("Arial", 15), fg="#F8F7F2",
            bg="#790B0C", bd=3
        )
        self.page_section.pack(fill="x", pady=20)
        self.navigation_section = tk.LabelFrame(
            self.wrap_frame, text=" Navigation ", height=100,
            font=("Arial", 15), fg="#F8F7F2",
            bg="#790B0C", bd=3
        )
        self.navigation_section.pack(fill="x")
        self.navigation_section.grid_rowconfigure(0, weight=1)
        self.navigation_section.grid_rowconfigure(1, weight=1)
        self.navigation_section.grid_columnconfigure(0, weight=1)
        self.navigation_section.grid_columnconfigure(1, weight=4)

        # Page section buttons declaring
        self.home_btn = ctk.CTkButton(
            self.page_section, height=40, corner_radius=0, anchor="w",
            text="  Back to Home", font=("Arial", 15),
            command=lambda: control.change_page(0)
        )
        self.map_view_btn = ctk.CTkButton(
            self.page_section, height=40, corner_radius=0, anchor="w",
            text="  Map View", font=("Arial", 15),
            command=lambda: control.change_page(1)
        )
        self.about_btn = ctk.CTkButton(
            self.page_section, height=40, corner_radius=0, anchor="w",
            text="  About Us", font=("Arial", 15),
            command=lambda: control.change_page(2)
        )
        self.terms_btn = ctk.CTkButton(
            self.page_section, height=40, corner_radius=0, anchor="w",
            text="  Terms and Conditions", font=("Arial", 15),
            command=lambda: control.change_page(3)
        )

        # Page section buttons packing
        self.home_btn.pack(fill="x", pady=(10, 5))
        self.map_view_btn.pack(fill="x", pady=5)
        self.about_btn.pack(fill="x", pady=5)
        self.terms_btn.pack(fill="x", pady=(5, 10))

        # Navigation section declaration
        self.from_label = ctk.CTkLabel(self.navigation_section, text="     From:", font=("Arial", 15), text_color="#F8F7F2")
        self.to_label = ctk.CTkLabel(self.navigation_section, text="     To:", font=("Arial", 15), text_color="#F8F7F2")
        self.from_box = ctk.CTkComboBox(self.navigation_section, values=self.places)
        self.from_box.set("Select an Origin")
        self.to_box = ctk.CTkComboBox(self.navigation_section, values=self.places)
        self.to_box.set("Select a Destination")
        self.navigate_btn = ctk.CTkButton(
            self.navigation_section, height=40, corner_radius=10,
            text="NAVIGATE", font=("Arial", 15, "bold"),
            fg_color="#F8F7F2", text_color="#790B0C"
        )
        
        # Navigation section packing
        self.from_label.grid(row=0, column=0, sticky="w", pady=(20, 10))
        self.to_label.grid(row=1, column=0, sticky="w", pady=10)
        self.from_box.grid(row=0, column=1, sticky="we", pady=(20, 10), padx=(0, 15))
        self.to_box.grid(row=1, column=1, sticky="we", pady=10, padx=(0, 15))
        self.navigate_btn.grid(row=2, column=0, columnspan=2, sticky="we", pady=(10, 20), padx=15)

        """ Right Side Widget """
        self.map_widget = tkm.TkinterMapView(self.center_frame, corner_radius=10)
        self.map_widget.set_position(14.2908563, 120.9152714)  # LPU Coordinates
        self.map_widget.set_zoom(20)
        self.map_widget.grid(row=0, column=1, sticky="nsew", padx=(20, 0))


# For debugging and testing
if __name__ == "__main__":
    app = ctk.CTk()
    app.minsize(800, 600)
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)

    theme_path = "/".join([os.getcwd().replace("\\", "/"), "theme.json"])
    ctk.set_default_color_theme(theme_path)

    page = MapViewPage(app, app)
    page.grid(row=0, column=0, sticky="nsew")

    app.mainloop()