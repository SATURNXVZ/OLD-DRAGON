import random

class Personagem:
    def __init__(self, nome, classe, forca, des, con, int, sab, car):
        self.nome = nome
        self.classe = classe
        self.forca = forca
        self.destreza = des 
        self.constituicao = con
        self.inteligencia = int
        self.sabedoria = sab
        self.carisma = car 
    
    def printf(self):
        """Mostra todas as informações do personagem"""
        print("\n" + "═" * 80)
        print(f"FICHA DO PERSONAGEM - {self.nome.upper()}")
        print("═" * 80)
        print(f"Classe: {self.classe}")
        print(f"Força: {self.forca}")
        print(f"Destreza: {self.destreza}")
        print(f"Constituição: {self.constituicao}")
        print(f"Inteligência: {self.inteligencia}")
        print(f"Sabedoria: {self.sabedoria}")
        print(f"Carisma: {self.carisma}")
        print("═" * 80)

def dado():
    soma = 0
    for i in range(3):
        numero = random.randint(1, 6)
        #print(f"  Dado {i+1}: {numero}")
        soma += numero
    #print(f"  Total: {soma}")
    return soma
    
