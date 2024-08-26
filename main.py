import re 
import sys
entrada = input('CPF: ')
cpf_usuario = re.sub(r'[^0-9]','', entrada)
entrada_sequencial = entrada == entrada[0] * len(entrada)
if entrada_sequencial:
    print('Você enviou dados sequenciais')
    sys.exit()
noves_digitos = cpf_usuario[:9]
contador_regressivo1 = 10
resultado_digito = 0
for digito1 in noves_digitos:
    resultado_digito += int(digito1) * contador_regressivo1
    contador_regressivo1 -= 1
digito1 = (resultado_digito * 10) % 11
digito1 = digito1 if digito1 <=9 else 0

noves_digitos = cpf_usuario[:10]
contador_regressivo2 = 11
resultado_digito2 = 0
for digito2 in noves_digitos:
    resultado_digito2 += int(digito2)* contador_regressivo2
    contador_regressivo2 -= 1
digito2 = (resultado_digito2 * 10) % 11
digito2 = digito2 if digito2 <= 9 else 0
primeiro_numero = cpf_usuario[-2]
segundo_numero = cpf_usuario[-1]
primeiro_numero_int = int(primeiro_numero)
segundo_numero_int = int(segundo_numero)
if digito1 == primeiro_numero_int:
    if digito2 == segundo_numero_int:
        print('CPF VALIDO')
    else:
        print('CPF INVALIDO')
else:
    print('CPF INVALIDO')

sair = input('Digite qualquer coisa para sair.')