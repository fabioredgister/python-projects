print('  >>SISTEMA DE COMPRAS ONLINE<<\n')

#   Declaração de funções antes do início do código principal

#       Mostra o custo total dos itens.
#       Utilizado ao adicionar itens e ao chegar na conclusão da compra.
def mostrarCusto():
    global custoTotal, saldo
    print(f'  O custo total atual corresponde a R$ {custoTotal:.2f}.')
    if(custoTotal<=saldo):
        print(f'  R$ {(saldo-custoTotal):.2f} restantes.')
    else:
        print(f'  AVISO: SALDO INSUFICIENTE! Faltam R$ {(saldoFinal*-1.0):.2f}\n')

#       Mostra a lista de itens adicionados ao carrinho de compras.
#       Utilizado ao remover itens e como opção na tela de seleção da conclusão de compras.
def mostrarCompras():
    global compras
    print()
    if len(compras)==1:
        print(f'1 item cadastrado.')
    else:
        print(f'{len(compras)} itens cadastrados.')
    print('NOME - PRECO - QUANTIDADE A SER COMPRADA')
    for chave in compras:
        print(f"  {chave} - {compras[chave][0]:.2f} - {compras[chave][1]}")

#       Mostra os preços de cada item individualmente e em conjunto.
#       Utilizado ao remover itens.
def mostrarPreco(produtoRemove):
    global compras
    if compras[produtoRemove][1]==1:
        print(f'  {produtoRemove} possui 1 unidade de R$ {compras[produtoRemove][0]:.2f} a ser comprada.')
    else:
        print(f'  {produtoRemove} possui {compras[produtoRemove][1]} unidades de R$ {compras[produtoRemove][0]:.2f} a serem compradas.')
        print(f'  Ao todo, as {compras[produtoRemove][1]} unidades custam R$ {compras[produtoRemove][0]*compras[produtoRemove][1]:.2f}.')

#       Confirmação para cancelar as compras.
#       Utilizado quando o usuário insere 0 para sair na adição de itens ou na conclusão da compra.
def cancelarCompras(varVerif):
    if varVerif == 0:
        while True:
            cancelar = input('>>Voce quer cancelar as suas compras? [S/N] R: ')
            if cancelar!='s' and cancelar!='S' and cancelar!='n' and cancelar!='S':
                print('  Opção inválida! Redigite.\n')
            else:
                break
        return cancelar=='s' or cancelar=='S'
    else:
        return True

#       Confirmação para prosseguir, mesmo com quantidades enormes.
#       Utilizado quando o usuário insere uma grande quantidade de produtos e uma grande quantidade de unidades do produto.
def verifQuantEnorme(varVerif, valor):
    if int(varVerif)>valor:
        print(f'  {varVerif} é uma quantidade muito grande!')
        while True:
            prosseguir = input('>>Tem certeza que deseja comprar tudo isso? [S/N] R: ')
            if prosseguir!='s' and prosseguir!='S' and prosseguir!='n' and prosseguir!='N':
                print('  Opção inválida! Redigite.\n')
            else:
                break
        return prosseguir.lower()=='s'
    else:
        return True

#       Depositar dinheiro na conta do site.
#       Utilizado no início do jogo e na conclusão da compra.
def depositar():
    while True:
        novoSaldo = input('>>Informe o valor a ser depositado: R$ ')
        if not(novoSaldo.replace('.', '', 1).isdigit()):
            print('  Valor inválido! Redigite.\n')
        elif float(novoSaldo)<0:
            print('  Valor inválido! Redigite.\n')
        else:
            return float(novoSaldo)

#       Inserir quantidade de produtos a serem adicionados no carrinho.
#       Utilizado no início da compra e na conclusão quando o usuário decidir adicionar mais itens.
def quantMercadoriasComprar():
    while True:
        novasMercadorias = input('>>Insira a quantidade de mercadorias que você deseja adicionar: ')
        if novasMercadorias.isnumeric():
            if verifQuantEnorme(novasMercadorias, 10):
                return int(novasMercadorias)
        else:
            print('  Valor inválido! Redigite.\n')

#       Procedimento para adicionar produtos ao carrinho de compras
#       Utilizado no início da compra e na conclusão quando o usuário decidir adicionar mais itens.
def adicionar():
    global compras, custoTotal, saldoFinal, quantTotal
    while quantTotal > len(compras):
        while True:
            print(f'  Produto {len(compras)+1}/{quantTotal}')
            print('  Digite 0 para sair.')
            nome = input(f'>>Digite o nome do {len(compras)+1}º produto: ')
            if nome.isspace():
                print('  ERRO: O nome do produto não pode ser apenas espaços! Redigite.\n')
            elif nome.isnumeric() or nome.replace('.', '', 1).isdigit():
                if nome.isnumeric():
                    nome = int(nome)
                if nome==0:
                    break
                print('  ERRO: O nome do produto não pode ser apenas números! Redigite.\n')
            else:
                if nome.title() in compras:
                    print('  ERRO: Já existe um produto de mesmo nome registrado! Redigite.\n')
                else:
                    nome = nome.title()
                    break

        while nome!=0:
            print("\nAVISO: Não adicione ',' para separar a casa do milhar.")
            print("       Use '.' para dividir os centavos.")
            preco = input(f'>>Digite o preço de {nome}: ')
            if preco.isnumeric() or preco.replace('.', '', 1).isdigit():
                preco = float(preco)
                break
            else:
                print(f'  {preco} é um preço inválido! Redigite.\n')
        
        while nome!=0 and preco!=0:
            quantUnidades = input(f'>>Digite a quantidade de unidades a ser adquirida: ')
            if not(quantUnidades.isnumeric()):
                print(f'  {quantUnidades} não é uma quantidade de unidades válida! Redigite.\n')
            else:
                quantUnidades = int(quantUnidades)
                if verifQuantEnorme(quantUnidades, 25):
                    break

        # Dicionário 'compras' possui como valor tuplas de dois valores
        # Fórmula do que foi dito acima: dicionario.update(chave: [1º valor da tupla, 2º valor da tupla])
        # Neste código, essa fórmula se aplica da seguinte forma: compras.update(nome do produto: [preço, quantidade de produtos])
        if nome!=0 and preco!=0 and quantUnidades!=0:
            compras.update({nome: [preco, quantUnidades]})

            custoTotal += compras[nome][0] * compras[nome][1]
            saldoFinal = saldo-custoTotal
            if quantTotal > len(compras):
                mostrarCusto()
                print()
        else:
            if len(compras)>0:
                quantTotal = len(compras)
            break

#       Remover itens do carrinho de compras.
#       Utilizado como opção na conclusão da compra, seja quando o saldo é insuficiente ou não.
def remover():
    global compras, quantTotal

    while True:
        if len(compras)==1:
            produtoRemove = list(compras.keys())[0]
        else:
            mostrarCompras()
            print('\n  Digite 0 para sair.')
            produtoRemove = input('>>Digite o nome do produto a ser removido: ')
            if produtoRemove.isalnum():
                produtoRemove = produtoRemove.title()  
            if produtoRemove=='0':
                break

        if produtoRemove in compras:
            mostrarPreco(produtoRemove)
            while True:
                if(compras[produtoRemove][1]>1):
                    print('\n  Digite 0 para sair.')
                    quantRemove = input('>>Digite quantas unidades você deseja remover: ')
                    if not(quantRemove.isnumeric()):
                        print('  ERRO: O valor digitado é inválido! Redigite.\n')
                    elif int(quantRemove)==0:
                        break
                    elif int(quantRemove) > compras[produtoRemove][1]:
                        print('  ERRO: A quantidade a ser retirada é maior que a quantidade que inicialmente seria comprada! Redigite.\n')
                    elif int(quantRemove) < 0:
                        print('  ERRO: Quantidade inválida! Redigite.\n')
                    elif int(quantRemove)==compras[produtoRemove][1]:    
                        compras.pop(produtoRemove)
                        print(f'  {produtoRemove} foi removido completamente.')
                        break
                    else:
                        compras[produtoRemove][1] = compras[produtoRemove][1]-int(quantRemove)
                        print(f'  {produtoRemove} teve sua quantidade alterada.')
                        mostrarPreco(produtoRemove)
                        break
                else:
                    while True:
                        removerUnicaUnid = input(f'  Deseja remover a única unidade de {produtoRemove}?\n>>[S/N] R: ')
                        if removerUnicaUnid=='s' or removerUnicaUnid=='S':
                            compras.pop(produtoRemove)
                            break
                        elif removerUnicaUnid=='n' or removerUnicaUnid=='N':
                            break
                        else:
                            print('  ERRO: Opção inválida! Redigite.\n')
                    break

        else:
            print(f'  ERRO: {produtoRemove} não foi adicionado.')

        if len(compras)>1:
            while True:
                remover = input('\n>>Deseja remover mais algum item da lista? [S/N]: ')
                if remover=='s' or remover=='S':
                    break
                elif remover=='n' or remover=='N':
                    break
                else:
                    print('  A opção digitada é inválida! Redigite.')
            remover = remover=='s' or remover=='S'
        else:
            remover = False

        if not(remover):
            quantTotal = len(compras)
            break

#   Início do código principal

#       Declaração de variáveis
saldo = 0.0
saldoFinal = 0.0
compras = dict()
custoTotal = 0.0

#       Primeiros passos
print('  Olá! Seja bem-vindo ao sistema de compras online.\n')
print('  Faça o seu primeiro depósito para poder fazer suas primeiras compras.')
while True:
    saldo = depositar()
    if cancelarCompras(saldo):
        break

if saldo!=0:
    if saldo>99:
        print('\n  Você está indo bem!')
    else:
        print()
    print('  Agora precisamos saber quantas mercadorias você pretende comprar inicialmente.')
    while True:
        quantTotal = quantMercadoriasComprar()
        if cancelarCompras(quantTotal):
            break

#       Verificar se o que foi adicionado pode ser comprado ou se a compra foi cancelada.
if saldo==0 or quantTotal==0:
    print('  Compra cancelada.')
else:
    while True:
        adicionar()
        if cancelarCompras(len(compras)):
            break
    if len(compras)==0:
        print('  Compra cancelada.')
    while len(compras)>0:
        mostrarCusto()
        if saldoFinal>=0:
            while True:
                print(f'\nA compra pode ser concluída. Deseja fazer alguma alteração?')
                print('  [1] Ver carrinho de compras')
                print('  [2] Adicionar itens')
                print('  [3] Remover itens')
                print('  [4] Concluir compra')
                print('  [5] Cancelar compra')
                alterar = input('>>R: ')
                if not(alterar.isnumeric()):
                    print(f'  {alterar} não é uma opção válida! Redigite.')
                elif int(alterar)==1:
                    mostrarCompras()
                elif int(alterar)==2:
                    quantTotal += quantMercadoriasComprar()
                    adicionar()
                    break
                elif int(alterar)==3:
                    remover()
                    
                    #       É executado caso o usuário remova todos os produtos do carrinho de compras
                    while len(compras)==0:
                        if cancelarCompras(len(compras)):
                            break
                        else:
                            while True:
                                quantTotal = quantMercadoriasComprar()
                                if cancelarCompras(quantTotal):
                                    break
                            adicionar()
                    if len(compras)==0:
                        print('  Compra cancelada.')

                    break
                elif int(alterar)==4:
                    print('  Compra efetuada com sucesso!')
                    break
                elif int(alterar)==5:
                    if (cancelarCompras(0)):
                        print('  Compra cancelada.')
                        break
                else:
                    print(f'  {alterar} não é uma opção válida! Redigite.')
            if int(alterar)==4 or int(alterar)==5:
                break
        else:
            while True:
                print('  [1] Ver carrinho de compras')
                print('  [2] Fazer um depósito')
                print('  [3] Remover itens do carrinho de compras')
                print('  [4] Cancelar compra')
                opcao = input('>>Digite uma opcao a seguir: ')
                if not(opcao.isnumeric()):
                    print('  A opção digitada é inválida! Redigite.')
                elif int(opcao)==1:
                    mostrarCompras()
                elif int(opcao)==2:
                    saldo += depositar() 
                    print()
                    break
                elif int(opcao)==3:
                    remover()
                    print()
                    
                    #       É executado caso o usuário remova todos os produtos do carrinho de compras
                    while len(compras)==0:
                        if cancelarCompras(len(compras)):
                            break
                        else:
                            while True:
                                quantTotal = quantMercadoriasComprar()
                                if cancelarCompras(quantTotal):
                                    break
                            adicionar()
                    if len(compras)==0:
                        print('  Compra cancelada.')
                        
                    break
                elif int(opcao)==4:
                    print('  Compra cancelada.')
                    break
                elif int(opcao)==5:
                    if (cancelarCompras(0)):
                        print('  Compra cancelada.')
                        break
                else:
                    print(f'  {alterar} não é uma opção válida! Redigite.')
                print()
            if int(opcao)==4 or int(opcao)==5:
                break

        #       Cálculo do custo total da compra e do saldo final após a compra ser realizada.
        #       Serve para verificar se a compra pode ser concluída ou não.
        custoTotal = 0.0
        for indice in compras:
            custoTotal += compras[indice][0] * compras[indice][1]    
        saldoFinal = saldo-custoTotal
