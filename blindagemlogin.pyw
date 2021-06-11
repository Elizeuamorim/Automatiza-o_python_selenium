#Para estar realizando tem que fazer a instalação do Selenium "pip install selenium"
#também baixando o webdriver do selenium e colocando na pasta do python
#instalando o pymsgbox com o mesmo "pip install pymsgbox" para utilizar os alertas dessa biblioteca
from time import sleep
#para importar o webdriver do selenium
import pymsgbox
#Import para aparecer o alerta
from selenium import webdriver
#importar o webdriver da biblioteca Selenium
login = pymsgbox.prompt('Digite o login para tirar a blindagem?')
#transformar o login digitado em pelo usuário em uma variável
login1 =login.format();
#transformar a variável digitada em string
navegador = webdriver.Chrome();
#abrir o navegador
navegador.get("https://sitenet.serasa.com.br/Logon/autentica")
#abrir o site que deseja 
navegador.find_element_by_id("LOGON").send_keys("colocar login")
navegador.find_element_by_id("SENHA").send_keys("colocar senha")
#para encontrar a parte do sistema que deseja colocar e aqui já informo a senha que desejo
navegador.find_element_by_id("acessar").click()
#encontrar o botão de acesso e chamar o evento do click
sleep(5)
navegador.find_element_by_xpath('//*[@id="navbar-header"]/ul[2]/li[1]/a').click()
navegador.find_element_by_xpath('//*[@id="navbar-header"]/ul[2]/li[1]/ul/li[3]/a').click()
navegador.find_element_by_id("hylLogonBlindado").click()
#navegando pelo site por xpath e utilizando o evento de clicar
navegador.find_element_by_id("txtLogon").send_keys(login1)
#encontrando o elemento e adicionando o login que quero utilizar
navegador.find_element_by_id("lnkEnviar").click()
#clicar no botão de enviar
resultado = navegador.find_element_by_id("dialog").text
#gravar o resultado que o serasa mandou em uma variável
pymsgbox.alert(resultado)
#mostrar o resultado em um alerta
navegador.quit()
#sair do sistema

