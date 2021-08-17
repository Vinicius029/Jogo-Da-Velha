import os
from tela import Tela
from jogador import Jogador
from pc import Maquina
from verificador import Verificador


def tela():
    t = Tela()
    t.tela(velha, jogadas)
    

def jogador():
    global jogadas, quemJoga, vit, maxJogada
    j = Jogador()
    j.jogador(jogadas, quemJoga, maxJogada,velha)
    quemJoga = 1
    jogadas += 1
    
    
def maquina():
    global jogadas, quemJoga, vit, maxJogada
    m = Maquina()
    m.computador(jogadas, quemJoga, maxJogada,velha)
    quemJoga = 2
    jogadas += 1


def verificarVencedor():
    global velha
    v = Verificador()
    vitoria = v.verificador(velha)
    return vitoria


def redefinirJogo():
    global jogadas, quemJoga, maxJogada, velha
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
        jogador()
        maquina()
        tela()
        vitoria = verificarVencedor()
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
    redefinirJogo()


os.system('cls')
print('-----FIM DE JOGO-----')
 # 184 linhas



