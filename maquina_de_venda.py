#Classe dos produtos disponíveis para venda na máquina.
class Produto:
    def __init__(self, id, nome, preco, estoque):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

#Configurações iniciais/ padrão
#Cria as instâncias de produtos
produtos = []
produto_1 = Produto(1, 'Coca Cola', 375, 0)
produto_2 = Produto(2, 'Pepsi', 367, 5)
produto_3 = Produto(3, 'Monster Energy', 996, 1)
produto_4 = Produto(4, 'Café', 125, 100)
produto_5 = Produto(5, 'Redbull', 1399, 2)

produto_id = 5 #A ID é sequencial e única.

#Adiciona os produtos no array de produtos
produtos.append(produto_1)
produtos.append(produto_2)
produtos.append(produto_3)
produtos.append(produto_4)
produtos.append(produto_5)

#Caixa: notas e moedas disponíveis e suas respectivas quantidades. Obs: nota máxima aceita pela máquina é de R$20.
caixa = [['nota', 2000, 5],
         ['nota', 1000, 5],
         ['nota', 500, 5],
         ['nota', 200, 5],
         ['moeda', 100, 5],
         ['moeda', 50, 5],
         ['moeda', 25, 5],
         ['moeda', 10, 5],
         ['moeda', 5, 5],
         ['moeda', 1, 5]]

#Imprime as opções disponíveis para o cliente.
def exibeProdutos(produtos):
    i = 0
    while i < len(produtos):
        print(f" [{i + 1}] {produtos[i].nome} - R$ {(produtos[i].preco/100):.2f} - Quantidade em estoque: {produtos[i].estoque}")
        i += 1

#Exibe o menu completo com as opções.
def exibeMenu(produtos):
    print("\n \
           \n +--------------------------------------------------------+ \
           \n |                    ESCOLHA A BEBIDA                    | \
           \n +--------------------------------------------------------+ ")
    
    exibeProdutos(produtos)

    print(" +--------------------------------------------------------+  \
          \n\n Nota máxima aceita: R$20,00 \n")

#Formata o troco em forma de moedas, notas e suas quantidades a serem devolvidas.
def formataTroco(troco_a_devolver):
    for i in range(0, len(troco_a_devolver)):
        print(f'{troco_a_devolver[i][0]} {troco_a_devolver[i][1]}(s) de R${(troco_a_devolver[i][2]/100):.2f}')

#Modo administrador
def modoAdmin():
    global produto_id
    while True:
        print('\nModo administrador.')
        opcao_admin = input('\nO que deseja fazer? \
                             \n[1] Adicionar produto \
                             \n[2] Remover produto \
                             \n[3] Editar produto \
                             \n[4] Sair do modo administrador\n')
        
        #Verifica validade do input do usuário
        while not(opcao_admin == '1' 
            or opcao_admin == '2' 
            or opcao_admin == '3' 
            or opcao_admin == '4'):
            print('Opção inválida. Tente novamente.\n')

        #Adiciona produto
        if opcao_admin == '1':
            print('\nOpção inserir novo produto.')
            produto_id += 1
            produto_nome = input('Insira o nome do produto: ')
            produto_preco = float(input('Insira o preço do produto (preço máximo R$ 20,00): '))
            produto_estoque = int(input('Insira a quantidade em estoque do produto: '))
            novo_produto = Produto(produto_id, produto_nome, int(produto_preco*100), produto_estoque)
            produtos.append(novo_produto)
            print('Produto adicionado com sucesso.')

        #Remove produto
        elif opcao_admin == '2':
            print('\nOpção remover produto.')
            exibeProdutos(produtos)
            remove_produto = int(input('\nQual destes produtos deseja remover? '))
            print(f'Produto {produtos[remove_produto - 1].nome} removido com sucesso.')
            produtos.pop(remove_produto - 1)
            print('Produto removido com sucesso.')
        
        #Edita produto
        elif opcao_admin == '3':
            print('\nOpção editar produto.')
            exibeProdutos(produtos)
            produto_a_editar = int(input('Que produto deseja editar? ')) - 1
            print(f'Edite o produto {produtos[produto_a_editar].nome}.')
            produtos[produto_a_editar].nome = input('Edite o nome do produto: ')
            produtos[produto_a_editar].preco = int((float(input('Edite o preço do produto (preço máximo R$ 20,00): '))) * 100)
            produtos[produto_a_editar].estoque = int(input('Edite a quantidade do produto em estoque: '))            
            print('Produto editado com sucesso.')

        #Sai do modo administrador
        elif opcao_admin == '4':
            print('Modo administrador finalizado.')
            return

#Modo de venda
def modoVenda(opcao):
    verifica_pagamento = True

    #Verifica se a opção é válida.
    for idx, produto in enumerate(produtos):
        if opcao != (idx + 1):
            continue

        if produto.estoque < 1:
            print('Produto sem estoque. Por favor escolha outro.')
            return

        while verifica_pagamento == True:
            pagamento = input(f'Por favor insira uma nota de valor acima de R${produto.preco/100} e no máximo de R$20,00: ')

            #Verifica input do usuário
            try:
                pagamento = int(pagamento)
            except:
                print('Por favor insira uma nota de R$2,00 até R$20,00.')
                continue 
            
            #Verifica se a nota inserida é maior que o preço do produto e menor que a nota máxima permitida que é 20 reais.
            if pagamento >= produto.preco/100 and pagamento <= 20:
                troco = pagamento * 100 - produto.preco
                troco_a_devolver = []
                
                #Percorre a matriz, da maior pra menor nota/ moeda em caixa.
                for k in range(len(caixa)): 
                    notasOuMoedas = troco // caixa[k][1]
                
                    #Verifica se a quantidade das notas ou moedas requeridas é suficiente.
                    if caixa[k][2] >= notasOuMoedas:
                        troco -= notasOuMoedas * caixa[k][1]
                        caixa[k][2] -= notasOuMoedas
                        if notasOuMoedas > 0:
                            troco_a_devolver.append([notasOuMoedas, caixa[k][0], caixa[k][1]])
            
                if troco == 0:
                #Máquina entrega o produto com sucesso.
                    print(f'\nMáquina devolve troco de R${(pagamento * 100 - produto.preco)/100}')
                    formataTroco(troco_a_devolver)
                    print(f'\n*O produto {produto.nome} é entregue pela máquina.*')
                    produto.estoque -= 1
                    verifica_pagamento = False
                
                #Se a máquina não possui troco em caixa.
                else:
                    print('\nMáquina com estoque insuficiente de dinheiro em caixa para o troco necessário.')
                    print(f'*Máquina devolve R$ {pagamento:.2f}*')
                    verifica_pagamento = False
  
            #Se o cliente inserir uma nota diferente das permitidas.
            else: 
                print('Nota inválida.')
                print('*Máquina devolve o dinheiro que foi inserido.*\n')

#Primeira mensagem que o usuário vê na tela
print("Bem vindo à máquina de venda de bebidas!")
verifica_pagamento = True

#Loop para cliente escolher produto e realizar o pagamento.
while True:
    exibeMenu(produtos)
    opcao = input('Sua escolha: ')

    #Verifica a validade do input do usuario
    try:
        opcao = int(opcao)
    except:
        print('Opção inválida. Por favor escolha uma das opções existentes.')
        continue

    opcao = int(opcao)

    #Ativa modo administrador
    if opcao == 657865:
        modoAdmin()
    #Se o usuário escolhe uma opção existente
    elif opcao > 0 and opcao <= len(produtos):
        modoVenda(opcao)
        #Verifica se o cliente quer fazer outra compra.
        deseja_continuar = input('\nDeseja continuar? (s/n)')
        if deseja_continuar != 's':
            break

    #Se o cliente escolhe uma opção inválida.
    else:
        print('Opção inválida. Por favor escolha uma das opções existentes.')

#Finaliza o programa.
print('\nVolte sempre!')
    


        

