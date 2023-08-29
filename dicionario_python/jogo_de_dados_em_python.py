'''91-Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em
ordem, sabendo que o vencedor tirou o maior número no dado.'''

import random,time
from operator import itemgetter
jogadores = dict()
dados = list()
for c in range (1,5):
    jogadores['jogador'] = str(input('digitar nome do jogador: ')).strip().upper()
    jogadores['numero'] = random.randint(1,6)
    #time.sleep(1)
    print('dado rolado')
    dados.append(jogadores.copy())
print('-*'*15)
print(f'{"RESULTADOS":^30}')
print('-*'*15)
for i, e in enumerate(dados):
    print(f'{i} JOGADOR -> {e["jogador"]:<10} NUMERO -> { e ["numero"]}')

dados = sorted(dados, key=itemgetter('numero'),reverse=True)

print('----------- PLACAR -----------')
for i, v in enumerate(dados):
    print(f'{i} lugar:{v["jogador"]:<10} com {v["numero"]}')
