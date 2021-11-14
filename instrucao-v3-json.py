# Para ler o {}arquivo.json
import json
#
with open('aula57/abc.json', 'r') as file:
    #
    lerJson = file.read()
    # print(f'\n\n lerJson = file.read(): \n {lerJson}')
    #
    lerJson = json.loads(lerJson)  # Converte em dicionário.
    # print(f'\n\n lerJson = file.read(): \n {lerJson}')
    for ky, vl in lerJson.items():
        print(ky, vl)
    print(f'\n')
    for ky, vl in lerJson.items():
        print(f'\n {ky}')
        for k2, v2 in vl.items():
            print(f'\t {k2}: {v2}')
