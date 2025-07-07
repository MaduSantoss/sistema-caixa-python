def menu():
    print("=" * 10 + " SISTEMA DE CAIXA " + "=" * 10)
    print("""
[1] - Adicionar produto
[2] - Ver produtos
[3] - Total da compra
[4] - Finalizar compra
""")

produtos = []

def adicionar_produto(produtos):
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    produtos.append({"nome": nome, "preco": preco})
    print("Produto adicionado com sucesso!")
    return produtos

def ver_produtos(produtos):
    print("Produtos cadastrados:")
    for indice, produto in enumerate(produtos):
        print(f"{indice + 1}. Nome: {produto['nome']} , Preço: R${produto['preco']:.2f}")
    return produtos

def total_da_compra(produtos):
    total = 0
    for produto in produtos:
        total += produto['preco']
    print(f"Total da compra: R${total:.2f}")
    return total

while True:
    menu()
    try:
        op = int(input("Bem-vindo! Escolha uma opção: "))
    except ValueError:
        print("Opção inválida. Digite um número de 1 a 4.")
        continue

    if op == 1:
        adicionar_produto(produtos)
    elif op == 2:
        ver_produtos(produtos)
    elif op == 3:
        total_da_compra(produtos)
    elif op == 4:
        print("Saindo... Obrigado por comprar conosco!")
        break
    else:
        print("Opção inválida. Tente novamente.")
