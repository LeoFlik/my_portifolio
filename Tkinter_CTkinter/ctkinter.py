from customtkinter import *
from PIL import Image, ImageTk

root = CTk(fg_color="#FAF0E6")
root.geometry("460x260")
set_appearance_mode("light")
set_default_color_theme("green")

image_path = CTkImage(light_image=Image.open("plano_fundo.png"), size=(460, 260))


labelParaFundo = CTkLabel(root, image=image_path)
labelParaFundo.pack()

root.mainloop()
