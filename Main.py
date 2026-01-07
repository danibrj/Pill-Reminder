# from MinHeap import Min_Heap
# heap = Min_Heap()
import tkinter as tk

class Pill_Reminder_App:
    def __init__(self,root):
        self.root = root
        self.root.title("Pill-Reminder")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
                
        self.label = tk.Label(self.root,text="مدیریت قرص ها",font=("Arial",30))
        self.label.pack(padx=0)

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=20)
        
        self.insert_btn = tk.Button(self.main_frame,text="افزودن قرص",command=self.insert_pill,width=20,height=2)
        self.delete_btn = tk.Button(self.main_frame,text="خذف قرص",command=self.insert_pill,width=20,height=2)
        self.search_btn = tk.Button(self.main_frame,text="جستجو قرص",command=self.insert_pill,width=20,height=2)
        self.update_btn = tk.Button(self.main_frame,text="ویرایش قرص",command=self.insert_pill,width=20,height=2)
        self.showAll_btn = tk.Button(self.main_frame,text="مشاهده قرص ها",command=self.insert_pill,width=20,height=2)
        self.exit_btn = tk.Button(self.main_frame,text="خروج",command=self.insert_pill,width=20,height=2)
        
        self.insert_btn.grid(row=0, column=0, padx=5, pady=20)
        self.delete_btn.grid(row=0, column=1, padx=5, pady=20)
        self.search_btn.grid(row=1, column=0, padx=5, pady=20)
        self.update_btn.grid(row=1, column=1, padx=5, pady=20)
        self.showAll_btn.grid(row=2, column=0, padx=5, pady=20)
        self.exit_btn.grid(row=2, column=1, padx=5, pady=20)

    def insert_pill(self):
        pass


if __name__ == "__main__":
    root = tk.Tk()
    app = Pill_Reminder_App(root)
    root.mainloop()