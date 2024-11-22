def resumo():
    mensagem = "Augusta Ada Byron King (1815 — 1852), Condessa de Lovelace, atualmente conhecida como Ada Lovelace, foi uma matemática e escritora inglesa. É uma pioneira na inserção das mulheres no mundo da computação."
    return mensagem


def educacao():
    mensagem = "Ada foi educada em casa, aprendia matemática e ciências. Ela acreditava que a intuição e a imaginação eram fundamentais para pôr em prática conceitos matemáticos e científicos de forma eficaz. Ada valorizava a metafísica tanto quanto a matemática, sendo ambas ferramentas para explorar mundos invisíveis ao nosso redor."
    return mensagem


def linguagem_ada():
    mensagem = "A linguagem de programação Ada foi criada em homenagem à Ada Lovelace pelo Departamento de Defesa dos Estados Unidos. A documentação da linguagem foi aprovada em 10 de Dezembro de 1980."
    return mensagem


def artigos():
    mensagem = ""
    return mensagem


def citacoes():
    mensagem = ""
    return mensagem


def sair():
    mensagem = "\nObrigado pela leitura!"
    return mensagem


def erro():
    mensagem = "\nOpção inválida!"
    return mensagem


print("\nOlá! Você está aprendendo sobre Ada Lovelace.\n")

continuar = True
while continuar == True:

    opcao = int(
        input(
"""
\nDigite o número correspondente ao menu que você deseja acessar:
1 - Resumo
2 - Educação
3 - Linguagem Ada
4 - Principais Artigos
5 - Citações
6 - Sair\n
"""
        )
    )

    if opcao == 1:
        print("1 - Resumo")
        mensagem = resumo()

    elif opcao == 2:
        print("2 - Educação")
        mensagem = educacao()

    elif opcao == 3:
        print("3 - Linguagem Ada")
        mensagem = linguagem_ada()

    elif opcao == 4:
        print("4 - Principais Artigos")
        mensagem = artigos()

    elif opcao == 5:
        print("5 - Citações")
        mensagem = citacoes()

    elif opcao == 6:
        mensagem = sair()
        continuar = False

    else:
        mensagem = erro()

    print(mensagem)
