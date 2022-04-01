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
    print("Seja Bem Vindo\nAo CADASTRO de produtos!")
    valores = []

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
                    # ADICIONAR VERIFICACAO DE DUPLO ID
                    valores.append(valor)            
                elif index[x] == 'NOME':
                    valor = str(valor)
                    # ADICIONAR VERIFICACAO DE PALAVRA VERDADEIRA
                    valores.append(valor)
                elif index[x] == 'PRECO':
                    valor = float(valor)
                    valores.append(valor)
                elif index[x] == 'ESTOQUE':
                    valor = int(valor)
                    valores.append(valor)
                # altera o valor do index caso a entrada seja aceita e adicionada
                x += 1
            except:
                print(f"Valor inválido para {index[x]}! \nPor Favor, verifique novamente o conteúdo de sua entrada!\n")
        return valores 
    
    x = guia_de_cadastro(valores)
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
                cadastrar_produto()
            elif acao == -255:
                print("Obrigado por usar o programa!")
                return False
        except:
            print("Sua entrada foi considerada inválida! Por Favor, tente novamente:")
    #if isinstance(acao, int):
print("\tSeja Bem Vindo, sr. Operador!")
main()
