class Produto:
    __nome:str
    __quantidade:int
    __valor:float
    __categoria:str
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome:str):
        self.__nome = nome
 
    def get_quantidade(self):
        return self.__quantidade
    
    def set_quantidade(self, quantidade:int):
        self.__quantidade = quantidade
        
    def get_valor(self):
        return self.__valor
    
    def set_valor(self, valor:float):
        self.__valor = valor
        
    def get_categoria(self):
        return self.__categoria
    
    def set_categoria(self, categoria:str):
        self.__categoria = categoria                 
       
produtos = {'nome': None, 'quantidade': None, 'valor': None, 'categoria': None}   
list_produtos = [] 
      
def adicionar_produto():
    produtos = {}
    p = Produto()
    p.set_nome(str(input("Digite o nome do Produto: ")))
    p.set_quantidade(int(input("Digite a quantidade do Produto: ")))
    p.set_valor(float(input("Digite o valor do Produto: ")))
    p.set_categoria(str(input("Digite a categoria do Produto: ")))
    produtos['nome'] = p.get_nome()
    produtos['quantidade'] = p.get_quantidade()
    produtos['valor'] = p.get_valor()
    produtos['categoria'] = p.get_categoria()
    list_produtos.append(produtos)
    print('\nProduto Cadastrado')        
 
def remover_produto():
    for i in range(len(list_produtos)):
        print(f'[{i}]. ' + str(list_produtos[i]))
    op = int(input('\nSelecione uma opcao: '))
    del list_produtos[op]
 
def editar_produto():
    for i in range(len(list_produtos)):
        print(f'[{i}]. ' + str(list_produtos[i]))
    op = int(input('\nSelecione uma opcao: '))
    for x in range(len(list_produtos)):
        if op == x:
            list_produtos[op]['nome'] = str(input("Digite o nome do Produto: "))
            list_produtos[op]['quantidade'] = int(input("Digite a quantidade do Produto: "))
            list_produtos[op]['valor'] = float(input("Digite o valor do Produto: "))
            list_produtos[op]['categoria'] = str(input("Digite a categoria do Produto: "))        

def listar_produto ():
    for i in range(len(list_produtos)):
        print(f'[{i}]. ' + str(list_produtos[i]))
   
opcoes = ['Listar Produtos','Cadastrar Produto','Editar Produto', 'Remover produto', 'Sair'] 
op = True

while op:
    print('\n-- MENU --') 
    for ops, opcao in enumerate(opcoes):
        print(f'[{ops+1}] - {opcao}')
    op = int(input('\nSelecione uma opcao: '))
    if op == 1:
        listar_produto()
    elif op == 2:
        adicionar_produto()
    elif op == 3:
        editar_produto()
    elif op == 4:
        remover_produto()
    elif op == 5:
        exit(1) 
    elif op > len(opcoes):
        print('Opcao incorreta, tente novamente! ')