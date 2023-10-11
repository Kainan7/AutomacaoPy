#Passo 1: Entrar no sistema da empresa (simulação)
    #link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
#Passo2 : Fazer login
#Passo3: Importa a base de dados de produtos
#Passo4: Cadastrar 1 produto
#Passo5: Repetir o cadastro para todos os produtos

#pyautogui permite controlar o seu mouse, teclado e a tela do computador com os códigos
import pyautogui
import time #permite controle o "tempo"

#pyautogui.click -> clicar com o mouse
#pyautogui.write -> escreve um texto
#pyautogui.press -> apertar 1 tecla só
#pyautogui.hotkey -> atalha (combinação com control) 


pyautogui.PAUSE = 0.3 #pausa que o pyautogui vai dar, em cada comando dele, vai esperar 0,5
#PASSO 1 abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
#entrar no link
link = ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.write(link)
pyautogui.press("enter")
#esperar o site carregar
time.sleep(1)
#PASSO 2 fazer login
pyautogui.click(x=560, y=467) #clicks = 1, significa que vai dar apenas 1 clique, se quiser mais ponha 2 e daí vai. Se quiser clicar com o lado direito, buttown = "left"6.5        

pyautogui.write("victorkainan@outlook.com")

pyautogui.press("tab") #pula para a "senha"
pyautogui.write("sua senha aqui")

pyautogui.press("tab") #pula para o "entrar"
pyautogui.press("enter")

time.sleep(1)

#PASSO 3: IMPORTAR A BASE DE DADOS DE PRODUTOS
import pandas #serve para importar a base de dados

tabela = pandas.read_csv("produtos.csv") #read ler vários tipos de arquivos, como: excel, csv, mysql etc.

for linha in tabela.index: #se quisesse para colunas, seria columns e não seria index
    #PASSO 4: Cadastra produtos
    pyautogui.click(x=267, y=347)
    
    codigo = tabela.loc[linha, "codigo"] #tabela.loc = localiza a linha e a coluna da tabela

    
    
    #preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs): #se obs não for vazio, ele preenche, caso contrario nao faz. ISNA = verifica se está vazio
        pyautogui.write(str(obs))
    
        
    #para enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(500) #serve para rodar a pagina até em cima, se quiser scroll para baixo = numero negativo
    