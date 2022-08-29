import numpy as np

lista = ['pedra', 'papel', 'tesoura']

result = np.random.choice(lista, 1)

print('')
print('##################        Escolha:                       ##################')
print('##################        pedra, papel ou tesoura        ##################')
print('')

escolha = str(input('Escolha do jogador: '))
print('')

print('O computador escolheu: ', result)

print('')

if escolha == result:
    print('##################        Empate!             ##################')
if escolha == 'pedra' and result == 'tesoura':
    print('##################        Você Ganhou!        ##################')
if escolha == 'papel' and result == 'pedra':
    print('##################        Você Ganhou!        ##################')
if escolha == 'tesoura' and result == 'papel':
    print('##################        Você Ganhou!        ##################')
if escolha == 'pedra' and result == 'papel':
    print('##################        Você Perdeu!        ##################')
if escolha == 'papel' and result == 'tesoura':
    print('##################        Você Perdeu!        ##################')
if escolha == 'tesoura' and result == 'pedra':
    print('##################        Você Perdeu!        ##################')