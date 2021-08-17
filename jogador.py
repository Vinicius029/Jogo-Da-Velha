class Jogador():
    
    def jogador(self, jogadas, quemJoga, maxJogada, velha):
        """FUNÇÃO DO JOGADOR"""
        if quemJoga == 2 and jogadas <  maxJogada:
            try: 
                linha = int(input('Linha:'))
                coluna = int(input('Coluna: '))

                while velha[linha][coluna] != ' ':
                    linha = int(input('Linha:'))
                    coluna = int(input('Coluna: '))

                velha[linha][coluna] = 'X'
            except:
                print('Linha e Coluna inválido!')