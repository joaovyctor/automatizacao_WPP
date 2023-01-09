import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib


contatos_df = pd.read_excel("Enviar.xlsx")
print(contatos_df)

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")
time.sleep(30)

#while len(navegador.find_elements_by_id("side")) <1:
#    time.sleep(1)


# já estamos com o login feito no whatsapp web
for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, "Pessoa"]
    numero = contatos_df.loc[i, "Número"]
    texto = urllib.parse.quote(f"OI {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    time.sleep(15)
    #navegador.find_element_by_xpath(
    enviar = navegador.find_element('xpath',
        '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span').send_keys(Keys.ENTER)
    time.sleep(5)
#input("Digite qualquer letra")