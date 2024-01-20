from customtkinter import *
from CTkMessagebox import CTkMessagebox
import tkinter
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException
import pyautogui

options = webdriver.EdgeOptions()
options.add_argument("--headless")
drive = webdriver.Edge(options=options)


root = CTk()
root.geometry("750x350")
root.title("Cep treview")
set_appearance_mode("dark")
set_default_color_theme("dark-blue")

def search():
    # Desabilitar o botão enquanto a busca está em andamento
    

    url = "https://buscacepinter.correios.com.br/app/endereco/index.php"

    drive.get(url)
    pyautogui.sleep(2)
    data = cep_input.get()
    drive.find_element(By.NAME, "endereco").send_keys(data)
    pyautogui.sleep(seconds=0.5)
    data = cep_input.get()
    pyautogui.sleep(1)
    drive.find_element(By.NAME, "btn_pesquisar").click()
    pyautogui.sleep(1)


    logradouro = drive.find_element(
        By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]'
    ).text
    
    pyautogui.sleep(1)

    bairro = drive.find_element(
        By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[2]'
    ).text
    bairro__label.configure(text=bairro)
    pyautogui.sleep(1)

    localidade = drive.find_element(
        By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]'
    ).text
    localidade__label.configure(text=localidade)
    pyautogui.sleep(1)

    cep = drive.find_element(
        By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]'
    ).text
    cep__label.configure(text=cep)
    pyautogui.sleep(1)

  
    root.after(2000, lambda: cep_input.delete(0, END))

cep_label = CTkLabel(root, text="CEP", text_color="white", font=("Georgia", 20))
cep_label.grid(row=1, column=0,stick="NSEW")
cep_input = CTkEntry(root, text_color="black", font=("Georgia", 20), fg_color="#FFFAFA")
cep_input.grid(row=1, column=1, columnspan=5,stick="NSEW")
cep_search = CTkButton(root, text="Pesquisar", font=("Georgia", 20),command=search)
cep_search.grid(row=1, column=6, padx=10, stick="NSEW")

# bg_color = root._apply_appearance_mode(ThemeManager.theme["CTkFrame"]["fg_color"])
text_color = root._apply_appearance_mode(ThemeManager.theme["CTkLabel"]["text_color"])
selected_color = root._apply_appearance_mode(
    ThemeManager.theme["CTkButton"]["fg_color"]
)


treestyle = ttk.Style(root)
treestyle.theme_use("alt")
treestyle.configure(
    "Treeview",
    foreground=text_color,
    fieldbackground="#FFFAFA",
    borderwidth=3,
    font=("Georgia", 15),
)

tree_view = ttk.Treeview(root, columns=(1, 2, 3, 4), show="headings")
tree_view.column(1, anchor="center")
tree_view.heading(1, text="Logradouro")
tree_view.column(2, anchor="center")
tree_view.heading(2, text="Bairro")
tree_view.column(3, anchor="center")
tree_view.heading(3, text="Localidade/UF")
tree_view.column(4, anchor="center")
tree_view.heading(4, text="CEP")

tree_view.grid(row=2, column=0, columnspan=12, rowspan=12, stick="NSEW")

root.mainloop()
