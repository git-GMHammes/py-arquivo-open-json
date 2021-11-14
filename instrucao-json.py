import json
#
d1 = {
    'Cliente 1': {
        'nome': 'Luiz',
        'idade': '25'
    },
    'Cliente 3': {
        'nome': 'Diego',
        'idade': '45'
    },
    'Cliente 4': {
        'nome': 'Amanda',
        'idade': '24'
    },
    'Cliente 2': {
        'nome': 'Gustavo',
        'idade': '35'
    }
}
#print(f'\n\n d1 = {d1}\n\n')
dicJson = json.dumps(d1, indent=True)
# print(f'\n\n dicJson: \n {dicJson}\n\n')
with open('aula57/abc.json', 'w+') as file:
    file.write(dicJson)
