import cv2
import numpy as np
from tkinter import Tk, Button, Label, filedialog, Scale, HORIZONTAL
from PIL import Image, ImageTk
import threading

class ImageProcessingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("多功能影像處理工具箱")
        
        # 初始化變數
        self.image = None
        self.processed_image = None
        self.current_mode = None
        self.cap = None
        self.running = False

        # 介面設計
        Button(root, text="上傳影像", command=self.upload_image).grid(row=0, column=0, padx=5, pady=5)
        Button(root, text="啟用前置鏡頭", command=self.start_webcam).grid(row=0, column=1, padx=5, pady=5)
        Button(root, text="停止鏡頭", command=self.stop_webcam).grid(row=0, column=2, padx=5, pady=5)
        Button(root, text="幾何變換", command=self.activate_geometric_transform).grid(row=0, column=3, padx=5, pady=5)
        Button(root, text="影像濾波", command=self.activate_image_filtering).grid(row=0, column=4, padx=5, pady=5)
        Button(root, text="卡通化影像", command=self.activate_cartoonize_image).grid(row=0, column=5, padx=5, pady=5)

        # 滑桿設置
        self.scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, label="調整參數", command=self.update_image)
        self.scale.grid(row=1, column=0, columnspan=6, padx=5, pady=5)

        # 影像顯示
        self.image_label = Label(root)
        self.image_label.grid(row=2, column=0, columnspan=6, padx=5, pady=5)

    def upload_image(self):
        self.stop_webcam()
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = cv2.imread(file_path)
            self.processed_image = self.image.copy()
            self.display_image(self.image)

    def start_webcam(self):
        self.stop_webcam()
        self.cap = cv2.VideoCapture(0)  # 開啟前置鏡頭
        self.running = True
        threading.Thread(target=self.update_webcam).start()

    def stop_webcam(self):
        if self.cap is not None:
            self.running = False
            self.cap.release()
            self.cap = None

    def update_webcam(self):
        while self.running and self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                break
            self.image = frame
            self.processed_image = self.image.copy()
            if self.current_mode:
                self.update_image()
            else:
                self.display_image(self.image)

    def save_image(self):
        if self.processed_image is not None:
            file_path = filedialog.asksaveasfilename(defaultextension=".jpg",
                                                     filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")])
            if file_path:
                cv2.imwrite(file_path, self.processed_image)
                print("影像已儲存:", file_path)

    def display_image(self, img):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img_pil = Image.fromarray(img_rgb)
        img_tk = ImageTk.PhotoImage(img_pil)
        self.image_label.configure(image=img_tk)
        self.image_label.image = img_tk

    def activate_geometric_transform(self):
        self.current_mode = "geometric"
        self.scale.configure(from_=0, to=360, label="旋轉角度")

    def activate_image_filtering(self):
        self.current_mode = "filtering"
        self.scale.configure(from_=1, to=31, label="濾波器大小")  # 濾波器大小必須是奇數

    def activate_cartoonize_image(self):
        self.current_mode = "cartoon"
        self.scale.configure(from_=5, to=25, label="細膩程度")

    def update_image(self, event=None):
        if self.image is None:
            return
        
        if self.current_mode == "geometric":
            angle = self.scale.get()
            height, width = self.image.shape[:2]
            center = (width // 2, height // 2)
            matrix = cv2.getRotationMatrix2D(center, angle, 1)
            self.processed_image = cv2.warpAffine(self.image, matrix, (width, height))

        elif self.current_mode == "filtering":
            kernel_size = self.scale.get()
            if kernel_size % 2 == 0:  # 確保濾波器大小為奇數
                kernel_size += 1
            self.processed_image = cv2.GaussianBlur(self.image, (kernel_size, kernel_size), 0)

        elif self.current_mode == "cartoon":
            region_size = self.scale.get()
            if region_size % 2 == 0:
                region_size += 1
            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            gray = cv2.medianBlur(gray, 7)
            edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                          cv2.THRESH_BINARY, region_size, 10)
            color = cv2.bilateralFilter(self.image, 9, 250, 250)
            self.processed_image = cv2.bitwise_and(color, color, mask=edges)

        self.display_image(self.processed_image)

if __name__ == "__main__":
    root = Tk()
    app = ImageProcessingApp(root)
    root.mainloop()
