# from MinHeap import Min_Heap
# heap = Min_Heap()
import tkinter as tk
from PIL import Image, ImageTk
class Pill_Reminder_App:
    def __init__(self,root):
        self.root = root
        self.root.title("Pill-Reminder")
        self.root.geometry("700x400")
        self.root.resizable(False, False)
        
                # --- بارگذاری عکس پس‌زمینه ---
        self.bg_image = Image.open("Screenshot 2026-01-07 224538.png")      # مسیر عکس خودت
        self.bg_image = self.bg_image.resize((700, 400))  # اندازه با پنجره هماهنگ
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        # Label برای پس‌زمینه
        self.bg_label = tk.Label(self.root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.label = tk.Label(self.root,text="مدیریت قرص ها",font=("Arial",30),bg="#FFFFFF")
        self.label.place(x=230,y=10)

        self.main_frame = tk.Frame(self.root,bg="#FFFFFF")
        self.main_frame.place(x=150,y=90)
##8ACAE3
        
        self.insert_btn = tk.Button(self.main_frame,text="افزودن قرص",command=self.insert_pill,width=12,height=2,font=("Arial",14))
        self.delete_btn = tk.Button(self.main_frame,text="حذف قرص",command=self.insert_pill,width=12,height=2,font=("Arial",14))
        self.search_btn = tk.Button(self.main_frame,text="جستجو قرص",command=self.insert_pill,width=12,height=2,font=("Arial",14))
        self.update_btn = tk.Button(self.main_frame,text="ویرایش قرص",command=self.insert_pill,width=12,height=2,font=("Arial",14))
        self.showAll_btn = tk.Button(self.main_frame,text="مشاهده قرص ها",command=self.insert_pill,width=12,height=2,font=("Arial",14))
        self.exit_btn = tk.Button(self.main_frame,text="خروج",command=self.insert_pill,width=12,height=2,font=("Arial",14))
        
        self.insert_btn.grid(row=0, column=0, padx=25, pady=14)
        self.delete_btn.grid(row=0, column=1, padx=25, pady=14)
        self.search_btn.grid(row=1, column=0, padx=25, pady=14)
        self.update_btn.grid(row=1, column=1, padx=25, pady=14)
        self.showAll_btn.grid(row=2, column=0, padx=25, pady=14)
        self.exit_btn.grid(row=2, column=1, padx=25, pady=14)

    def insert_pill(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = Pill_Reminder_App(root)
    root.mainloop()