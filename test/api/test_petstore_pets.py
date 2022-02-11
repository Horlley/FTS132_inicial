# Bibliotecas -
# Site para testes = https://petstore.swagger.io/
import time

import pytest  # Motor dos testes deve ser sempre importado
import requests  # Framework de Teste de API

# Endereço da API
base_url = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}

def testar_criar_um_pet():
    # Configurar
    status_code_esperado = 200
    nome_pet_esperado = 'Frajola'
    tag_esperado = 'vacinado'

    # Executar
    resposta = requests.post(
        url=base_url,
        data=open('F:/TesteAutomacao/Iterays/TestesWEB/FTS132_inicial/test/db/pet1.json', 'rb'),
        headers=headers
    )
    # Formatar
    print(resposta)
    print(resposta.status_code)

    corpo_da_resposta = resposta.json()

    # Verificar
    assert resposta.status_code == status_code_esperado
    assert corpo_da_resposta['name'] == nome_pet_esperado
    # assert corpo_da_resposta['tags'] == tag_esperado
