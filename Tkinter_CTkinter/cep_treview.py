from customtkinter import *
from customtkinter import filedialog
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



def automatic_search():
        caminho_arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo",
        filetypes=[("Texto", "*.txt")]
    )
        if caminho_arquivo:
            with open(caminho_arquivo,'+r') as file:
              input = file.readlines()
              lista_ceps =[cep.strip() for cep in input]
              print(lista_ceps)
    
        search_two(lista_ceps)
    

def search_two(dados):
    # Desabilitar o botão enquanto a busca está em andamento
    
    for i in dados:
            if i != 'CEP':
                print(i)
                data = i


                url = "https://buscacepinter.correios.com.br/app/endereco/index.php"

                drive.get(url)
                pyautogui.sleep(2)
                #data = cep_input.get()
                drive.find_element(By.NAME, "endereco").send_keys(data)
                pyautogui.sleep(seconds=0.5)
                #data = cep_input.get()
                
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

                pyautogui.sleep(1)

                localidade = drive.find_element(
                    By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]'
                ).text
            
                pyautogui.sleep(1)

                cep = drive.find_element(
                    By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]'
                ).text
            
                pyautogui.sleep(3)

                tree_view.insert('',END,values= (logradouro,bairro,localidade,cep))

                drive.find_element(By.XPATH,'//*[@id="btn_nbusca"]').click()

                pyautogui.sleep(2)

    
        #root.after(2000, lambda: cep_input.delete(0, END))

def search():
    # Desabilitar o botão enquanto a busca está em andamento
    
  


        url = "https://buscacepinter.correios.com.br/app/endereco/index.php"

        drive.get(url)
        pyautogui.sleep(2)
        data = cep_input.get()
        drive.find_element(By.NAME, "endereco").send_keys(data)
        pyautogui.sleep(seconds=0.5)
        #data = cep_input.get()
        
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

        pyautogui.sleep(1)

        localidade = drive.find_element(
            By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[3]'
        ).text
    
        pyautogui.sleep(1)

        cep = drive.find_element(
            By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[4]'
        ).text
    
        pyautogui.sleep(3)

        tree_view.insert('',END,values= (logradouro,bairro,localidade,cep))

    

        root.after(2000, lambda: cep_input.delete(0, END))



cep_label = CTkLabel(root, text="CEP", text_color="white", font=("Sans", 20))
cep_label.grid(row=1, column=0,stick="NSEW")
cep_input = CTkEntry(root, text_color="black", font=("Sans", 20), fg_color="#FFFAFA")
cep_input.grid(row=1, column=1, columnspan=5,stick="NSEW")
cep_input.focus()
cep_search = CTkButton(root, text="Pesquisar", font=("Sans", 20),command=search)
cep_search.grid(row=1, column=6, padx=10, stick="NSEW")
auto_search = CTkButton(root, text="AutoBusca", font=("Sans", 20),command=automatic_search)
auto_search.grid(row=1, column=8, padx=10, stick="NSEW")

# bg_color = root._apply_appearance_mode(ThemeManager.theme["CTkFrame"]["fg_color"])
#text_color = root._apply_appearance_mode(ThemeManager.theme["CTkLabel"]["text_color"])
selected_color = root._apply_appearance_mode(
    ThemeManager.theme["CTkButton"]["fg_color"]
)


treestyle = ttk.Style(root)
treestyle.theme_use("alt")
treestyle.configure(
    "Treeview",
    foreground='black',
    fieldbackground="#FFFAFA",
    borderwidth=3,
    font=("Sans", 10), sep='.'
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

tree_view.grid(row=2, column=0, columnspan=14, stick="NSEW")

root.mainloop()
