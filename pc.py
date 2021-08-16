from random import randint
from time import sleep


class Maquina():

    def computador(self, jogadas, quemJoga, maxJogada,velha):
        if quemJoga == 1 and jogadas < maxJogada:
            linha = randint(0,2)
            coluna = randint(0,2)
            while velha[linha][coluna] != ' ':
                linha = randint(0,2)
                coluna = randint(0,2)
            velha[linha][coluna] = "O"
          
           