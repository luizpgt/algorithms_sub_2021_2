#ALUNO: luiz paulo grafetti terres
#MATERIA: algoritmos e lógica de programacao 2021.2

# lista de PRODUTOS de escopo global: 'banco' de produtos. 
db_produtos = []

class Produto ():
    def __init__(self, id, nome, preco, estoque):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

def print_sys_mensagem(msg):
    print("\n","-"*len(msg),"\n",msg,"\n","-"*len(msg))

# essa funcao situa o usuario, sobre onde ele esta, dentro do sistema.
def print_sessao_programa(sessao):
    print("\n",sessao,"\n","-"*15)

def is_string(palavra):
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
    if len(lista_de_obj) < 1: # ALTERAR-----------------------------------------------------------
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
        excesso_estoque = tam_estoque - 7
        coluna_estoque = '| ESTOQUE' 
        coluna_estoque += ' '*excesso_estoque + ' |'

        print(coluna_id, coluna_nome, coluna_preco, coluna_estoque)

        # a linha que separa o cabecalho do corpo: de tamanho total da tabela
        linha_sep = coluna_id +' '+ coluna_nome +' '+ coluna_preco +' '+ coluna_estoque
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
            tam_min_estoque = 7
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
                resultado.append(produto)
                print(f"produto encontrado: \n")
    if isinstance(elemento_busca, str) == True:
        for produto in db_produtos:
            nome = produto.nome.lower()
            if elemento_busca == nome:
                print('1 prod encontrado')
                resultado.insert(0, produto)
            elif elemento_busca in nome:
                print('outro prod encontrado')
                resultado.append(produto)
    if resultado:
        return resultado
    else:
        raise Exception # produto nao encontrado

# pagina principal - lista de opcoes
def main():
    while True: 
        print("\n\nEscolha o que desejas fazer:")
        print("\t[1] \tcadastrar um novo produto")
        print("\t[2] \tlistar produtos")
        print("\t[3] \tbuscar produto")
        print("\t[-255] \tsair")
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
                    print_sessao_programa("LISTAGEM")
                    listar_produtos(db_produtos)
                except:
                    print_sys_mensagem("Aparentemente a lista de produtos está vazia!")
            elif acao == 3:
                print_sessao_programa("BUSCAR")
                try:
                    busca = input("Entre um nome ou código do produto: ")
                    listar_produtos(buscar_produto(busca))
                except:
                    print_sys_mensagem("Produto não encontrado!")
            elif acao == -255:
                print_sys_mensagem("Obrigado por usar o programa!")
                return False
            else:
                raise IndexError
        except IndexError:
            print_sys_mensagem("Parece que sua entrada não condiz com nenhuma opção! Por Favor, tente novamente.")
        except:
            print_sys_mensagem("Sua entrada foi considerada inválida! Por Favor, tente novamente:")
print("\tSeja Bem Vindo, sr. Operador!")
main()
