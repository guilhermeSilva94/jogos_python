import adivinhacao
import forca

def escolhe_jogo():
    print('Escolha o seu jogo:')
    print('*' * 19)

    print('(1) Forca (2) Adivinhação')
    print('')

    jogo = int(input('Qual jogo?'))

    if(jogo == 1):
        print('Jogo da Forca')
        forca.jogar()
    elif(jogo == 2):
        print('Jogo da Adivinhação')
        adivinhacao.jogar()  

if(__name__ == '__main__'):
    escolhe_jogo()