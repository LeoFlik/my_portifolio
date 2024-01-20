# from selenium import webdriver as opcoesSelenium
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import pyautogui as tempoEspera

# #Abre o navegador da Web do Google Chrome
# options = opcoesSelenium.EdgeOptions()
# navegador = opcoesSelenium.Edge(options=options)
# navegador.get("https://www.mercadolivre.com.br/")

# #Procura o campo Name, digita a palavra que queremos procurar e cola
# navegador.find_element(By.NAME, "as_word").send_keys("carteira")

# #Aguarda 2 segundos
# tempoEspera.sleep(2)

# #Procura o botão com o XPATH e clica no botão para pesquisar
# # navegador.find_element(By.XPATH, "/html/body/header/div/form/button").click()
# tempoEspera.press('return')

# #Aguarda 6 segundos
# tempoEspera.sleep(6)

# dadosProduto = navegador.find_elements(By.CSS_SELECTOR, '#root-app  div  div.ui-search-main.ui-search-main--only-products.ui-search-main--with-topkeywords  section ')


# # linha = 2
# for informacoes in dadosProduto:

#     nomeProduto = informacoes.find_element(By.XPATH, '//*[@id=":rk:"]/div[2]/div[1]/div[1]/a/h2').text
#     precoProduto = informacoes.find_element(By.XPATH,'//*[@id=":rk:"]/div[2]/div[1]/div[2]/div/div/div/span[1]/span[2]').text

#     # try:
#     #     centavosProduto = informacoes.find_element(By.CLASS_NAME, "price-tag-cents").text
#     # except:
#     #     centavosProduto = "0"

#     urlProduto = informacoes.find_element(By.XPATH,'//*[@id=":rk:"]/div[2]/div[1]/div[1]/a').get_attribute("href")

#     print(nomeProduto + " - " + precoProduto + "," + " - " + urlProduto)
# importando as bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui as pa
import openpyxl
import os
from icecream import ic

from customtkinter import *
import CTkMessagebox

root = CTk()


root.mainloop()

# # adicionando as variaveis gerais
# url = "https://www.mercadolivre.com.br/"
# # address_workbook = "shoes_mercado_livre.xlsx"
# options = webdriver.EdgeOptions()
# driver = webdriver.Edge(options=options)
# # workbook = openpyxl.load_workbook(address_workbook)
# # active_workbook = workbook["Planilha1"]
# search = "tênis masculino tamanho 40 frete grátis"

# # pegando os dados de precos da pagina
# driver.get(url)
# pa.sleep(2)
# search_bar = driver.find_element(By.CLASS_NAME, "nav-search-input").send_keys(search)
# pa.sleep(2)
# pa.press("return")
# pa.sleep(6)

# list = driver.find_elements(By.XPATH, '//*[@id="root-app"]/div/div[2]/section/ol')
# print(len(list))

# for i in list:
#     print(
#         i.find_element(
#             By.XPATH, '//*[@id="root-app"]/div/div[2]/section/ol/div[2]'
#         ).get_attribute("id")
#     )

from CTkMessagebox import CTkMessagebox
import customtkinter

def show_info():
    # Default messagebox for showing some information
    CTkMessagebox(title="Info", message="This is a CTkMessagebox!")

def show_checkmark():
    # Show some positive message with the checkmark icon
    CTkMessagebox(message="CTkMessagebox is successfully installed.",
                  icon="check", option_1="Thanks")
    
def show_error():
    # Show some error message
    CTkMessagebox(title="Error", message="Something went wrong!!!", icon="cancel")
    
def show_warning():
    # Show some retry/cancel warnings
    msg = CTkMessagebox(title="Warning Message!", message="Unable to connect!",
                  icon="warning", option_1="Cancel", option_2="Retry")
    
    if msg.get()=="Retry":
        show_warning()
        
def ask_question():
    # get yes/no answers
    msg = CTkMessagebox(title="Exit?", message="Do you want to close the program?",
                        icon="question", option_1="Cancel", option_2="No", option_3="Yes")
    response = msg.get()
    
    if response=="Yes":
        app.destroy()       
    else:
        print("Click 'Yes' to exit!")
              
app = customtkinter.CTk()
app.rowconfigure((0,1,2,3,4,5), weight=1)
app.columnconfigure(0, weight=1)
app.minsize(200,250)

customtkinter.CTkLabel(app, text="CTk Messagebox Examples").grid(padx=20)
customtkinter.CTkButton(app, text="Check CTkMessagebox", command=show_checkmark).grid(padx=20, pady=10, sticky="news")
customtkinter.CTkButton(app, text="Show Info", command=show_info).grid(padx=20, pady=10, sticky="news")
customtkinter.CTkButton(app, text="Show Error", command=show_error).grid(padx=20, pady=10, sticky="news")
customtkinter.CTkButton(app, text="Show Warning", command=show_warning).grid(padx=20, pady=10, sticky="news")
customtkinter.CTkButton(app, text="Ask Question", command=ask_question).grid(padx=20, pady=(10,20), sticky="news")

app.mainloop()

