#SSSSAssistente pessoal sem voz ou reconhecimento de voz feita por Vodrick a 20/12/2020

#Perguntar estado

print('Olá tudo bem? ')
a=input()

if a.lower() in ['sim','claro']:
    print('Ainda bem que voce está bem!!!')

else:
    print('O que aconteceu? ')
    input()
    print('De qualquer forma espero que fique tudo bem!!:D')

#Pausa

input('Pressione ENTER para continuar')

#Apresentação

print('Ainda não apresentei-me...chamo-me VodrickBot...deve ser familiar para ti XD')
input('Pressione ENTER para continuar')
print('O nome do meu criador é Vodrick...logo eu sou um bot criado por ele...ok...admito...')

#Pausa na apresentação

input('Pressione ENTER para continuar')
print('A piada foi muito má ahhaha!!')
print('Mas tudo bem...')

#Pausa

input('Pressione ENTER para continuar')

#Nome

print('Já agora...')
b=str(input('Qual é o teu nome? '))
print(f'Belo nome, {b.capitalize()}.')
print('Se estás a ler isto é porque provavelmente ele amostrou-te o "meu" projeto..')

#Pausa

input('Pressione ENTER para continuar')

#Idade

print('Ele não me falou nada sobre ti...já agora mais uma vez')
c=int(input('Quantos anos tens? '))

if c==17 :
    print(f'What???Tens {c} anos? Incrivel tens a mesma idade que eu!!!')
elif c<17 :
    print('És mais novo que eu...eu tenho 17 anos.')
else:
    print('És mais velho que eu!! Tenho apenas 17.')

#Pausa

input('Pressione ENTER para continuar')

#Localização

print('Qual destrito de Portugal moras?')
d=str(input())

if d.capitalize()=='Porto':
    print(f'Moras no destrito do {d.capitalize()}??Incrivel!! Eu moro ai...na verdade fui criado ai!!')
elif d.capitalize() in ['Lisboa', 'Porto', 'Braga', 'Setúbal', 'Aveiro', 'Faro', 'Leiria', 'Coimbra', 'Santarém', 'Viseu', 'Madeira', 'Açores', 'Vila Real',  'Castelo Branco', 'Évora', 'Guarda', 'Beja', 'Bragança', 'Portalegre']:
    print(f'Hum moras no destrito de/do {d.capitalize()}...pelos vistos moramos no mesmo país!!')
else:
    print(f'Não sei onde fica {d}.')

#Pausa
input('Pressione ENTER para continuar')

#Despedida

print(f'De qualquer jeito gostei de falar contigo, {b.capitalize()}!!!')
print('Vemo-nos por ai.....adeuus!!!:D')

#FIM





    
