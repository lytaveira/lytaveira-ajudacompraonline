class Produto:
    def __init__(self, nome, preco, moeda):
        self.nome = nome
        self.preco = preco
        self.moeda = moeda

class CarrinhoCompras:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, produto, quantidade):
        self.itens.append({'produto': produto, 'quantidade': quantidade})

    def calcular_total(self, taxa_cambio):
        total = 0
        for item in self.itens:
            preco_unitario = item['produto'].preco
            quantidade = item['quantidade']
            total += (preco_unitario * quantidade) * taxa_cambio
        return total

    def exibir_carrinho(self, taxa_cambio):
        print("\nCarrinho de Compras:")
        for item in self.itens:
            produto = item['produto']
            quantidade = item['quantidade']
            preco_em_reais = produto.preco * taxa_cambio
            print(f"{produto.nome} x{quantidade}: R${preco_em_reais:.2f}")

def adicionar_produto_interativo():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto na moeda estrangeira: "))
    moeda = input("Digite a moeda do produto (por exemplo, USD, EUR, CNY): ")
    return Produto(nome, preco, moeda)

def adicionar_item_interativo(carrinho):
    produto = adicionar_produto_interativo()
    quantidade = int(input("Digite a quantidade: "))
    carrinho.adicionar_item(produto, quantidade)
    print(f"{quantidade} {produto.nome}(s) adicionado(s) ao carrinho!")

def main():
    carrinho = CarrinhoCompras()

    # Definindo taxas de câmbio
    taxas_cambio = {'EUR': 5.36, 'USD': 4.93, 'CNY': 0.69}

    while True:
        print("\n--- Menu ---")
        print("1. Adicionar Produto ao Carrinho")
        print("2. Exibir Carrinho")
        print("3. Calcular Total do Carrinho em BRL")
        print("4. Sair")

        escolha = input("Escolha uma opção (1/2/3/4): ")

        if escolha == '1':
            adicionar_item_interativo(carrinho)

        elif escolha == '2':
            moeda = input("Digite a moeda para exibir o carrinho (EUR, USD, CNY): ").upper()
            taxa_cambio = taxas_cambio.get(moeda, 1.0)
            carrinho.exibir_carrinho(taxa_cambio)

        elif escolha == '3':
            moeda = input("Digite a moeda para calcular o total em BRL (EUR, USD, CNY): ").upper()
            taxa_cambio = taxas_cambio.get(moeda, 1.0)
            total_brl = carrinho.calcular_total(taxa_cambio)
            print(f"\nTotal do Carrinho em BRL: R${total_brl:.2f}")

        elif escolha == '4':
            print("Saindo do programa. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
