import pytest

from main import somar_dois_numeros, calcular_area_circulo


def testar_somar_dois_numeros():
# 1- Configura / Prepara
    # Dados e Valores
    # Entradas
    num1 = 8
    num2 = 9
    # Saidas
    resultado_esperado = 17

# 2 - Executar
    resultado_atual = somar_dois_numeros(num1, num2)

# 3 - Confirmar / Check / Valida
    assert resultado_atual == resultado_esperado

def testar_calcular_area_circulo():
    raio = 1
    resultado_esperado = 3.14
    resultado_atual = calcular_area_circulo(raio)
    assert resultado_atual == resultado_esperado