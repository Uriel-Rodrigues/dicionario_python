'''93: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um
dicionário, incluindo o total de gols feitos durante o campeonato.'''

cont= 0
aproveitamento = dict()
lista = list()

aproveitamento['jogador'] = str(input('nome do jogador: ')).strip()
aproveitamento['N° partidas'] = int(input('numero de partidas: '))

for p in range(aproveitamento['N° partidas']):
    aproveitamento[f'partida {p+1}'] = int(input(f'numero de arremessos na {p+1}° partida: '))
    cont = aproveitamento[f'partida {p+1}'] + cont
aproveitamento['total'] = cont

lista.append(aproveitamento.copy())

print('-='*20)
print(f'{"APROVEITAMENTO":^34}')
print('-='*20)

print(f'- NOME: {lista[0]["jogador"]}')
print(f'- N° PARTIDAS: {lista[0]["N° partidas"]}')

for i in range(aproveitamento['N° partidas']):
    print(f'    - PARTIDA {i+1}: {lista[0][f"partida {i+1}"]}')

print(f'- ARREMESSOS: {lista[0]["total"]}')
