import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk

class PokemonGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokemon Adventure")
        self.root.geometry("600x500")  # 設定視窗大小 (寬x高)

        self.player = {
            "name": "",
            "pokemon": None,
            "items": {"potion": 3},
            "storage": []
        }

        self.create_main_menu()


    def create_main_menu(self):
        self.clear_screen()

        # 加載圖片
        image_path = "game_homepage.png"
        image = Image.open(image_path)
        self.image_width, (self.image_height-200) = image.size  # 取得圖片尺寸
        self.bg_image = ImageTk.PhotoImage(image)

        # 設定視窗大小根據圖片
        self.root.geometry(f"{self.image_width}x{self.image_height}")

        # 顯示圖片
        tk.Label(self.root, image=self.bg_image).pack()

        # 標題
        tk.Label(self.root, text="歡迎來到 Pokemon 世界！", font=("Arial", 16)).pack()

        # 按鈕
        tk.Button(self.root, text="創建帳號", command=self.create_account).pack()
        tk.Button(self.root, text="開始冒險", command=self.start_adventure).pack()
        tk.Button(self.root, text="離開遊戲", command=self.root.quit).pack()



    def create_account(self):
        self.clear_screen()
        tk.Label(self.root, text="請輸入你的訓練家名稱: ").pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()
        tk.Button(self.root, text="確定", command=self.set_player_name).pack()
    
    def set_player_name(self):
        name = self.name_entry.get()
        if name:
            self.player["name"] = name
            messagebox.showinfo("成功！", f"你的訓練家名稱設定為 {name}！")
            self.choose_pokemon()
        else:
            messagebox.showwarning("錯誤", "名稱不能為空！")
    
    def choose_pokemon(self):
        self.clear_screen()
        tk.Label(self.root, text="選擇你的初始寶可夢: ").pack()
        for pokemon in ["小火龍", "傑尼龜", "妙蛙種子"]:
            tk.Button(self.root, text=pokemon, command=lambda p=pokemon: self.set_pokemon(p)).pack()
    
    def set_pokemon(self, pokemon):
        self.player["pokemon"] = pokemon
        messagebox.showinfo("成功！", f"你選擇了 {pokemon}！")
        self.create_main_menu()
    
    def start_adventure(self):
        if not self.player["name"] or not self.player["pokemon"]:
            messagebox.showwarning("警告", "請先創建帳號並選擇寶可夢！")
            return
        self.explore()

    def explore(self):
        self.clear_screen()
        tk.Label(self.root, text="你正在冒險中...").pack()
        tk.Button(self.root, text="遇到野生寶可夢！", command=self.wild_pokemon_encounter).pack()
        tk.Button(self.root, text="返回主選單", command=self.create_main_menu).pack()
    
    def wild_pokemon_encounter(self):
        wild_pokemon = random.choice(["皮卡丘", "波波", "小拉達"])
        self.clear_screen()
        tk.Label(self.root, text=f"你遇到了野生的 {wild_pokemon}！").pack()
        tk.Button(self.root, text="丟出精靈球", command=lambda: self.catch_pokemon(wild_pokemon)).pack()
        tk.Button(self.root, text="逃跑", command=self.explore).pack()
    
    def catch_pokemon(self, pokemon):
        success = random.randint(1, 10) > 4
        if success:
            self.player["storage"].append(pokemon)
            messagebox.showinfo("成功！", f"你捕捉了 {pokemon}！")
        else:
            messagebox.showinfo("失敗", f"{pokemon} 掙脫了！")
        self.explore()
    
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = PokemonGame(root)
    root.mainloop()
