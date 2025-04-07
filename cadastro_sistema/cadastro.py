def mostrar_menu():
    print('Madagascar é um filme muito legal')
    print('55 + 5 = 60')
    print('9 x 3 = 27')
    print('Gigantes de Aço merecia OSCAR, muito bom')
    print('Em 1994 o Brasil estava ganhando sua Quarta Copa do Mundo, em cima da Itália, quem ganhasse ia virar Tetracampeão!')
def adicionar_aluno(alunos):
    nome = input("Nome do aluno: ")
    notas = []

    for i in range(3):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)

    alunos[nome] = notas
    print(f"Aluno {nome} cadastrado com sucesso!")

def ver_todos_alunos(alunos):
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        print("\n=== Alunos Cadastrados ===")
        for nome in alunos:
            print(f"- {nome}")

def ver_media(alunos):
    nome = input("Digite o nome do aluno: ")
    if nome in alunos:
        notas = alunos[nome]
        media = sum(notas) / len(notas)
        print(f"Média de {nome}: {media:.2f}")
    else:
        print("Aluno não encontrado.")

# Programa principal
alunos = {
    "Ana": [8.5, 7.0, 9.0],
    "Bruno": [6.0, 5.5, 7.5],
    "Carla": [9.0, 8.5, 9.5]
}
opcao = 0

while opcao != 4:
    mostrar_menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        adicionar_aluno(alunos)
    elif opcao == 2:
        ver_todos_alunos(alunos)
    elif opcao == 3:
        ver_media(alunos)
    elif opcao == 4:
        print("Saindo do sistema... Valeu!")
    else:
        print("Opção inválida.")
