import pyautogui as bot
bot.PAUSE=1.5
def abrir_login(): #função para abrir o login do site da prefeitura
    bot.hotkey('alt', 'tab')
    cidadao = bot.locateCenterOnScreen('botoes/cidadao.png')
    bot.click(cidadao)
    y_offset=50
    bot.moveTo(cidadao.x, cidadao.y+y_offset)                               
    bot.click()
    bot.click(bot.locateCenterOnScreen('botoes/nfs.png'))
    bot.click(bot.locateCenterOnScreen('botoes/nfs2.png'))
    bot.click(x=989, y=922)

def get_field_positions(): #função que pega as posições dos campos CNPJ, CPF e SENHA
    locate_cnpj=bot.locateCenterOnScreen('botoes/cnpj.png')
    locate_cpf=bot.locateCenterOnScreen('botoes/cpf.png')
    locate_senha=bot.locateCenterOnScreen('botoes/senha.png')
    locate_entrar=bot.locateCenterOnScreen('botoes/entrar.png')
    context={'cnpj': locate_cnpj, #colocando as posições em um dicionário para acessar uma por uma depois
            'cpf':locate_cpf, 
            'senha':locate_senha,
            'entrar':locate_entrar}
    
    return context

def click_field(position):
    bot.click(position)

def fill_login(cnpj, cpf, senha):
    positions=get_field_positions()   #pegando o dicionário de posições
    click_field(positions['cnpj'])  #clicando na posição do cnpj pela da chave 'cnpj' do dicionário que retorna a posiçao do campo
    bot.write(cnpj)
    click_field(positions['cpf'])#clicando na posição do cnpj pela da chave 'cpf' do dicionário que retorna a posiçao do campo do npj
    bot.write(cpf)
    click_field(positions['senha'])#clicando na posição do cnpj pela da chave 'senha' do dicionário que retorna a posiçao do campo
    bot.write(senha) 
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

def get_relatorios():
    bot.click(bot.locateCenterOnScreen('botoes/relatorio.png'))
    bot.click(bot.locateCenterOnScreen('botoes/date.png'))
    bot.click(bot.locateCenterOnScreen('botoes/back.png'))
    bot.click(bot.locateCenterOnScreen('botoes/day1.png'))
    bot.click(bot.locateCenterOnScreen('botoes/date.png'))
    bot.click(bot.locateCenterOnScreen('botoes/back.png'))
    bot.click(bot.locateCenterOnScreen('botoes/day30.png'))

bot.sleep(1)
#credenciais = get_infos('teste-db.txt')#falta fazer a parte de abrir o txt, pegar as informações de cnpj, colar no cnpj, depois cpf e senha e assim, fazer o login de cada empresa
#for cnpj, cpf, senha in credenciais:
    #fill_login(cnpj, cpf, senha)
    #bot.sleep(5)
get_relatorios()


