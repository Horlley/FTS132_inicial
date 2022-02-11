import  pytest

def print_hi(name):
    print(f'Oi, {name}')

def somar_dois_numeros(num1, num2):
    return num1 + num2

def subtrair_dois_numeros(num1, num2):
    return num1 - num2

def multiplica_dois_numeros(num1, num2):
    return num1 * num2

def divisao_dois_numeros(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 'Não é possivel dividir por zero'

def elevar_um_numero_pelo_outro(num1, num2):
    return num1 ** num2

def calcular_area_quadrado(num1):
    return num1 * num1

def calcular_area_circulo(raio):
    try:
        return 3.14 * raio ** 2
    except TypeError:
        return 'Falha no calculo'

def calcular_area_do_paralelograma(largura, comprimento, altura):
    return largura * comprimento * altura

if __name__ == '__main__':
    soma = somar_dois_numeros(5, 7)
    print(f'A soma dos números é: {soma}')

    subtracao = subtrair_dois_numeros(5, 7)
    print(f'O valor da subtração é: {subtracao}')

    multiplicacao = multiplica_dois_numeros(10, 5)
    print(f'O valor da multiplicação e: {multiplicacao}')

    divisao = divisao_dois_numeros(50, 5)
    print(f'O valor da divisão é: {divisao}')

    # elevar = elevar_um_numero_pelo_outro(2, 3)
    # print(f'O valor da potencia é: {elevar}')
    #
    # quadrado = calcular_area_quadrado(5)
    # print(f'O quadrado é: {quadrado}')
    #
    # raio = calcular_are_circulo(5)
    # print(f'O raio é: {raio}')

# Testes
'''
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
    
'''
