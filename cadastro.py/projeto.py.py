alunos = []
def adicionar():
    nome = input("Digite o nome do aluno: ").strip().title()
    idade = int(input("Digite a idade do aluno: "))
    while True:
            nota = float(input("Digite a nota do aluno: "))
            if 0 <= nota <= 10:
                break
            else:
                print("Nota inválida. Digite um valor entre 0 e 10.")
    dados = {"nome": nome,
             "idade": idade,
             "nota": nota}
    alunos.append(dados)
def listar():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return
    for aluno in alunos:
        print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Nota: {aluno['nota']}\n{'='*30}")
def buscar():
    nome_busca = input("Digite o nome do aluno que deseja buscar: ").strip().title()
    encontrados = [aluno for aluno in alunos if aluno['nome'] == nome_busca]
    if encontrados:
        for aluno in encontrados:
            print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Nota: {aluno['nota']}\n{'='*30}")
    else:
        print("Aluno não encontrado.")
def remover():
    nome_remover = input("Digite o nome do aluno que deseja remover: ").strip().title()
    for aluno in alunos:
        if aluno['nome'] == nome_remover:
            alunos.remove(aluno)
            print(f"Aluno {nome_remover} removido com sucesso.")
            return
    print("Aluno não encontrado.")
def media_geral():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado para calcular a média.")
        return
    media = sum(aluno['nota'] for aluno in alunos) / len(alunos)
    print(f"A média geral das notas é: {media:.2f}")
while True:
    opcao = int(input("O que deseja fazer?\n1 - Cadastrar aluno \n2 - Listar alunos \n3 - Buscar aluno pelo nome \n4 - Remover aluno \n5 - Mostrar media geral das notas \n6 - Sair "))
    match opcao:
        case 1:
            adicionar()
        case 2:
            listar()
        case 3:
            buscar()
        case 4:
            remover()
        case 5:
            media_geral()
        case 6:
            break