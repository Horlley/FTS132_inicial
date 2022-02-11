import csv

import pytest

from main import somar_dois_numeros, calcular_area_circulo, calcular_area_do_paralelograma


@pytest.mark.parametrize('num01, num02, resultado_esperado',
                         [
                             (1, 2, 3),
                             (5, 7, 12),
                             (12, 44, 56),
                             (8, 9, 17)
                         ])
def testar_somar_dois_numeros(num01, num02, resultado_esperado):
    # 2 - Executar
    resultado_atual = somar_dois_numeros(num01, num02)

    # 3 - Confirmar / Check / Valida
    assert resultado_atual == resultado_esperado


# Anotação para usar como massa de teste
@pytest.mark.parametrize('raio, resultado_esperado',
                         [
                             # Valores
                             (1, 3.14),
                             (2, 12.56),
                             (3, 28.26),
                             (4, 50.24),
                             ('a', 'Falha no calculo'),
                             (' ', 'Falha no calculo'),
                         ])
def testar_calcular_area_circulo(raio, resultado_esperado):
    # raio = 1
    # resultado_esperado = 3.14
    resultado_atual = calcular_area_circulo(raio)
    assert resultado_atual == resultado_esperado


# Ler dados de um csv para usar no teste do paralelograma

def ler_dados_csv():
    dados_csv = []
    nome_arquivo = 'F:/TesteAutomacao/Iterays/TestesWEB/FTS132_inicial/test/db/dados_01.csv'
    try:
        with open(nome_arquivo, newline='') as csvfile:
            campos = csv.reader(csvfile, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo nao encontrado: {nome_arquivo}')
    except Exception as fail:
        print(f'Falha imprevista: {fail}')

@pytest.mark.parametrize('id,largura,comprimento,altura,resultado_esperado', ler_dados_csv())
def testar_calcular_area_do_paralelograma(id,largura,comprimento,altura,resultado_esperado):
    # 1 Configura
    # largura = 5
    # comprimento = 10
    # altura = 2
    # resultado_Esperado = 1
    calculo_esperado = (int(largura) * int(comprimento) * int(altura) )

    # 2 - Executa
    resultado_atual = calcular_area_do_paralelograma(int(largura), int(comprimento), int(altura))

    # 3 - Compara
    assert resultado_atual == int(resultado_esperado)

    # FTS-132 Aula - 16
