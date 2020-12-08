class Produto():
    __nome:str
    __quantidade:int
    __valor:float
    __descricao:str
    __peso:float
    __altura:float
    __largura:float
    
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
        
    def get_descricao(self):
        return self.__descricao
    
    def set_descricao(self, descricao:str):
        self.__descricao = descricao      

    def get_peso(self):
        return self.__peso
    
    def set_peso(self, peso:float):
        self.__peso = peso          
        
    def get_altura(self):
        return self.__altura
    
    def set_altura(self, altura:float):
        self.__altura = altura         
        
    def get_largura(self):
        return self.__largura
    
    def set_largura(self, largura:float):
        self.__largura = largura                           
                   
class Categoria():
    __nome:str
    __subcategoria:str

    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome:str):
        self.__nome = nome
        
    def get_subcategoria(self):
        return self.__subcategoria
    
    def set_subcategoria(self, subcategoria:str):
        self.__subcategoria = subcategoria           
