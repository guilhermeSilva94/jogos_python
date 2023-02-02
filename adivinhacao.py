from random import randrange

print('Bem vindo no jogo de Adivinhação!')
print('*' * 33)

total_tentativas = 0
numero_secreto = round(randrange(1, 101))
pontos = 1000

print('Qual o nível de dificuldade?')
print('(1) Fácil (2) Médio (3) Dificil')
nivel = int(input())

if (nivel == 1):
    total_tentativas = 20
elif (nivel == 2):
    total_tentativas = 10
else:
    total_tentativas = 5

#contador_tentativas = 1

#while(contador_tentativas < total_tentativas + 1):
for contador_tentativas in range(1, total_tentativas + 1):
    
    print('Tentativa {} de {}' .format(contador_tentativas, total_tentativas))
    print('*' * 16)

    chute = int(input('Digite um número entre 1 e 100: '))

    if (chute < 1 or chute > 100):
        print('Digite um número entre 1 e 100!')
        print('')
        continue

    acertou = numero_secreto == chute
    chute_maior = numero_secreto > chute
    chute_menor = numero_secreto < chute

    if(acertou):
        print('Você acertou!! Sua pontuação é {}' .format(pontos))
        break
    elif(chute_menor):
        print('Você errou! O número secreto é menor')
        print('')
    elif(chute_maior):
        print('Você errou! o número secreto é maior')
        print('')

    pontos_perdidos = abs(numero_secreto - chute)
    pontos = pontos - pontos_perdidos

    contador_tentativas = contador_tentativas + 1

    if(contador_tentativas == total_tentativas + 1):
        print('Suas tentativas acabaram! O número secreto é {}' .format(numero_secreto))
        
print('Fim de jogo')