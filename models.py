class Produto():
    __nome:str
    __quantidade:int
    __valor:float
    __descricao:str
    
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
