import pyautogui as bot
import pygetwindow as gw
import os
bot.PAUSE=1
def abrir_login(): #função para abrir o login do site da prefeitura
    bot.hotkey('alt', 'tab')
    bot.click(x=1101, y=243)
    bot.moveTo(x=1102, y=302)
    bot.click(x=1102, y=302)
    bot.sleep(5)
    bot.press('tab', presses=8)
    bot.press('enter')
    bot.press('tab', presses=8)        
    bot.press('enter')
    bot.click(x=1483, y=429)  

def get_field_positions(): #função que pega as posições dos campos CNPJ, CPF e SENHA
    locate_cnpj=bot.locateCenterOnScreen('cnpj.png')
    locate_cpf=bot.locateCenterOnScreen('cpf.png')
    locate_senha=bot.locateCenterOnScreen('senha.png')
    locate_entrar=bot.locateCenterOnScreen('entrar.png')
    context={'cnpj': locate_cnpj, #colocando as posições em um dicionário para acessar uma por uma depois
            'cpf':locate_cpf, 
            'senha':locate_senha,
            'entrar':locate_entrar}
    
    return context

def click_field(position):
    bot.click(position)

def fill_login(cnpj, cpf, senha):
    bot.sleep(1)
    positions=get_field_positions()   #pegando o dicionário de posições
    click_field(positions['cnpj'])  #clicando na posição do cnpj pela da chave 'cnpj' do dicionário que retorna a posiçao do campo
    bot.write(cnpj)
    bot.click(x=1483, y=429)
    click_field(positions['cpf'])
    bot.write(cpf)
    bot.click(x=1483, y=429)   #clicando na posição do cnpj pela da chave 'cpf' do dicionário que retorna a posiçao do campo do npj
    click_field(positions['senha'])
    bot.write(senha)
    bot.click(x=1483, y=429) #clicando na posição do cnpj pela da chave 'senha' do dicionário que retorna a posiçao do campo
    click_field(positions['entrar']) #clicando no botão de entrar

def get_infos(arquivo):
    credenciais = []  # Lista para armazenar as credenciais
    with open(arquivo, 'r') as db:
        for linhas in db:
            linhas = linhas.strip()  # Remove espaços em branco
            partes = linhas.split(', ')
            if len(partes) == 3:
                credenciais.append(partes)  # Adiciona as 3 informaçoes na lista
    return credenciais
bot.sleep(1)
abrir_login()
credenciais = get_infos('teste-db.txt')
for cnpj, cpf, senha in credenciais:
    fill_login(cnpj, cpf, senha)

#falta fazer a parte de abrir o txt, pegar as informações de cnpj, colar no cnpj, depois cpf e senha e assim, fazer o login de cada empresa

