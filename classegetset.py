class Age: 
    def __init__(self, idade = 0): 
         self._idade = idade 
      
    
    def get_idade(self): 
        return self._idade 
      
    
    def set_idade(self, x): 
        self._idade = x 
  
var = Age() 
var.set_idade(20) 
print(var.get_idade()) 
  
print(var._idade)

