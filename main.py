import math
from prettytable import PrettyTable

def calcula_nota_atividade(atividades_entregues, total_atividades=25):
    return min(10, (atividades_entregues / total_atividades) * 10)

def calcula_media_final(nota_atividade, nota_prova, nota_trabalho):
    media = (nota_atividade + nota_prova + nota_trabalho) / 3
    return math.ceil(media)

def main():
    alunos = []

    while True:
        nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break

        try:
            atividades_entregues = int(input("Quantas atividades o aluno entregou (de 25)? "))
            nota_prova = float(input("Nota da prova (0-10): "))
            nota_trabalho = float(input("Nota do trabalho (0-10): "))
        except ValueError:
            print("Por favor, insira valores numéricos válidos.")
            continue

        nota_atividade = calcula_nota_atividade(atividades_entregues)
        media_final = calcula_media_final(nota_atividade, nota_prova, nota_trabalho)

        aluno = {
            'nome': nome,
            'nota_atividade': nota_atividade,
            'nota_prova': nota_prova,
            'nota_trabalho': nota_trabalho,
            'media_final': media_final
        }
        alunos.append(aluno)

    # Exibir os resultados em uma tabela ASCII
    tabela = PrettyTable()
    tabela.field_names = ["Nome do Aluno", "Nota de Atividade", "Nota da Prova", "Nota do Trabalho", "Média Final"]

    for aluno in alunos:
        tabela.add_row([aluno['nome'], aluno['nota_atividade'], aluno['nota_prova'], aluno['nota_trabalho'], aluno['media_final']])

    print(tabela)

if __name__ == "__main__":
    main()