# from MinHeap import Min_Heap
# heap = Min_Heap()
import tkinter as tk
from ManageSystem import ManageSystem 
from PIL import Image, ImageTk
class Pill_Reminder_App:
    def __init__(self,root):
        self.ms = ManageSystem()
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
        self.main_frame.place(x=200,y=90)
        
        self.notifn = tk.Label(self.root,text="اعلانات",font=("Arial",17),bg="#FFFFFF")
        self.notifn.place(x=70,y=56)        
        self.notif = tk.Label(self.root,text="",font=("Arial",10),bg="#FFFFFF",width=20,height=17)
        self.notif.place(x=20,y=85)
##8ACAE3
        
        self.insert_btn = tk.Button(self.main_frame,text="افزودن قرص",command=self.insert_pill,width=12,height=2,font=("Arial",14))
        self.delete_btn = tk.Button(self.main_frame,text="حذف قرص",command=self.insert_pill,width=12,height=2,font=("Arial",14))
        self.search_btn = tk.Button(self.main_frame,text="جستجو قرص",command=self.insert_pill,width=12,height=2,font=("Arial",14))
        self.update_btn = tk.Button(self.main_frame,text="ویرایش قرص",command=self.insert_pill,width=12,height=2,font=("Arial",14))
        self.showAll_btn = tk.Button(self.main_frame,text="مشاهده قرص ها",command=self.showAll,width=12,height=2,font=("Arial",14))
        self.exit_btn = tk.Button(self.main_frame,text="خروج",command=self.insert_pill,width=12,height=2,font=("Arial",14))
        
        self.insert_btn.grid(row=0, column=0, padx=25, pady=14)
        self.delete_btn.grid(row=0, column=1, padx=25, pady=14)
        self.search_btn.grid(row=1, column=0, padx=25, pady=14)
        self.update_btn.grid(row=1, column=1, padx=25, pady=14)
        self.showAll_btn.grid(row=2, column=0, padx=25, pady=14)
        self.exit_btn.grid(row=2, column=1, padx=25, pady=14)

    def insert_pill(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("افزودن قرص")
        add_window.geometry("700x400")
        add_window.resizable(False, False)
        
        tk.Label(add_window, text="نام قرص :").place(x=140,y=30)
        pillName = tk.Entry(add_window,font=("Arial",17))
        pillName.place(x=210,y=30)
        
                
        tk.Label(add_window, text="مدت زمان:").place(x=140,y=90)
        pillIntervalH = tk.Entry(add_window,font=("Arial",17))
        pillIntervalH.place(x=210,y=90)
        
                
        tk.Label(add_window, text="تعداد قرص :").place(x=140,y=140)
        pillQuantity = tk.Entry(add_window,font=("Arial",17))
        pillQuantity.place(x=210,y=140)
        
        tk.Button(add_window,text="ثبت",command=lambda:self.add_pill(pillName.get(),pillIntervalH.get(),pillQuantity.get()),width=25,font=("Arial",17)).place(x=140,y=230)
        tk.Button(add_window,text="خروج",command=add_window.destroy,width=25,font=("Arial",17)).place(x=140,y=290)
        
        
        
    
    def add_pill(self,name,itvh,quantity):
        itvh = int(itvh)
        quantity = int(quantity)
        self.ms.insert(name,itvh,quantity)
        
    
    def showAll(self):
        show_window = tk.Toplevel(self.root)
        show_window.title("مشاهده قرص ها")
        show_window.geometry("700x400")
        show_window.resizable(False, False)
        
        # tk.Label(show_window, text="قرص ها").place(x=140,y=30)
        self.allPill = tk.Label(show_window,text="",font=("Arial",10),bg="#B8B8B8",width=80,height=15)
        self.allPill.place(x=23,y=15)
        
        text = self.ms.showAll()
        
        self.allPill.config(text=text)
        
        tk.Button(show_window,text="خروج",command=show_window.destroy,width=25,font=("Arial",17)).place(x=155,y=290)
            


if __name__ == "__main__":
    root = tk.Tk()
    app = Pill_Reminder_App(root)
    root.mainloop()