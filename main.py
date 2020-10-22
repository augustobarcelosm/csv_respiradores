#   O programa faz uma varredura no arquivo do governo federal sobre a distribuição dos respiradores
# e pelo input você pode pesquisar o nome do estado e retornará a quantidade total que cada estado
# recebeu de respiradores


import csv


def estado(state):
    re = 0
    with open('distribuicao_respiradores.csv', encoding='utf8') as arq:
        resp = csv.reader(arq, delimiter=';') # trocar o padrão de ',' do csv por ';'
        next(resp)  # skipa o cabeçalho
        for linha in resp:
            if linha[2].lower().strip() == state:
                re += int(linha[5])
    return f'Numero total de respirador para o {state}: {re}'


if __name__ == '__main__':

    with open('distribuicao_respiradores.csv', encoding='utf8') as q:

        leitura = csv.reader(q, delimiter=';')

        destino = set([i[2].lower().strip() for i in leitura])

        e = input('Digite o estado')
        print(destino)

        if e in destino:
            print(estado(e))
        else:
            pass
#       codigo para reinicar o programa caso digite um estado errado















