from customtkinter import *
from CTkMessagebox import CTkMessagebox
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
root.geometry("900x500")
root.title("Busca Cep")
set_appearance_mode("light")
set_default_color_theme("dark-blue")


# def search():


#     url = "https://buscacepinter.correios.com.br/app/endereco/index.php"

#     drive.get(url)
#     pyautogui.sleep(2)
#     data = cep_input.get()
#     drive.find_element(By.NAME,'endereco').send_keys(data)
#     pyautogui.sleep(2)
#     data = cep_input.get()
#     pyautogui.sleep(2)
#     drive.find_element(By.NAME,'btn_pesquisar').click()
#     pyautogui.sleep(2)
#     try:
#       logradouro =drive.find_element(By.XPATH,'//*[@id="resultado-DNEC"]/tbody/tr/td[1]').text
#       logradouro__label.configure(text= logradouro)
#       pyautogui.sleep(1)
#       bairro =drive.find_element(By.XPATH,'//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text
#       bairro__label.configure(text=bairro)
#       pyautogui.sleep(1)
#       localidade =drive.find_element(By.XPATH,'//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text
#       localidade__label.configure(text=localidade)
#       pyautogui.sleep(1)
#       cep = (drive.find_element(By.XPATH,'//*[@id="resultado-DNEC"]/tbody/tr/td[4]').text)
#       cep__label.configure(text=cep)
#       pyautogui.sleep(3)

#     except NoSuchElementException:
#         erro__label.configure(text="CEP não encontrado")
#         new_search()

#     new_search()


def search():
    # Desabilitar o botão enquanto a busca está em andamento
    buscar.configure(state="disabled")

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

    try:
        logradouro = drive.find_element(
            By.XPATH, '//*[@id="resultado-DNEC"]/tbody/tr/td[1]'
        ).text
        logradouro__label.configure(text=logradouro)
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

    except NoSuchElementException:
        cep__label.configure(text="CEP não encontrado")
        logradouro__label.configure(text="")
        bairro__label.configure(text="")
        localidade__label.configure(text="")

    # Habilitar o botão após a busca ou em caso de erro
    buscar.configure(state="normal")
    root.after(2000, lambda: cep_input.delete(0, END))


descpriton_label = CTkLabel(
    master=root,
    text="Digite o CEP que deseja buscar no campo abaixo.",
    text_color="black",
    width=150,
    height=45,
    font=("Sans ", 30),
)
descpriton_label.place(x=35, y=50)
holder_frame = CTkFrame(
    root,
    width=160,
    height=55,
    border_width=4,
    bg_color="#A9A9A9",
    border_color="#808080",
)
holder_frame.place(x=35, y=100)

cep_label = CTkLabel(
    master=holder_frame,
    text="CEP:",
    text_color="black",
    width=150,
    height=45,
    font=("Sans ", 30),
)
cep_label.place(x=3, y=3)  # Ajuste as coordenadas conforme necessário

cep_input = CTkEntry(
    root,
    font=("Sans ", 30),
    width=160,
    height=55,
)
cep_input.focus()
cep_input.place(x=225, y=100)

buscar = CTkButton(
    root, text="Pesquisar", font=("Sans ", 30), width=160, height=35, command=search
)

buscar.place(x=400, y=105)


logradouro_head_label = CTkLabel(
    master=root, text="Logradouro:", text_color="black", font=("Sans ", 35)
)

logradouro_head_label.place(x=35, y=200)

logradouro__label = CTkLabel(
    master=root, text="", text_color="black", font=("Sans ", 35)
)

logradouro__label.place(x=240, y=200)

bairro_head_label = CTkLabel(
    master=root, text="Bairro/Distrito:", text_color="black", font=("Sans ", 35)
)

bairro_head_label.place(x=35, y=250)

bairro__label = CTkLabel(master=root, text="", text_color="black", font=("Sans ", 35))

bairro__label.place(x=270, y=250)

localidade_head_label = CTkLabel(
    master=root, text="Localidade/UF:", text_color="black", font=("Sans ", 35)
)

localidade_head_label.place(x=35, y=300)

localidade__label = CTkLabel(
    master=root, text="", text_color="black", font=("Sans ", 35)
)

localidade__label.place(x=290, y=300)

cep_head_label = CTkLabel(
    master=root, text="CEP:", text_color="black", font=("Sans ", 35)
)

cep_head_label.place(x=35, y=350)

cep__label = CTkLabel(master=root, text="", text_color="black", font=("Sans ", 35))

cep__label.place(x=130, y=350)


root.mainloop()
