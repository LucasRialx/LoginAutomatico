import requests
from bs4 import BeautifulSoup

# URL do site de login
url_login = 'https:www.exemplo.com.br'

# Dados do login
login_data = {
    'username': 'Login',  # Substitua pelo seu nome de usuário
    'password': 'Password.'     # Substitua pela sua senha
}

# Criar uma sessão para manter as cookies e informações de login
session = requests.Session()

# Fazer a requisição POST com os dados de login
response = session.post(url_login, data=login_data)

# Verificar se o login foi bem-sucedido
if response.ok:
    print('Login realizado com sucesso!')

    # Acessar uma página protegida após o login
    url_protected = 'https:www.exemplo.com.br/page2'
    response_protected = session.get(url_protected)

    # Verificar se o acesso foi bem-sucedido
    if response_protected.ok:
        print('Página protegida acessada com sucesso!')
        soup = BeautifulSoup(response_protected.text, 'html.parser')
        
        # Exemplo: Exibir o título da página
        print(soup.title.text)
    else:
        print('Falha ao acessar a página protegida.')
else:
    print('Falha ao realizar login.')
