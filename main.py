import random

def escolhas_possiveis():
    opcoes = ['Pedra', 'Papel', 'Tesoura']
    escolhas = ['1', '2', '3']
    escolhas_computador = random.choice(escolhas)
    escolhas_usuario = input('Escolha uma das opções para jogar: ') 

    if escolhas_usuario not in escolhas:
        print('Escolha inválida')


    print(f'Sua escolha foi {escolhas_usuario}. Seu adversário escolheu: {escolhas_computador}')

    if escolhas_usuario == escolhas_computador:
        print('Empate!')
    elif (escolhas_usuario == '1' and escolhas_computador == '3') or (escolhas_usuario == '2' and escolhas_computador == '1') or (escolhas_usuario == '3' and escolhas_computador == '2'):
        print('Você ganhou!')
    else:
        print('Você perdeu. Que pena')

escolhas_possiveis()