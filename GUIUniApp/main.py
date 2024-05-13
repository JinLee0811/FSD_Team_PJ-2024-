import os
import sys

# Get and add parent directory paths to the system path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import tkinter as tk
from guicontroller.controller import GUIUniAppController
from guiframe.view import LoadingScreen

class MainApplication(tk.Tk):
    def __init__(self):
        # Initialize the Tkinter root window
        super().__init__()
        self.title("GUIUniApp")
        self.geometry("375x612")
        self.resizable(False, False)

        # Create and pack the loading screen
        self.loading_screen = LoadingScreen(self)
        self.loading_screen.pack(fill=tk.BOTH, expand=True)
        
        # Schedule the show_login_frame method to be called after 3 seconds
        self.after(3000, self.show_login_frame)  

    def show_login_frame(self):
         # Destroy the loading screen
        self.loading_screen.destroy()
         # Create an instance of the GUIUniAppController
        self.controller = GUIUniAppController(self)

# Entry point of the application
if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()

