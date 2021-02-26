#bibliotecas
import random
from datetime import date
#variaveis
con = bin = 0
data = date.today().year
#layout

print("_________  _________     ___________________ _______   ")
print("\_   ___ \ \_   ___ \   /  _____/\_   _____/ \       \  ")
print("/    \  \/ /    \  \/  /   \  ___ |    __)_  /   |    \ ")
print("\     \___ \     \____ \    \_\  \|        \/    |     \ ")
print(" \______  / \______  /  \______  /_______  /\____|__   / ")
print("        \/         \/          \/        \/         \ / ")
print("          by     Channel: JhinStroke   ")
print("")
print("Sistema de Login...")

login = int (input ("- Digite a Senha: "))
verifica = False

if login == 666:
 print("[+] CCGENERATORV2 PRIVATE [-] ")

print(" ---------- Cartões ---------- ")
print("- Classic [ 1 ] ")
print("- Platinum [ 2 ] ")
print("- Black [ 3 ]")
print("- Infinity International [ 4 ]")
print("- Sair [ 0 ] ")
print(" ------------------------------ ")
print("")

cartao =int (input ("Qual Tipo de Cartão Você Quer Gerar ? "))
cvv = random.randrange(100, 999)
mes = random.randint(1, 12)
ano = data + random.randint(1, 7)
cc = random.randrange(1, 9999999999)
cpf = random.randrange(1, 999999999)
digito = random.randrange(1, 99)
idade = random.randrange(20, 100)
cep = random.randrange(11111, 99999)
cepi = random.randrange(111, 999)

if cartao == 1:
    bin = 472955
    con += 1
    print('-' * 49)
    print('')
    print(' [!] - CC Classic GERADO #{} - [!]'.format(con))
    print('')
    print(' [!] Cartão: {}{} [!]'.format(bin, cc))
    print(' [!] Cvv: {} [!]'.format(cvv))
    print(' [!] Validade: {}/{} [!]'.format(mes, ano))
    print(' - Cpf: {}-{}'.format(cpf, digito))
    print(' - Idade: {}'.format(idade))
    print(' - Cep: {}-{}'.format(cep, cepi))
    print(' [!] Formatado: {}{}|{}|{}|{} [!]'.format(bin, cc, mes, ano, cvv))
    print(' - Checker - https://www.mrchecker.net/card/ccn2/')
    print('-' * 49)
print("")

if cartao == 2:
    bin = 48062909
    con += 1
    print('-' * 49)
    print('')
    print(' [!] - CC Platinum GERADO #{} - [!]'.format(con))
    print('')
    print(' - Cartão: {}{} [!]'.format(bin, cc))
    print(' - Cvv: {} [!]'.format(cvv))
    print(' - Validade: {}/{} [!]'.format(mes, ano))
    print(' - Cpf: {}-{}'.format(cpf, digito))
    print(' - Idade: {}'.format(idade))
    print(' - Cep: {}-{}'.format(cep, cepi))
    print(' [!] Formatado: {}{}|{}|{}|{} [!]'.format(bin, cc, mes, ano, cvv))
    print(' - Checker - https://www.mrchecker.net/card/ccn2/')
    print('-' * 49)

if cartao == 3:
    bin = 229239
    con += 1
    print('-' * 49)
    print('')
    print(' [!] - CC Black GERADO #{} - [!]'.format(con))
    print('')
    print(' - Cartão: {}{} [!]'.format(bin, cc))
    print(' - Cvv: {} [!]'.format(cvv))
    print(' - Validade: {}/{} [!]'.format(mes, ano))
    print(' - Cpf: {}-{}'.format(cpf, digito))
    print(' - Idade: {}'.format(idade))
    print(' - Cep: {}-{}'.format(cep, cepi))
    print(' [!] Formatado: {}{}|{}|{}|{} [!]'.format(bin, cc, mes, ano, cvv))
    print(' - Checker - https://www.mrchecker.net/card/ccn2/')
    print('-' * 49)

if cartao == 4:
    bin = 411184
    con += 1
    print('-' * 49)
    print('')
    print(' [!] - CC Infinity GERADO #{} - [!]'.format(con))
    print('')
    print(' - Cartão: {}{} [!]'.format(bin, cc))
    print(' - Cvv: {} [!]'.format(cvv))
    print(' - Validade: {}/{} [!]'.format(mes, ano))
    print(' - Cpf: {}-{}'.format(cpf, digito))
    print(' - Idade: {}'.format(idade))
    print(' - Cep: {}-{}'.format(cep, cepi))
    print(' [!] Formatado: {}{}|{}|{}|{} [!]'.format(bin, cc, mes, ano, cvv))
    print(' - Checker - https://www.mrchecker.net/card/ccn2/')
    print('-' * 49)
