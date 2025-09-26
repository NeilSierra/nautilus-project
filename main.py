import customtkinter as ctk
import os as os

# Import pages
from modules.landingPage import LandingPage
from modules.mapViewPage import MapViewPage

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("NAUTILUS: Campus Navigator")
        self.minsize(800, 600)

        # Set color theme
        self.theme_path = "/".join([os.getcwd().replace("\\", "/"), "theme.json"])
        ctk.set_default_color_theme(self.theme_path)

        # Frame to hold the pages
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Store pages classes
        self.pages = [LandingPage, MapViewPage]
        self.pagesList = {} # Store pages with numbering

        # Iterate and list the page with number
        for n, Page in enumerate(self.pages):
            frame = Page(master=self.main_frame, control=self)
            self.pagesList[n] = frame
            frame.grid(row=0, column=0, sticky="nsew") # Pack page to occupy the screen
        
        # Raise the landing page
        self.change_page(0)

    def change_page(self, n):
        page = self.pagesList[n]
        page.tkraise()

# Run the app
app = App()
app.mainloop()