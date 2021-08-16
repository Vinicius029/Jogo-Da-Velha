import os
from time import sleep
from jogador import Jogador
from pc import Maquina
from colorama.ansi import Fore, Back, Style



def tela():
    os.system('cls')
    print(f'{Style.BRIGHT}\033[1;33m    0   1   2')
    print(f'0:  {velha[0][0]} | {velha[0][1]} | {velha[0][2]}')
    print('   -----------')
    print(f'1:  {velha[1][0]} | {velha[1][1]} | {velha[1][2]}')
    print('   -----------')
    print(f'2:  {velha[2][0]} | {velha[2][1]} | {velha[2][2]}\033[m')
    print()
    print(f'Jogadas: {Fore.GREEN}{str(jogadas)}{Fore.RESET}{Style.RESET_ALL}')
    


def jogador():
    global jogadas
    global quemJoga
    global vit
    global maxJogada

    if quemJoga == 2 and jogadas <  maxJogada:
        try: 
            linha = int(input('Linha:'))
            coluna = int(input('Coluna: '))

            while velha[linha][coluna] != ' ':
                linha = int(input('Linha:'))
                coluna = int(input('Coluna: '))

            velha[linha][coluna] = 'X'
            quemJoga = 1
            jogadas += 1
        except:
            print('Linha e Coluna inválido!')

def jog():
    global jogadas
    global quemJoga
    global vit
    global maxJogada
    j = Jogador()
    j.jogador(jogadas, quemJoga, maxJogada,velha)
    quemJoga = 1
    jogadas += 1
    
    
     
def maquina1():
    global jogadas
    global quemJoga
    global vit
    global maxJogada
    m = Maquina()
    m.computador(jogadas, quemJoga, maxJogada,velha)
    quemJoga = 2
    jogadas += 1

"""def maquina():
    global jogadas
    global quemJoga
    global vit
    global maxJogada

    if quemJoga == 1 and jogadas < maxJogada:
        linha = randint(0,2)
        coluna = randint(0,2)
        while velha[linha][coluna] != ' ':
            linha = randint(0,2)
            coluna = randint(0,2)
            sleep(2)
        velha[linha][coluna] = "O"
        jogadas += 1
        quemJoga = 2"""

def verificador():
    
    global velha
    vit = 'n'
    simbolos = ['X','O']
    for s in simbolos:
        vit = 'n'
        indexL = indexC = 0
        while indexL < 3:
            soma = indexC = 0
            while indexC < 3:
                if velha[indexL][indexC] == s:
                    soma += 1
                indexC += 1
            if soma == 3:
                vit = s
                break
            indexL += 1

        if vit != 'n':
            break

        #VERIFICAÇÃO DE COLUNAS

        indexL = indexC = 0
        while indexC < 3:
            soma = indexL = 0
            while indexL < 3:
                if velha[indexL][indexC] == s:
                    soma += 1
                indexL += 1
            if soma == 3:
                vit = s
                break
            indexC += 1
        if vit  != 'n':
            break
        
        #VERIFICA DIAGONAL 1
        soma = 0
        inDia = 0
        while inDia < 3:
            if velha[inDia][inDia] == s:
                soma += 1
            inDia += 1
        if soma == 3:
            vit = s
            break

        #VERIFICA DIAGONAL 2
        soma = 0
        inDiaC = 2
        inDiaL = 0
        while inDiaC >= 0:
            if velha[inDiaL][inDiaC] == s:
                soma += 1
            inDiaL += 1
            inDiaC -= 1
        if soma == 3:
            vit = s
            break
    
    return vit


def redefinir():
    global velha
    global jogadas
    global quemJoga
    global maxJogada
    jogadas = 0
    quemJoga = 2
    maxJogada = 9
    velha = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]


jogadas = 0
quemJoga = 2
maxJogada = 9
vJogador = vComputador = 0
vit = "n"
velha = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
jogarMais = "s"
while jogarMais == 's':
    while True:
        tela()
        jog()
        maquina1()
        tela()
        vitoria = verificador()
        if (vitoria != 'n') or (jogadas >= maxJogada):
            if vitoria == 'X':
                print('Vitoria do Jogador')
                vJogador += 1
            elif vitoria == 'O':
                print('Vitoria do computador')
                vComputador +1
            else:
                print('Empate')
            break
    print(f'Placar: Jogador {vJogador} x {vComputador} Computador')
    jogarMais = str(input('Quer jogar novamente? [S/N] ')).lower()
    redefinir()





