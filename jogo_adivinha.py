from random import randint
from time import sleep

computador = randint(0, 10)
print('<>' * 27)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar!')
print('<>' * 27)

jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)

if jogador == computador:
    print('PARABÉNS!! Você me venceu!')
else:
    print(f'GANHEI!! Eu pensei no número {computador} e não no {jogador}!')