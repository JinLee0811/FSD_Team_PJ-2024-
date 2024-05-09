import os
import sys
import tkinter as tk
import datetime

from guicontroller.controller import GUIUniAppController
from guiframe.view import LoadingScreen 

# 현재 스크립트가 위치한 디렉토리 경로를 가져옵니다.
current_dir = os.path.dirname(os.path.abspath(__file__))
# 현재 스크립트의 부모 디렉토리(즉, src 디렉토리의 부모)의 경로를 얻습니다.
parent_dir = os.path.dirname(current_dir)
# 부모 디렉토리를 sys.path에 추가합니다.
sys.path.append(parent_dir)

class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('GUIUniApp')
        self.geometry('375x612')
        self.resizable(False, False)

        # 로딩 화면 표시
        self.loading_screen = LoadingScreen(self)
        self.loading_screen.pack(fill=tk.BOTH, expand=True)
        self.after(3000, self.show_login_frame)  # 3초 후 로그인 프레임 표시

    def show_login_frame(self):
        self.loading_screen.destroy()  # 로딩 화면 제거
        self.controller = GUIUniAppController(self)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
    