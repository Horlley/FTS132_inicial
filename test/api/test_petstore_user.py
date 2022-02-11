# Bibliotecas -
# Site para testes = https://petstore.swagger.io/
import time

import pytest  # Motor dos testes deve ser sempre importado
import requests  # Framework de Teste de API

# Endereço da API
base_url = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}
token_usuario = ''

def testar_criar_usuario():
    # Configuração
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '1000'

    # Executa
    resposta = requests.post(  # Faz a requisição
        url=base_url,
        data=open('F:/TesteAutomacao/Iterays/TestesWEB/FTS132_inicial/test/db/user1.json', 'rb'),
        headers=headers
    )

    # Formatação
    corpo_da_resposta = resposta.json()


    # Valida
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada


def testar_consultar_usuario():
# Configura
    status_code = 200
    id= 1000
    username = 'testeapi'
    firstName = 'testeapi'
    lastName = 'teste'
    email = 'teste@mail.com'
    password = '123456'
    phone = '99999999999'
    userStatus = 0

# Executa
    resposta = requests.get(
        url=f'{base_url}/{username}',
        headers=headers
    )
# Formata
    corpo_da_resposta = resposta.json()

# Compara
    assert resposta.status_code == status_code
    assert corpo_da_resposta['id'] == id
    assert corpo_da_resposta['username'] == username
    assert corpo_da_resposta['firstName'] == firstName
    assert corpo_da_resposta['lastName'] == lastName
    assert corpo_da_resposta['email'] ==  email
    assert corpo_da_resposta['password'] ==  password
    assert corpo_da_resposta['phone'] ==  phone

def testar_alterar_usuario():
    # Configura
    username = 'testeapi'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '1000'

    # Executa
    resposta = requests.put(
        url=f'{base_url}/{username}',
        data=open('F:/TesteAutomacao/Iterays/TestesWEB/FTS132_inicial/test/db/user2.json', 'rb'),
        headers=headers
    )

    # Formata
    corpo_da_resposta = resposta.json()

    # Compara
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'] == mensagem_esperada

def testar_excluir_usuario():
    # Configura
    username = 'testeapi'
    status_code_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = 'testeapi'

    # Executa
    resposta = requests.delete(
        url=f'{base_url}/{username}',
        headers=headers
    )

    # Formata
    match resposta.status_code:
        case 200:
            corpo_da_resposta = resposta.json()
            print(corpo_da_resposta)

            # compara
            assert resposta.status_code == status_code_esperado
            assert corpo_da_resposta['code'] == codigo_esperado
            assert corpo_da_resposta['type'] == tipo_esperado
            assert corpo_da_resposta['message'] == mensagem_esperada
        case 400:
            print(' Usuário fornecido incorretamente')
        case 404:
            print(' Usuário não encontrado')

def testar_login_do_usuario():
    # Configura
    username = 'testeapi'
    password = 'sucesso'
    status_codigo_esperado = 200
    codigo_esperado = 200
    tipo_esperado = 'unknown'
    inicio_mensagem_esperada = 'logged in user session:'

    # Executa
    resposta = requests.get(
        url=f'{base_url}/login?username={username}&password={password}',
        headers=headers
    )

    # Formata
    corpo_da_resposta = resposta.json()

    # Compara
    assert resposta.status_code == status_codigo_esperado
    assert corpo_da_resposta['code'] == codigo_esperado
    assert corpo_da_resposta['type'] == tipo_esperado
    assert corpo_da_resposta['message'].find(inicio_mensagem_esperada) != -1

    # Extrair texto da mensagem: logged in user session: = tamanho 23
    mensagem_recebida = corpo_da_resposta['message']
    token_usuario = mensagem_recebida[23:100]
    mensagem_completa = inicio_mensagem_esperada + token_usuario
    assert corpo_da_resposta['message'] == mensagem_completa

def testar_seguencia_de_testes():
    testar_criar_usuario()
    time.sleep(5)
    # testar_alterar_usuario()
    # time.sleep(5)
    testar_login_do_usuario()
    time.sleep(5)
    testar_consultar_usuario()
    time.sleep(5)
    testar_excluir_usuario()