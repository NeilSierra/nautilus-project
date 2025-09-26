import customtkinter as ctk
import os as os

from PIL import Image

class LandingPage(ctk.CTkFrame): # Page 0
    def __init__(self, master, control):
        super().__init__(master)

        # Frame to center the items
        self.center_frame = ctk.CTkFrame(self)
        self.center_frame.pack(expand=True)

        """ Widget Declaration """
        # Nautilus logo
        self.nautilus_logo = Image.open("/".join([os.getcwd().replace("\\", "/"), "sources/logo.png"]))
        self.logo = ctk.CTkLabel(
            self.center_frame, text="",
            image=ctk.CTkImage(light_image=self.nautilus_logo, dark_image=self.nautilus_logo, size=(250, 250))
        )
        # Nautilus labels
        self.title = ctk.CTkLabel(self.center_frame, text="N A U T I L U S", font=("Helvetica", 50, "bold"), text_color="#790B0C")
        self.subtitle = ctk.CTkLabel(self.center_frame, text="Campus Navigator", font=("Arial", 30, "bold"))
        # Navigate button
        self.navigate_btn = ctk.CTkButton(
            self.center_frame, height=40, width=300,
            text="START NAVIGATING", font=("Arial", 20, "bold"),
            command=lambda: control.change_page(1)
        )
        self.about_btn = ctk.CTkButton(
            self.center_frame, height=40, width=300,
            text="ABOUT US", font=("Arial", 20, "bold"),
            fg_color="#1F1F1F",
            command=lambda: control.change_page(2)
        )

        """ Widget Placement """
        self.logo.pack()
        self.title.pack()
        self.subtitle.pack()
        self.navigate_btn.pack(pady=(70, 0))
        self.about_btn.pack(pady=(10, 0))

# For debugging and testing
if __name__ == "__main__":
    app = ctk.CTk()
    app.minsize(800, 600)
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(0, weight=1)

    theme_path = "/".join([os.getcwd().replace("\\", "/"), "theme.json"])
    ctk.set_default_color_theme(theme_path)

    page = LandingPage(app, app)
    page.grid(row=0, column=0, sticky="nsew")

    app.mainloop()