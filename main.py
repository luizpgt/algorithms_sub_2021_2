#ALUNO: luiz paulo grafetti terres
#MATERIA: algoritmos e lógica de programacao 2021.2
from copy import copy

# lista de PRODUTOS de escopo global: 'banco' de produtos. 
db_produtos = []

class Produto ():
    def __init__(self, id, nome, preco, estoque):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

# exibe mensagens formatadas visando atencao do usuario
def print_sys_mensagem(msg):
    print("\n","-"*len(msg),"\n",msg,"\n","-"*len(msg),"\n")

# essa funcao situa o usuario, sobre onde ele esta, dentro do sistema.
def print_sessao_programa(sessao):
    tam = len(sessao)
    print("\n",sessao,"\n","-"*tam)

# verifica se a entrada eh uma string 
def is_string(palavra):
    palavra = str(palavra) 
    palavra = palavra.lower()
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    cont = 0
    for letra in list(alfabeto):
        if letra in palavra:
            cont += 1
    if cont > 0:
        return True
    else:
        return False

def get_confirmacao():
    conf = input("(s/n) ")
    conf = conf.lower()
    
    if conf == 's':
        return True
    if conf == 'n': 
        return False
    if is_string(conf) == True and conf != 's' and conf != 'n':
        print_sys_mensagem("Sua entrada não foi considerada válida, tente novamente!")
    if is_string(conf) == False:
        print_sys_mensagem("Por favor, entre uma das letras para confirmacao: (s/n)")
    return get_confirmacao()

def cadastrar_produto():

    print_sessao_programa("CADASTRO")
    print("Para cancelar a ação de CADASTRO a qualquer momento, pressione a combinação de teclas CTRL+C\n")
    # array para armazenar entradas do usuario que 
    # posteriormente serao adicionadas ao objeto
    valores = []

    def is_duplo_id(id):
        for objeto in db_produtos:
            if id == objeto.id:
                return True

    def is_valid_preco(preco):
        if is_string(preco) == False:
            
            # caso o usuario tenha entrado um float
            # no formato com virgula, sera feita uma
            # troca desse caractere para um '.'
            virgula = ','
            if virgula in preco:
                preco = preco.replace(virgula, '.')
            preco = float(preco)
            return preco
        else:
            return False

    def confirmacao_de_cadastro(cad_info):
        print("\n\nDeseja inserir o produto: ")
        listar_produtos(cad_info)
        conf = get_confirmacao()
        return conf
    
    def guia_de_cadastro(valores):
        
        # lista INDEX permite que sejam controladas
        # as entradas do usuario, e que seja feito
        # um tratamento basico dos dados entrados

        index = ['ID', 'NOME', 'PRECO', 'ESTOQUE']
        x = 0 # controla o indice da lista 

        while True:
            if x >= len(index):
                break
            elif index[x] == 'ID':
                print("Código do produto: \t\t", end=' ')
            elif index[x] == 'NOME':
                print("Nome do produto: \t\t", end=' ')
            elif index[x] == 'PRECO':
                print("Preco do produto: \t\t", end=' ')
            elif index[x] == 'ESTOQUE':
                print("Quantia do produto em estoque: ", end=' ')
            valor = input("\t\t")
            try:
                if index[x] == 'ID':
                    valor = int(valor)
                    # verifica uma possivel ocorrencia
                    # de identificador duplicado
                    if is_duplo_id(valor) == True:
                        raise IndexError
                    else:
                        valores.append(valor)
                elif index[x] == 'NOME':
                    valor = str(valor)
                    # verifica se a entrada eh realmente
                    # uma string antes de a armazenar
                    if is_string(valor) == True:
                        valor = valor.capitalize()
                        valores.append(valor)
                    else:
                        raise ValueError
                elif index[x] == 'PRECO':
                    # verifica se a entrada eh realmente um float
                    # antes de a armazenar
                    valor = is_valid_preco(valor)
                    if  valor == False: 
                        raise ValueError
                    elif isinstance(valor, float) == True:
                        valores.append(valor)
                elif index[x] == 'ESTOQUE':
                    valor = int(valor)
                    valores.append(valor)
                # altera o valor do index caso a entrada seja aceita e adicionada
                x += 1
            except IndexError:
                print_sys_mensagem("O Valor adicionado pertence a outro produto! Entre um novo identificador único !")
            except:
                print_sys_mensagem(f"Valor inválido para {index[x]}. Verifique novamente o conteúdo de sua entrada !")
        return valores 
    
    # armazena as informacoes no 
    # objeto e no array de objetos
    cad_info = []
    cad_info.append(Produto(*guia_de_cadastro(valores)))
    while True:
        try:
            if confirmacao_de_cadastro(cad_info) == True:
                db_produtos.append(*cad_info)
                print_sys_mensagem("Produto cadastrado com Sucesso !")
            else:
                print_sys_mensagem("Cadastro Cancelado !")
            # array de valores limpo apos confirmacao
            cad_info.clear()
            return False
        except:
            print_sys_mensagem("O valor entrado não corresponde com nenhuma opção listada !")

def listar_produtos(lista_de_obj):
    # caso não tenham produtos cadastrados, sera notificado que
    # a tabela nao possui elementos para fazer a listagem
    if len(lista_de_obj) < 1: 
        raise Exception
        
    # as variaveis TAM_X sao responsaveis por armazenar 
    # os tamanhos limites de cada coluna da tabela, ou seja, arma-
    # zenarao os maiores len() encontrados entre todos os objetos
    # armazenados
    tam_id = tam_nome = tam_preco = tam_estoque = 0
    
    for obj in lista_de_obj:
        
        # as variaveis a seguir: armazenar o tamanho [len()] de 
        # cada objeto referente a cada iteracao do laco de repe-
        # ticao
        id = len(str(obj.id))
        nome = len(str(obj.nome))
        preco = len(str(obj.preco))
        estoque = len(str(obj.estoque))
        
        # abaixo: filtrando os maiores objetos em 'comprimento'
        # e os armazenando
        if id > tam_id:
            tam_id = id
        if nome > tam_nome:
            tam_nome = nome
        if preco > tam_preco:
            tam_preco = preco
        if estoque > tam_estoque:
            tam_estoque = estoque


    def print_cabecalho(tam_id, tam_nome, tam_preco, tam_estoque):
        
        # as variaveis EXCESSO_X serao responsaveis por 
        # armazenar a quantia de 'espacos em branco' que serao im-
        # pressos a partir do nome de cada atributo no cabecalho

        # as variaveis COLUNA_X armazenarao o que sera 
        # impresso no cabecalho propriamente dito. ela sofre mul-
        # tiplas concatenacoes para o resultado final 
        
        # formatacao identificador
        excesso_id = tam_id - 2
        coluna_id = '| ID'
        coluna_id += ' '*excesso_id

        # formatacao nome
        excesso_nome = tam_nome - 4
        coluna_nome = '| NOME' 
        coluna_nome += ' '*excesso_nome
        
        # formatacao preco
        excesso_preco = tam_preco - 5
        coluna_preco = '| PRECO' 
        coluna_preco += ' '*excesso_preco
        
        # formatacao estoque
        excesso_estoque = tam_estoque - 10
        coluna_estoque = '| QUANTIDADE' 
        coluna_estoque += ' '*excesso_estoque + ' |'

        # a linha que separa (mede um tamanho completo da tabela)
        linha_sep = coluna_id +' '+ coluna_nome +' '+ coluna_preco +' '+ coluna_estoque
        
        print('-'*len(linha_sep))
        print(coluna_id, coluna_nome, coluna_preco, coluna_estoque)
        print('-'*len(linha_sep))

    def print_corpo(tam_id, tam_nome, tam_preco, tam_estoque):
         
        for obj in lista_de_obj:
            
            # convertendo cada atributo dos objetos para 
            # string para facilitar o manejo da tabela
            obj_id = str(obj.id)
            obj_nome = str(obj.nome)
            obj_preco = str(obj.preco)
            obj_estoque = str(obj.estoque)

            # as variaveis TAM_MIN_X sao responsaveis por armazenar 
            # os tamanhos minimos necessarios para cada coluna manter
            # uma estrutura organizada. esse valor minimo existe em
            # funcao da limitacao por parte do cabecalho, onde apare-
            # cem palavras de 2, 4, 5 a 7 letras

            # as variaveis TAM_X possuem o mesmo valor e mesma fun-
            # cao de quando utilizadas na print_cabecalho(). da mes-
            # ma forma acontece com as variaveis COLUNA_X, que nesse 
            # momento tem sua estrutura um pouco diferente
            
            # formatacao identificador
            tam_min_id = 2
            if tam_min_id > tam_id:
                excesso_id = tam_min_id - len(obj_id)
            else:
                excesso_id = tam_id - len(obj_id)
            coluna_id = '| '+obj_id
            if excesso_id >= 0:
                coluna_id += ' '*excesso_id
            
            # formatacao nome
            tam_min_nome = 4
            if tam_min_nome > tam_nome:
                excesso_nome = tam_min_nome - len(obj_nome)
            else:
                excesso_nome = tam_nome - len(obj_nome)
            coluna_nome = '| '+obj_nome
            if excesso_nome >= 0:
                coluna_nome += ' '*excesso_nome
            
            # formatacao preco
            tam_min_preco = 5
            if tam_min_preco > tam_preco:
                excesso_preco = tam_min_preco - len(obj_preco)
            else:
                excesso_preco = tam_preco - len(obj_preco)
            coluna_preco = '| '+obj_preco
            if excesso_preco >= 0:
                coluna_preco += ' '*excesso_preco

            # formatacao estoque
            tam_min_estoque = 10
            if tam_min_estoque > tam_estoque:
                excesso_estoque = tam_min_estoque - len(obj_estoque)
            else:
                excesso_estoque = tam_estoque - len(obj_estoque)
            coluna_estoque = '| '+ obj_estoque
            if excesso_estoque >= 0:
                coluna_estoque += ' '*excesso_estoque 
                coluna_estoque += ' |'

            print(coluna_id, coluna_nome, coluna_preco, coluna_estoque)

    print_cabecalho(tam_id, tam_nome, tam_preco, tam_estoque)
    print_corpo(tam_id, tam_nome, tam_preco, tam_estoque)

def buscar_produto(elemento_busca):
    resultado = []

    isString = is_string(elemento_busca)
    if isString == False:
        elemento_busca = int(elemento_busca)
    else:
        elemento_busca = elemento_busca.lower()
    
    # caso o usuario entre um codigo para busca
    if isinstance(elemento_busca, int) == True:
        for produto in db_produtos:
            if elemento_busca == produto.id:
                copia_prod = copy(produto)
                resultado.append(copia_prod)

    # caso o usuario entre um nome para busca
    if isinstance(elemento_busca, str) == True:
        for produto in db_produtos:
            nome = produto.nome.lower()
            copia_prod = copy(produto)
            if elemento_busca == nome:
                # para casos onde a entrada seja exatamente
                # igual ao produto encontrado, o produto re-
                # tornado ira para o topo da lista de resultados
                resultado.insert(0, copia_prod)
            elif elemento_busca in nome:
                # casos onde a string de entrada esta contida
                # no nome de algum objeto (semelhante)
                resultado.append(copia_prod)
    
    if resultado:
        return resultado
    else:
        raise Exception # produto nao encontrado

def atualizar_produto():

    def selecionar_produto():
        print("Código do produto: ", end="")
        produto_entrado = input()
        produto_entrado = int(produto_entrado)
        produto = buscar_produto(produto_entrado)
        
        if len(produto) == 1:
            return produto
        else: 
            raise Exception

    def selecionar_mudanca(produto):
        print_sessao_programa("Produto selecionado")
        listar_produtos(produto)
        while True:
            try: 
                print("\nSelecione o que alterar: ")
                print("\t[1] Preço")
                print("\t[2] Quantia em estoque")
                print("\t[3] Alterar Quantia e Preço do produto")
                mudanca = int(input())
                if mudanca == 1 or mudanca == 2 or mudanca == 3:
                    return mudanca
                else:
                    raise Exception
            except KeyboardInterrupt:
                # caso o usuario queira cancelar a alteracao (Ctrl+C)
                raise KeyboardInterrupt
            except:
                print_sys_mensagem("Entre uma opção válida !")

    def entrar_alteracoes(mudanca):

        alteracoes = [] # usado para mudanca = 3
        alteracao = 0 # usado caso mudanca = 1 ou 2

        # novo preco e estoque sao inicializados com false 
        # para podermos ter controle caso o usuario entre
        # um valor invalido somente para o estoque e um va-
        # lido para preco (e o bloco TRY abaixo precise ser
        # chamado mais de uma vez). importante para manter 
        # a linearidade do ponto de vista do usuario
        novo_preco = novo_estoque = False    
        
        while True:
            try: 
                if mudanca == 1 or mudanca == 3:
                    if novo_preco == False:
                        print("Novo Preço: ")
                        novo_preco = float(input())
                        
                        if mudanca == 3:
                            # caso 3 = alterar preco e estoque
                            alteracoes.append(novo_preco) 
                        else:
                            # caso 1 alterar somente preco
                            alteracao = novo_preco

                if mudanca == 2 or mudanca == 3:
                    if novo_estoque == False:
                        print("Nova quantia em Estoque: ")
                        novo_estoque = int(input()) 
                        if mudanca == 3:
                            # caso 3 alterar preco e estoque
                            alteracoes.append(novo_estoque)
                        else:
                            # caso 2 alterar estoque
                            alteracao = novo_estoque
                
                return alteracoes if mudanca == 3 else alteracao
            
            except KeyboardInterrupt:
                # cancela atualizacao de cadastro
                raise KeyboardInterrupt
            except:
                print_sys_mensagem("Verifique se os valores entrados são válidos !")

    def confirmar_alteracoes(prod_alterado):
        print("Alterar o produto com as seguintes alterações: ")

        listar_produtos(prod_alterado)
        conf = get_confirmacao()
        return conf
        
    def aplicar_alteracao(prod_alterado):
        for produto in db_produtos:
            if prod_alterado[0].id == produto.id:
                produto.preco = prod_alterado[0].preco
                produto.estoque = prod_alterado[0].estoque
        
        return True # positivo caso as alteracoes sejam aplicadas

    while True:
        try:
            print("Cancelar a qualquer momento a atualização de cadastro:\tCtrl+c")

            produto_selec = selecionar_produto()
            alterar_em = selecionar_mudanca(produto_selec)
            alteracoes = entrar_alteracoes(alterar_em)

            # caso o usuario opte por atualizar 
            # preco e estoque do mesmo produto
            if isinstance(alteracoes, list): 
                produto_selec[0].preco = alteracoes[0]
                produto_selec[0].estoque = alteracoes[1]
            # caso pretenda alterar somente o preco
            elif isinstance(alteracoes, float):
                produto_selec[0].preco = alteracoes
            # caso pretenda alterar somente o estoque
            elif isinstance(alteracoes, int):
                produto_selec[0].estoque = alteracoes
           
            conf = confirmar_alteracoes(produto_selec)
            if conf == True:
                if aplicar_alteracao(produto_selec) == True:
                    print_sys_mensagem("Produto alterado com sucesso !")
                else: 
                    print_sys_mensagem("Ocorreu algum problema ao salvar o produto !")
            else:
                print_sys_mensagem("Operação de alteração cancelada !")
            return False

        except KeyboardInterrupt:

            # cancela a operacao
            raise KeyboardInterrupt
        except:
            print_sys_mensagem("Produto não encontrado !")
    
def cadastrar_compra():

    # onde serao armazenadas informacoes sobre a compra
    carrinho = []

    # caso o mesmo produto apareca mais de 1 vez
    # no carrinho = True
    def is_repetido(compra_info):
        for produto in carrinho:
            if compra_info[0].id == produto.id:
                return True
        return False

    # caso tenham quantidades disponiveis do
    # produto no estoque, retornara POSITIVO
    # para continuar a compra
    def is_qtd_disponivel(info_compra, qtd_compra):
        qtd_estoque = 0
        
        for produto in db_produtos:
            if info_compra[0].id == produto.id:
                
                # armazena a quantidade total 
                # em estoque do produto sendo
                # comprado
                qtd_estoque = produto.estoque
        if is_repetido(info_compra) == True:
            for produto in carrinho:
                if info_compra[0].id == produto.id:
                    
                    # soma as quantidades de um 
                    # mesmo produto no carrinho
                    qtd_compra += produto.estoque

        # permite a compra somente se a quantia
        # de X estiver disponivel no estoque
        if qtd_estoque >= qtd_compra:
            return True
        else:
            print_sys_mensagem(f"Quantidade excede a máxima disponível em: {(qtd_estoque-qtd_compra)*-1} unidade(s) !")
            return False

    # mostra informacoes do produto a ser adicionado
    # ao carrinho e espera confirmacao do operador
    def confirmar_insercao(prod_info):
        print_sessao_programa("\nINFORMAÇÕES DA COMPRA")
        listar_produtos(prod_info)
       
        if is_repetido(prod_info) == True:
            print("Este produto mesmo produto já está no carrinho. Efetuar uma segunda entrada? ", end="")
        else:
            print("Adicionar produto ao carrinho? ", end=" ")
        conf = get_confirmacao()
        return conf

    # caso seja confirmado pelo operador,
    # o produto eh adicionado ao carrinho
    def add_to_carrinho(prod_adc):
        prod_adc = prod_adc[0]
        print_sessao_programa("CARRINHO")
        carrinho.append(prod_adc)
        listar_produtos(carrinho)
                    
    def fechar_compra(carrinho):
        
        # encerra exec da func cadastrar 
        # caso carrinho esteja vazio
        if len(carrinho) == 0:
            return False
        
        print_sessao_programa("CUPOM FISCAL")
        listar_produtos(carrinho)
        total_compra = 0
        
        # soma o valor total da compra
        # e da baixa no estoque de pro-
        # dutos
        for produto_comprado in carrinho:
            total_compra += produto_comprado.preco
            for produto in db_produtos:
                if produto_comprado.id == produto.id:
                    produto.estoque -= produto_comprado.estoque

        print_sys_mensagem(f"Preço Total da compra: {total_compra}.")
    
        # caso len(carrinho) >= 1 e os 
        # produtos tenham sido retirados
        # do estoque
        return True

    while True:
        try:
            print("\nPara cancelar a compra acione: \tCtrl+C")
            print("Para fechar o carrinho digite: \t'ok'")
            print("Digite o código do produto: ", end="")
            produto = input()
            if is_string(produto) == True:
                if produto.lower() == 'ok':

                    # caso a compra seja fechada com produtos no
                    # carrinho, sera encerrado este while, e a 
                    # compra encaminhada para fechamento. o con-
                    # trario, a operacao de compra sera cancelada
                    if fechar_compra(carrinho) == True:
                        return False
                    else: 
                        raise KeyboardInterrupt
                else:

                    # caso o valor entrado seja uma string
                    # nao esperada
                    raise Exception
            else:
                # converte para int somente apos a confir-
                # macao de que a entrada nao eh uma str
                produto = int(produto)
            
            # onde serao armazenadas infor-
            # macoes do produto comprado
            prod_info = []
            prod_info = buscar_produto(produto)
                 
            print("Quantidade: ",end="")
            qtd_compra = int(input())
            
            # faz as devidas alteracoes na (copia)
            # do produto escolhido para compra.
            # importante para o acompanhamento do
            # carrinho de compras. as alteracoes
            # no obj prod original serao feitas
            # ao confirmar da compra 
            prod_info[0].estoque = qtd_compra
            prod_info[0].preco = prod_info[0].preco*qtd_compra

            disponibilidade_estoque = is_qtd_disponivel(prod_info, qtd_compra)
            if disponibilidade_estoque == True:                
                # confirmacao do operador
                confirmacao_insercao = confirmar_insercao(prod_info)
            else: 
                continue

            # somente adiciona ao carrinho com confirmacao de quantia 
            # valida em estoque e confirmacao de entrada do operador
            if confirmacao_insercao == True and disponibilidade_estoque == True:
                add_to_carrinho(prod_info)
            elif confirmacao_insercao == False:
                print_sys_mensagem("O produto não foi inserido !")
            elif disponibilidade_estoque == False:
                print_sys_mensagem("Quantidade não disponível em estoque. Produto não inserido !")
        
        except KeyboardInterrupt:
            print_sys_mensagem("Compra cancelada")
            return False
        except:
            print_sys_mensagem("Verifique o valor do código e/ou quantidade entrados.")     

# inicio - lista de opcoes
def main():
    while True:
        print_sessao_programa("INICIO")
        print("Escolha sua próxima ação:")
        print("\t[1] \tCadastrar novo produto")
        print("\t[2] \tAtualizar produto cadastrado")
        print("\t[3] \tRegistrar compra")
        print("\t[4] \tBuscar produto")
        print("\t[5] \tRelatório de produtos")
        print("\t[-255] \tSair")
        acao = input("Entrada: ")
        try:
            acao = int(acao)
            if acao == 1: # cadastro novo produto 
                try:
                    cadastrar_produto()
                except KeyboardInterrupt:
                    print_sys_mensagem("Cadastro cancelado !")
            
            elif acao == 2: # atualizar cadastrod de produto
                try:
                    print_sessao_programa("ALTERAR PRODUTO")
                    atualizar_produto() 
                except KeyboardInterrupt:
                    print_sys_mensagem("Atualização de cadastro Cancelada !")
            
            elif acao == 3: # cadastrar nova compra
                print_sessao_programa("ADICIOINAR COMPRA")
                cadastrar_compra()
            
            elif acao == 4: # buscar produto na lista
                print_sessao_programa("BUSCAR")
                try:
                    busca = input("Entre um nome ou código do produto: ")
                    listar_produtos(buscar_produto(busca))
                except:
                    print_sys_mensagem("Produto não encontrado !")
            
            elif acao == 5: # listar todos os produtos
                try:
                    print_sessao_programa("RELATÓRIO")
                    listar_produtos(db_produtos)
                except:
                    print_sys_mensagem("Lista de produtos está vazia!")
            
            elif acao == -255: # sair
                print_sys_mensagem("Obrigado por usar o programa !")
                return False
            else:
                raise Exception
        
        except:
            print_sys_mensagem("Sua entrada não condiz com nenhuma opção. Tente novamente !")

main()
