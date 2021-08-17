from random import randint


class Maquina():

    def computador(self, jogadas, quemJoga, maxJogada,velha):
        """FUNÇÃO DO COMPUTADOR"""
        if quemJoga == 1 and jogadas < maxJogada:
            linha = randint(0,2)
            coluna = randint(0,2)
            while velha[linha][coluna] != ' ':
                linha = randint(0,2)
                coluna = randint(0,2)
            velha[linha][coluna] = "O"
          
           