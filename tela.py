import os
from colorama.ansi import Fore, Style


class Tela():

    def tela(self, velha, jogadas):
        """TELA DO JOGO DA VELHA"""
        os.system('cls')
        print(f'{Style.BRIGHT}\033[1;33m    0   1   2')
        print(f'0:  {velha[0][0]} | {velha[0][1]} | {velha[0][2]}')
        print('   -----------')
        print(f'1:  {velha[1][0]} | {velha[1][1]} | {velha[1][2]}')
        print('   -----------')
        print(f'2:  {velha[2][0]} | {velha[2][1]} | {velha[2][2]}\033[m')
        print()
        print(f'Jogadas: {Fore.GREEN}{str(jogadas)}{Fore.RESET}{Style.RESET_ALL}')


