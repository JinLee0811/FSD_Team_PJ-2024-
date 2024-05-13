# Entry point of the application

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
        super().__init__()
        self.title("GUIUniApp")
        self.geometry("375x612")
        self.resizable(False, False)

        self.loading_screen = LoadingScreen(self)
        self.loading_screen.pack(fill=tk.BOTH, expand=True)
        self.after(3000, self.show_login_frame)

    def show_login_frame(self):
        self.loading_screen.destroy()
        self.controller = GUIUniAppController(self)


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
