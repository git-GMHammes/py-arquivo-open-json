# Criando/escrevendo arquivos no python
# Manipulação de arquivos
# A função chave para trabalhar com arquivos em Python é a função.open()
# A função tem dois parâmetros; nome de arquivo, e modo.open()
# Existem quatro métodos diferentes (modos) para abrir um arquivo:
# "r" - Leia - Valor padrão. Abre um arquivo para leitura, erro se o arquivo não existir
# "a" - Apêndice - Abre um arquivo para appending, cria o arquivo se ele não existir
# "w" - Escrever - Abre um arquivo para escrever, cria o arquivo se ele não existir
# "x" - Criar - Criar o arquivo especificado, devolve um erro se o arquivo existir
# Além disso, você pode especificar se o arquivo deve ser tratado como binário ou modo de texto
# "t" - Texto - Valor padrão. Modo texto
# "b" - Binário - Modo binário (por exemplo, imagens)
try:
    file = open('aula57/abcd.txt', 'w+')
    file.write('Linha \n')
    file.write('----- \n')
    file.write('Linha \n')
    file.seek(0, 0)
    print(f'\n\n{file.read()}')
finally:
    file.close()
