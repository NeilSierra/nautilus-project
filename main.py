from customtkinter import *             # pip install customtkinter
from PIL import Image, ImageTk          # pip install pillow

# Design variables
creamy_white        = "#f8f7f2"
light_red           = "#f3cbc5"
dark_red            = "#790b0c"
dark_gray           = "#1f1f1f"

class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("Nautilus: Campus Navigator")
        self.iconbitmap("sources/favicon.ico")
        self.minsize(800, 600)

        # Main frame that expands to the whole window
        # Holds all the pages
        main_frame = CTkFrame(self)
        main_frame.pack(fill="both", expand=True)
        main_frame.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)

        # Pages holder
        self.pages = {}

        # Add pages to dict
        for index, Page in enumerate((LandingPage, MapView)):
            frame = Page(master=main_frame, control=self)
            self.pages[index] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        # Call the fuction
        self.change_page(0)
    
    def change_page(self, index):
        # Get the page by index
        page = self.pages[index]
        # Bring to front
        page.tkraise()

class LandingPage(CTkFrame):
    def __init__(self, master, control):
        super().__init__(master)
        self.configure(fg_color=creamy_white)

        self.wave_imge = ImageTk.PhotoImage(Image.open("sources/landing_page_wave.png"))
        wave_background = CTkLabel(self, text="", image=self.wave_imge)
        wave_background.place(relx=0, rely=0, relwidth=1, relheight=1, anchor="nw")

        # Center frame
        center_frame = CTkFrame(self, fg_color=creamy_white)
        center_frame.pack(expand=True)

        # Nautilus logo
        self.logo_photo = ImageTk.PhotoImage(Image.open("sources/logo.png").resize((300, 300)))
        nautilus_logo = CTkLabel(center_frame, text="", image=self.logo_photo, fg_color=creamy_white)
        nautilus_logo.pack()

        # Title and subtitle
        title = CTkLabel(
            center_frame,
            text="N A U T U L I S", font=("Helvetica", 50, "bold"),
            fg_color=creamy_white, text_color=dark_red
        )
        subtitle = CTkLabel(
            center_frame,
            text="Campus Navigator", font=("Arial", 30),
            fg_color=creamy_white, text_color=dark_gray
        )
        title.pack()
        subtitle.pack(pady=(0, 80))

        # Buttons
        navigation_btn = CTkButton(
            center_frame, height=40, width=300,
            text="START NAVIGATING", font=("Arial", 20, "bold"),
            fg_color=dark_red, text_color=creamy_white, hover_color=dark_gray,
            command=lambda: control.change_page(1)
        )
        view_btn = CTkButton(
            center_frame, height=40, width=300,
            text="VIEW CAMPUS PLACES", font=("Arial", 20, "bold"),
            border_color=dark_red, border_width=2, corner_radius=5,
            fg_color=creamy_white, text_color=dark_red, hover_color=light_red,
            command=...
        )
        navigation_btn.pack(pady=(0, 10))
        view_btn.pack()

class MapView(CTkFrame):
    def __init__(self, master, control):
        super().__init__(master)
        self.configure(fg_color=dark_red)

        # Center frame
        center_frame = CTkFrame(self, fg_color=dark_red)
        center_frame.pack(expand=True)

        # Buttons
        back_btn = CTkButton(
            center_frame, height=40, width=300,
            text="BACK", font=("Arial", 20, "bold"),
            fg_color=dark_gray, text_color=creamy_white,
            command=lambda: control.change_page(0)
        )
        back_btn.pack()


app = App()
app.mainloop()