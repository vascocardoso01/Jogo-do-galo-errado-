# JOGO DO GALO
"""
1- definir o tabuleiro
2- definir os caracteres de jogo
3- rodar o jogo 
4- mostrar a tabela a cada jogada
5- verificar se alguém ganhou após cada jogada
"""

# Lista do jogo e Regras
tab = ['#','1','2','3','4','5','6','7','8','9']
print('BEM-VINDOS ao Jogo do Galo! Este é o vosso tabuleiro de jogo!')

# Função que define o tabuleiro
def tabuleiro():
    print(tab[7],'|', tab[8],'|',tab[9])
    print('----------')
    print(tab[4],'|',tab[5],'|', tab[6])
    print('----------')
    print(tab[1],'|',tab[2],'|',tab[3])

tabuleiro()

def verificar():
    possibilidade1 = tab[1]==tab[2]==tab[3]
    possibilidade2 = tab[4]==tab[5]==tab[6]
    possibilidade3 = tab[7]==tab[8]==tab[9]
    possibilidade4 = tab[1]==tab[4]==tab[7]
    possibilidade5 = tab[2]==tab[5]==tab[8]
    possibilidade6 = tab[3]==tab[6]==tab[9]
    possibilidade7 = tab[1]==tab[5]==tab[9]
    possibilidade8 = tab[7]==tab[5]==tab[3]
    lista_de_resultados = [possibilidade1,possibilidade2,possibilidade3,possibilidade4,possibilidade5,possibilidade6,possibilidade7,possibilidade8]
    return lista_de_resultados
verificacao = verificar()

# Função que define os caracteres utilizados em jogo
def caracteres():
    print('Em primeiro lugar, vamos definir os caracteres de jogo:')
    char_jogador1 = input('JOGADOR 1 -> Escolhe um caracter para jogares:')
    while len(char_jogador1) != 1 or char_jogador1.isdigit()==True:
        char_jogador1 = input('ERRRADO! Escolhe UM caracter para jogares:')
    else:
        print(f'O JOGADOR 1 vai jogar com o caracter {char_jogador1}')

    char_jogador2 = input('JOGADOR 2 -> Escolhe um caracter para jogares, diferente do JOGADOR 1:')
    while len(char_jogador2) != 1 or char_jogador2 == char_jogador1 or char_jogador1.isdigit()==True:
        char_jogador2 = input('ERRRADO! Escolhe UM caracter para jogares, DIFERENTE do JOGADOR1:')
    else:
        print(f'O JOGADOR 2 vai jogar com o caracter {char_jogador2}')
    return char_jogador1,char_jogador2

simbolo1, simbolo2 = caracteres()


# Função que define as jogadas -> Incompleto

jogadas_possiveis = ['1','2','3','4','5','6','7','8','9']                                                   # Neste exercício, convém ter uma lista de nºs em strings do que ints, para simplificar o código abaixo

def jogadas():
    print('Que o jogo comece! O Jogador 1 abre as hostilidades e, depois alternam por cada jogada!')
    count = 0
    while count <= 8:
        print(tabuleiro()) 
        jogada = input('Escolhe em que posição colocar o teu caracter (1-9):')
        while jogada not in jogadas_possiveis:                                                               # Simplificação, porque dos input() vem sempre uma string - anteriormente - while jogada.isdigit() != True or int(jogada) not in jogadas_possiveis: - porque tinha a lista só com ints
            jogada = input('Escolhe em que posição (disponível) colocar o teu caracter (1-9) - número:')
        if count%2 == True:
            tab[int(jogada)] = simbolo1
        else:
            tab[int(jogada)] = simbolo2

        jogadas_possiveis.remove(jogada)  
        count +=1  
        if any(verificacao):
            print('Parabéns, venceu o jogo!')
            tabuleiro()
            return
        else:
            continue
    tabuleiro()
    print('Empate! Tentem outra vez!')  
                                               

jogadas()


