#import
import pytest
import csv

import requests
from requests import HTTPError

jogadores_flamengo = [
    (1, 'Diego', 'Alves', 'goleiro', 'titular', '1'),
    (2, 'Isla', 'Chileno','lateral direito', 'reserva', '2'),
    (3, 'Felipe', 'Luis','lateral esquerdo', 'titular', '16'),
    (4, 'Matheus', 'Flamenguista','lateral direito', 'titular', '2')
]


def ler_csv():
    teste_dados_csv = []
    arquivo_csv = 'jogadores.csv'
    try:
        with open(arquivo_csv, newline='') as csvfile:
            dados = csv.reader(csvfile, delimiter=',')
            next(dados)
            for linha in dados:
                teste_dados_csv.append(linha)
        return teste_dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {arquivo_csv}')
    except Exception as fail:
        print(f'Falha imprevista: {fail}')



@pytest.mark.parametrize('id,nome,sobrenome,posicao,status,num_camisa', jogadores_flamengo)
def testar_dados_jogadores_flamengo(id,nome,sobrenome,posicao,status,num_camisa):
    try:
        id_obtido = ler_csv(id)
        nome_obtido = ler_csv(nome)
        sobrenome_obtido = ler_csv(sobrenome)

        print(f'id: {id_obtido} \n nome: {nome_obtido} \n sobrenome: {sobrenome_obtido}')
        print(f'id: {id_obtido} - nome: {nome_obtido} - sobrenome: {sobrenome_obtido}')
        print('id:{} \n nome:{} \n sobrenome:{}'.format(id_obtido, nome_obtido, sobrenome_obtido))

        assert id_obtido == int(id)
        assert nome_obtido == nome
        assert sobrenome_obtido == sobrenome

    except HTTPError as http_fail:  # Para o ISTQB, descobriu rodando é falha
        print(f'Um erro de HTTP aconteceu: {http_fail}')
    except Exception as fail:  # Qualquer exceção será tratada a seguir
        print(f'Falha inesperada: {fail}')