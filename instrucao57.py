# Criando/escrevendo arquivos no python

file = open('aula57/abcd.txt', 'w+')
file.write('Linha 1\n')
file.write('\t Linha 2\n')
file.write('\t\t Linha 3\n')

file.seek(0, 0)
print('Lendo... ')
print(file.read())
#
print(f'----------------------')
file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
#
print(f'----------------------')
file.seek(0, 0)
print(file.readlines())
#
print(f'----------------------')
file.seek(0, 0)
for linha in file.readlines():
    print(linha, end='Hahahahaha')
#
file.close()
