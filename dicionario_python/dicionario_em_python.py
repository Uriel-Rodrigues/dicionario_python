'''90-Faça um programa que leia nome e média de um aluno, guardando também a situação em um
dicionário. No final, mostre o conteúdo da estrutura na tela.'''

alunos = dict()

alunos['nome'] = str(input('digite o nome do aluno: '))
alunos['media'] = float(input('digite a media do aluno: '))
if alunos['media']>= 7.0:
    alunos['situação'] = 'Aprovado'
elif 5<= alunos['media'] <7:
    alunos['situação']= 'Recuperação'
else:
    alunos['situação'] = 'Reprovado'

print('-*'*30)
print(f'{"NOME":<10}{"MEDIA":<10}{"SITUAÇÃO":<10}')
print('-*'*30)
for i in alunos.values():
    print(f'{i:<10}',end='')

