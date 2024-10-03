import pyautogui as bot
import pygetwindow as gw
import os
bot.PAUSE=2
def abrir_login(): #função para abrir o login do site da prefeitura
    bot.hotkey('alt', 'tab')
    bot.click(x=1101, y=243)
    bot.moveTo(x=1102, y=302)
    bot.click(x=1102, y=302)
    bot.sleep(2)
    bot.press('tab', presses=8)
    bot.press('enter')
    bot.press('tab', presses=8)        
    bot.press('enter')
    bot.click(x=1483, y=429)  

def get_field_positions(): #função que pega as posições dos campos CNPJ, CPF e SENHA
    bot.sleep(5)
    locate_cnpj=bot.locateCenterOnScreen('cnpj.png')
    locate_cpf=bot.locateCenterOnScreen('cpf.png')
    locate_senha=bot.locateCenterOnScreen('senha.png')

    context={'cnpj': locate_cnpj, #colocando as posições em um dicionário para acessar uma por uma depois
            'cpf':locate_cpf, 
            'senha':locate_senha}
    
    return context

def click_field(position):
    bot.click(position)

#positions=get_field_positions()   #pegando o dicionário de posições
#click_field(positions['cnpj'])  #clicando na posição do cnpj pela da chave 'cnpj' do dicionário que retorna a posiçao do campo
#click_field(positions['cpf'])   #clicando na posição do cnpj pela da chave 'cpf' do dicionário que retorna a posiçao do campo do npj
#click_field(positions['senha']) #clicando na posição do cnpj pela da chave 'senha' do dicionário que retorna a posiçao do campo


#falta fazer a parte de abrir o txt, pegar as informações de cnpj, colar no cnpj, depois cpf e senha e assim, fazer o login de cada empresa

