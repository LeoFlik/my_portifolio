from customtkinter import *


window = CTk(fg_color="#e6e6e6")
window.geometry("800 x 800")
window._set_appearance_mode("System")
window.title("My first App")
window.state("withdrawn")

my_font = CTkFont(family="<Georgia", size=45, slant="italic")
frame = CTkFrame(master=window, width=200, height=200, border_color="grey").pack()

label = CTkLabel(
    master=frame,
    text="This is a Test",
    font=my_font,
    corner_radius=30,
    compound="left",
)
label.pack()

window.mainloop()
