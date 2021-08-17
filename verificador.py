class Verificador():

    def verificador(self, velha):
        """VERIFICAÇÃO DE LINHAS, COLUNAS E DIAGONAIS, PARA VERIFICAR SE TEVE VENCEDOR"""
        vit = 'n'
        simbolos = ['X','O']
        for s in simbolos:
            vit = 'n'
            indexL = indexC = 0
            
            #VERIFICAÇÃO DE LINHAS
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