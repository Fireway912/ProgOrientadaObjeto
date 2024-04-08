#Classe recebe um nome
class Newbie:
    def __init__(self, name):
        self.nm = name 
    #Metodo gera uma mensagem demonstracao
    def Greetings(self):
        print(f"Hello World! My name is {self.nm}\n")

#START
eu = Newbie("Adriano")
eu.Greetings()