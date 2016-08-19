n1 = float(input('digite um numero: '))
equacao = input('digite a equação: ')
n2 = float(input('digite outro numero: '))
subtracao = (n1 - n2)
divisao = (n1 / n2)
multiplicacao = (n1 * n2)
adicao = (n1 + n2)
if equacao == '-':
    print(subtracao)
if equacao == '/':
    print(divisao)
if equacao == '*':
    print(multiplicacao)
if equacao == '+':
    print(adicao)