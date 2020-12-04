from tkinter import ttk
from tkinter import *
from tkinter import messagebox
import os,shutil

root=Tk()

root.title('Arrangemet System')
root.geometry('600x400')
root.resizable(0,0)

frame = Frame(root,bg='red')
frame.pack(fill=BOTH,expand=True)

img = PhotoImage(file="pic.png")
root1= ttk.Label(frame,image=img)
root1.pack(fill=BOTH,expand=True) 

path1=StringVar()

# Function
def arrange():
    Files_Extension = {
            
        'Audio_Extension' : ('.mp3','.MP3','.M4A','.m4a','.WAV','.WMA','.wma'),
        'Video_Extension' : ('.MP4','.mp4','.flv'),
        'Document_Extension' : ('.pdf','.doc','.txt','.docx','.mdb'),
        'Image_Extension' : ('.jpg','.jpeg','.png','.JPG','.JPEG','.PNG'),
        'Software_Extension' : ('.exe','.EXE','.ISO','.iso'),
        'Zip_Files' : ('.7z','.zip','.7Z','.ZIP'),
        'Python_Extension' : ('.py'),
        'Java_Extension' : ('.java','.class'),
    }


    def Arrange(path,extensions):
        File1=[]
        for file in os.listdir(path):
            for ext in extensions:
                if file.endswith(ext):
                    File1.append(file)
        return File1


    path=path1.get()

    if os.path.exists(path):
        for extension_type,extension_name in Files_Extension.items():
            folder_name=extension_type.split('_')[0] + ' Files'

            final_path = os.path.join(path,folder_name)

            if os.path.exists(final_path):
                for item in Arrange(path,extension_name):
                    item_path = os.path.join(path,item)
                    shutil.move(item_path,final_path)

            elif len(Arrange(path,extension_name))==0:
                pass

            else:
                os.mkdir(final_path)
                for item in Arrange(path,extension_name):
                    item_path = os.path.join(path,item)
                    shutil.move(item_path,final_path)
        messagebox.showinfo('Success','Your files has been arranged')
    else:
        messagebox.showinfo('Warning','You have entered incorrect path')
  

def exitarrange():
    messagebox.showinfo('Exit','Thank You')
    exit()


# Look
headinglbl = Label(root1,text='Arrangement System',font=('algerian',30,'bold'),bg='aqua',fg='red')
headinglbl.pack(fill=X)

pathlbl = Label(root1,text='Path',font=('algerian',20,'bold'),bg='black',fg='white')
pathlbl.place(x=260,y=100)

pathentry = Entry(root1,font=('arial',20,'bold'),width=30,textvariable=path1)
pathentry.place(x=80,y=150)

btn = Button(root1,font=('arial',20,'bold'),text='Arrange',bg='aqua',fg='red',command=arrange)
btn.place(x=240,y=200)

btn2 = Button(root1,font=('arial',20,'bold'),text='Exit',bg='aqua',fg='red',command=exitarrange,width=7)
btn2.place(x=240,y=280)

root.mainloop()