class personagem:
    def __init__(self, vida, armadura, historia):
        self.vida = vida
        self.armadura = armadura
        self.historia = historia

    def vc_esta_vivo(self):
        if(self.vida>0):
            print("Esta vivo\n")
        else:
            print("Esta morto\n")

class guerreiro(personagem):
    def __init__(self, vida, armadura, historia, ataque):
        super().__init__(vida, armadura, historia)
        self.ataque = ataque

    def corte_rapido(self):
        print(f"Guerreiro tira {self.ataque} pontos de vida do oponente")