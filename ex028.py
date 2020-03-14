import random
from time import sleep
n = random.randint(0, 5) #Computador 'pensa ' em um numero
print('-=-'*30)
print('Vou pensar em um numero entre 0 a 5, tente adivinhar...')
print('-=-'*30)
r = int(input('Em que número eu pensei?')) #jogador tenta adivinhar
print(f'PROCESSANDO...')
sleep(2) #deixa o computador 'dormindo' por 2s
if n==r:
    print(f'Parabens!!Você acertou, o numero que eu pensei realmente foi o {n}')#se jogador acertar segue essa linha

else: #se não acertar segue essa
    print(f'Você errou :c .O numero que eu pensei não foi o {r}, foi o {n}! xD')
print('Foi muito divertido jogar com você!')
