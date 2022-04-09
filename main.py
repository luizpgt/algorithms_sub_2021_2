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

def print_sys_mensagem(msg):
    print("\n","-"*len(msg),"\n",msg,"\n","-"*len(msg),"\n")

# essa funcao situa o usuario, sobre onde ele esta, dentro do sistema.
def print_sessao_programa(sessao):
    print("\n",sessao,"\n","-"*15)

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

# esta funcao possui encapsulamento
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
            virgula = ','
            if virgula in preco:
                preco = preco.replace(virgula, '.')
            preco = float(preco)
            return preco
        else:
            return False

    def confirmacao_de_cadastro(cad_info):
        print("\n\nDeseja inserir o produto:")
        listar_produtos(cad_info)
        confirmacao = input('\n(S/n): ')
        print()
        confirmacao = confirmacao.lower()
        if confirmacao == 's':
            confirmacao = True
        elif confirmacao == 'n':
            confirmacao == False
        else:
            raise Exception
        
        return confirmacao
    
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
                print("Código do produto a ser adicionado: ", end=' ')
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
                print_sys_mensagem("O Valor adicionado pertence a outro produto! Entre um novo identificador único.")
            except:
                print_sys_mensagem(f"Valor inválido para {index[x]}! Por Favor, verifique novamente o conteúdo de sua entrada!")
        return valores 
    
    # armazena as informacoes no 
    # objeto e no array de objetos
    cad_info = []
    cad_info.append(Produto(*guia_de_cadastro(valores)))
    while True:
        try:
            if confirmacao_de_cadastro(cad_info) == True:
                db_produtos.append(*cad_info)
                print_sys_mensagem("Produto cadastrado com sucesso!")
            else:
                print_sys_mensagem("Cadastro Cancelado!")
            # array de valores limpo apos confirmacao
            cad_info.clear()
            return False
        except:
            print_sys_mensagem("O valor entrado não corresponde com nenhuma opção listada!")

def listar_produtos(lista_de_obj): # listagem de TODOS os produtos cadastrados
   
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
    if isinstance(elemento_busca, int) == True:
        for produto in db_produtos:
            if elemento_busca == produto.id:
                copia_prod = copy(produto)
                resultado.append(copia_prod)
    if isinstance(elemento_busca, str) == True:
        for produto in db_produtos:
            nome = produto.nome.lower()
            copia_prod = copy(produto)
            if elemento_busca == nome:
                resultado.insert(0, copia_prod)
            elif elemento_busca in nome:
                resultado.append(copia_prod)
    if resultado:
        return resultado
    else:
        raise Exception # produto nao encontrado

def atualizar_produto():
    def selecionar_produto():
        print("Nome ou código do produto que deseja alterar: ", end="")
        produto_entrado = input()
        produto = buscar_produto(produto_entrado)
        
        # para cada obj dentro do resultado
        # da busca, verificar se existem no-
        # mes de prod iguais
        cont_iguais = 0

        if len(produto) > 1:
            for obj in produto:
                nome = obj.nome
                if produto_entrado.lower() == nome.lower():
                    cont_iguais += 1
            if cont_iguais == 1:
                for i in range(1,len(produto)):
                    produto.pop(i)
            elif cont_iguais > 1:
                for obj in produto:
                    if produto_entrado.lower() != obj.nome.lower():
                        produto.remove(obj)
                print_sys_mensagem("Foram encontradas mais de uma correspondência para este nome!")
                listar_produtos(produto)
                print_sys_mensagem("Por Favor, entre dessa vez o código do produto que desejar: ")
                selecionar_produto()

        if len(produto) == 1:
            return produto
        else: 
            raise Exception
#        if len(produto) > 1:
 #           produto_valido = []
 #           if produto_entrado == produto[0].name:
#                produto_valido.append(produto[0])
 #               return produto_valido
 #       else:
  #          return produto

    def selecionar_mudanca(produto):
        print_sessao_programa("Produto selecionado")
        listar_produtos(produto)
        while True:
            try: 
                print("\nSelecione o que desejas alterar: ")
                print("\t[1] Preço")
                print("\t[2] Quantia em estoque")
                print("\t[3] Alterar Quantia e Preço do produto")
                mudanca = int(input())
                if mudanca == 1 or mudanca == 2 or mudanca == 3:
                    return mudanca
                else:
                    raise Exception
            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except:
                print_sys_mensagem("Entre uma opção válida")
    def entrar_alteracoes(mudanca):
        alteracoes = []
        alteracao = 0
        novo_preco = novo_estoque = False    
        while True:
            try: 
                if mudanca == 1 or mudanca == 3:
                    if novo_preco == False:
                        print("Entre um novo valor de preço para o produto: ")
                        novo_preco = float(input())
                        if mudanca == 3:
                            alteracoes.append(novo_preco) 
                        else:
                            alteracao = novo_preco

                if mudanca == 2 or mudanca == 3:
                    if novo_estoque == False:
                        print("Entre um novo valor para a quantia em estoque do produto: ")
                        novo_estoque = int(input()) 
                        if mudanca == 3:
                            alteracoes.append(novo_estoque)
                        else:
                            alteracao = novo_estoque
                return alteracoes if mudanca == 3 else alteracao
            except KeyboardInterrupt:
                
                # caso o usuario opte por cancelar
                # a atualizacao do cadastro
                raise KeyboardInterrupt
            except:
                print_sys_mensagem("Verifique se os valores entrados são válidos")

    def aplicar_alteracao(copia_prod_alterado):
        for produto in db_produtos:
            if copia_prod_alterado[0].id == produto.id:
                produto.preco = copia_prod_alterado[0].preco
                produto.estoque = copia_prod_alterado[0].estoque
        return True

    while True:
        try:
            print("Para cancelar a qualquer momento a atualização de cadastro:\tCtrl+c")
            produto_selec = selecionar_produto()
            alterar_em = selecionar_mudanca(produto_selec)
            alteracoes = entrar_alteracoes(alterar_em)

            if isinstance(alteracoes, list): 
                produto_selec[0].preco = alteracoes[0]
                produto_selec[0].estoque = alteracoes[1]
            elif isinstance(alteracoes, float):
                produto_selec[0].preco = alteracoes
            elif isinstance(alteracoes, int):
                produto_selec[0].estoque = alteracoes
                    
            if aplicar_alteracao(produto_selec) == True:
                print_sys_mensagem("Produto alterado com sucesso!")
                return False
            

        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except:
            print_sys_mensagem("Produto não encontrado")
    
def cadastrar_compra():

    # onde serao armazenadas informacoes sobre a compra
    carrinho = []

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
            print_sys_mensagem(f"A quantidade excede a máxima disponível em: {(qtd_estoque-qtd_compra)*-1} unidade(s).")
            return False

    def confirmar_insercao(prod_info):
        print("\nINFORMAÇÕES DA COMPRA: ")
        listar_produtos(prod_info)
        while True:
            try:
                if is_repetido(prod_info) == True:
                    print("Este produto já está no carrinho. Deseja efetuar uma segunda entrada? (s/n) ", end="")
                else: 
                    print("Deseja adicionar o produto ao carrinho? (S/n) ", end="")
                confirmacao = input()
                if confirmacao.lower() == 's':
                    return True
                elif confirmacao.lower() == 'n':
                    return False
                else:
                    raise Exception
            except:
                print_sys_mensagem("Entre uma alternativa válida.")
                    
    def fechar_compra(carrinho):
        
        # encerra exec da func caso
        # carrinho esteja vazio
        if len(carrinho) == 0:
            return False
        
        print_sessao_programa("CUPOM FISCAL: ")
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

        print_sys_mensagem(f"Preço Total da compra: {total_compra}")
    
        return True

    def add_to_carrinho(prod_adc):
        prod_adc = prod_adc[0]
        print_sessao_programa("CARRINHO:")
        carrinho.append(prod_adc)
        listar_produtos(carrinho)

    while True:
        try:
            print("\nPara cancelar a compra acione: \tCtrl+C")
            print("Para fechar o carrinho: \t'ok'")
            print("Digite o código do produto que deseja adicionar ao carrinho: ", end="")
            produto = input()
            if is_string(produto) == True:
                if produto.lower() == 'ok':
                    # caso a compra seja fechada com produtos no
                    # carrinho, sera encerrada essa funcao. o con-
                    # trario, a operacao de compra sera cancelada
                    if fechar_compra(carrinho) == True:
                        return False
                    else: 
                        raise KeyboardInterrupt
            else:
                # converte para int somente apos a confir-
                # macao de que a entrada nao eh uma str
                produto = int(produto)
            
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

            confirmacao_insercao = confirmar_insercao(prod_info)
            disponibilidade_estoque = is_qtd_disponivel(prod_info, qtd_compra)

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
            print_sys_mensagem("Por Favor, verifique o valor do código e/ou quantidade entrados.")     

# inicio - lista de opcoes
def main():
    while True:
        print_sessao_programa("INÍCIO")
        print("Escolha o que desejas fazer:")
        print("\t[1] \tCadastrar um novo produto")
        print("\t[2] \tAtualizar um produto cadastrado")
        print("\t[3] \tRegistrar nova compra")
        print("\t[4] \tBuscar produto")
        print("\t[5] \tRelatório de produtos")
        print("\t[-255] \tSair")
        acao = input("Entrada: ")
        try:
            acao = int(acao)
            if acao == 1:
                try:
                    cadastrar_produto()
                except KeyboardInterrupt:
                    print_sys_mensagem("Cadastro cancelado!")
            elif acao == 2:
                try:
                    print_sessao_programa("ALTERAR PRODUTO")
                    atualizar_produto() 
                except KeyboardInterrupt:
                    print_sys_mensagem("Atualização de cadastro Cancelada!")
            elif acao == 3:
                print_sessao_programa("ADICIOINAR COMPRA")
                cadastrar_compra()
            elif acao == 4:
                print_sessao_programa("BUSCAR")
                try:
                    busca = input("Entre um nome ou código do produto: ")
                    listar_produtos(buscar_produto(busca))
                except:
                    print_sys_mensagem("Produto não encontrado!")
            elif acao == 5:
                try:
                    print_sessao_programa("RELATÓRIO")
                    listar_produtos(db_produtos)
                except:
                    print_sys_mensagem("Aparentemente a lista de produtos está vazia!")
            elif acao == -255:
                print_sys_mensagem("Obrigado por usar o programa!")
                return False
            else:
                raise Exception
        except:
            print_sys_mensagem("Parece que sua entrada não condiz com nenhuma opção! Por Favor, tente novamente.")

main()
