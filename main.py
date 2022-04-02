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

# esta funcao possui encapsulamento
def cadastrar_produto():

    print("\nVocê está em: CADASTRO de produtos!")
    print("Para cancelar a ação de CADASTRO a qualquer momento, pressione a combinação de teclas CTRL+C\n")
    # array para armazenar entradas do usuario que 
    # posteriormente serao adicionadas ao objeto
    valores = []

    def is_duplo_id(id):
        for objeto in db_produtos:
            if id == objeto.id:
                return True
    
    def is_string(nome):
        nome = nome.lower()
        alfabeto = 'abcdefghijklmnopqrstuvwxyz'
        cont = 0
        for letra in list(alfabeto):
            if letra in nome:
                cont += 1
        if cont > 0:
            return True
        else:
            return False

    def is_valid_preco(preco):
        if is_string(preco) == False:
            virgula = ','
            if virgula in preco:
                preco = preco.replace(virgula, '.')
            preco = float(preco)
            return preco
        else:
            return False

    def confirmacao_de_cadastro(valores):
        print("O produto será cadastrado com as seguintes informações:\n")
        #sera adicionado mais codigo aqui  
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
                print("entre o código do produto a ser adicionado: ", end=' ')
            elif index[x] == 'NOME':
                print("entre o nome do produto a ser adicionado: ", end=' ')
            elif index[x] == 'PRECO':
                print("entre o preco do produto a ser adicionado: ", end=' ')
            elif index[x] == 'ESTOQUE':
                print("entre a quantia do produto X em estoque: ", end=' ')
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
                print("O Valor adicionado pertence a outro produto! Entre um novo identificador único.")
            except:
                print(f"Valor inválido para {index[x]}! \nPor Favor, verifique novamente o conteúdo de sua entrada!\n")
        return valores 
    
    # armazena as informacoes no 
    # objeto e no array de objetos
    x = guia_de_cadastro(valores)
    confirmacao_de_cadastro(valores)
    db_produtos.append(Produto(*x))

    # array de valores limpo apos confirmacao
    valores.clear()
    return print(f"Produto [{db_produtos[0].nome}] Cadastrado!")
    

    
#funcao principal - pagina principal - lista de opcoes
def main():
    while True: 
        print("\n\nEscolha o que desejas fazer:\n\t[1] \tcadastrar um novo produto\n\t[-255] \tsair")
        acao = input("Entrada: ")
        try:
            acao = int(acao)
            if acao == 1:
                try:
                    cadastrar_produto()
                except KeyboardInterrupt:
                    print("\n\t\t[ Cadastro cancelado! ]")
            elif acao == -255:
                print("Obrigado por usar o programa!")
                return False
            else:
                raise IndexError
        except:
            print("Sua entrada foi considerada inválida! Por Favor, tente novamente:")
print("\tSeja Bem Vindo, sr. Operador!")
main()
