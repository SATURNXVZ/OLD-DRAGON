import random

class Personagem:
    def __init__(self, nome, classe, race, forca, des, con, int, sab, car):
        self.nome = nome
        self.classe = classe
        self.race = race
        self.forca = forca
        self.destreza = des 
        self.constituicao = con
        self.inteligencia = int
        self.sabedoria = sab
        self.carisma = car 
    
    def printf(self):
        #Mostra todas as informações do personagem
        print("\n" + "═" * 80)
        print(f"FICHA DO PERSONAGEM - {self.nome.upper()}")
        print("═" * 80)
        print(f"Raça: {self.race}")
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
    
def race(self, raca, mov, infra, alin, habilidades): #movimento, infravisão, alinhamento
    self.race = raca
    self.mov = mov
    self.infra = infra
    self.alin = alin
    self.habilidade = habilidades

def escRaca(): 
    habilidades = {
    1: "Aprendizado e Adaptabilidade",
    2: "Percepção, Graciosos, Arte Marcial do Arco e Imunidades",
    3: "Mineradores, Vigoroso, Armas Grandes e Inimigos",
    4: "Furtivos, Destemidos, Bons de Mira, Pequenos e Armas Pequenas/Médias",
    5: "Avaliadores, Sagazes, Vigorosos e Restritos",
    6: "Aprendizado, Gracioso, Vigoroso, Idioma extra e Imunidades"
}
 
    while True:
            try:
                esc_race = int(input("Escolha sua Raça!\n\n1- Humano\n2- Elfo \n3- Anão\n4- Halfling\n5- Gnomo\n6- Meio-Elfo\n\nSua escolha: "))

                if esc_race < 1 or esc_race > 6:
                    print("ERRO! Digite um número entre 1 e 6!")
                    continue
                
                #tratamento para as raçcs
                if esc_race == 1: #humano
                    raca_val = "Humano"
                    mov_val = 9
                    infra_val = 0
                    alin_val = "Neutro"
                    print(f"\nHumano:\nOs mais Comuns, Versáteis e Adaptáveis Aventureiros!\n\nMovimentação: {mov_val}\nInfravisão: Nenhuma!\nAlinhamento de personalidade: Qualquer uma!\nHabilidades: {habilidades[esc_race]}\n")
                    
                elif esc_race == 2: #Elfo
                    raca_val = "Elfo"
                    mov_val = 9
                    infra_val = 18
                    alin_val = "Neutro"
                    print(f"\nElfo:\nMisteriosos, Longevos e Graciosos habitantes das Florestas!\n\nMovimentação: {mov_val} metros!\nInfravisão: {infra_val} metros!\nAlinhamento de personalidade: {alin_val}\nHabilidades: {habilidades[esc_race]}\n")
                    
                elif esc_race == 3: #Anão
                    raca_val = "Anão"
                    mov_val = 6
                    infra_val = 18
                    alin_val = "Bondoso"
                    print(f"\nAnão:\nOrgulhosos Habitantes dos Salões sob a Montanha!\n\nMovimentação: {mov_val} metros!\nInfravisão: {infra_val} metros!\nAlinhamento de personalidade: {alin_val}\nHabilidades: {habilidades[esc_race]}\n")
                    
                elif esc_race == 4: #Halfling
                    raca_val = "Halfling"
                    mov_val = 6
                    infra_val = 0
                    alin_val = "Neutro"
                    print(f"\nHalfling:\nOs mais Perspicazes e Curiosos Aventureiros!\n\nMovimentação: {mov_val} metros!\nInfravisão: nenhuma!\nAlinhamento de personalidade: {alin_val}\nHabilidades: {habilidades[esc_race]}\n")
                    
                elif esc_race == 5: # Gnomo
                    raca_val = "Gnomo"
                    mov_val = 6
                    infra_val = 18
                    alin_val = "Neutro"
                    print(f"\nGnomo:\nPequeno inventor mágico, curioso e engenhoso!\n\nMovimentação: {mov_val} metros!\nInfravisão: {infra_val}!\nAlinhamento de personalidade: {alin_val}\nHabilidades: {habilidades[esc_race]}\n")
                    
                elif esc_race == 6: #Meioelfo
                    raca_val = "Meio-Elfo"
                    mov_val = 9
                    infra_val = 9
                    alin_val = "Maldoso"
                    print(f"\nMeio-Elfo:\nRebelde errante, desafiando regras e destinos!\n\nMovimentação: {mov_val} metros!\nInfravisão: {infra_val}!\nAlinhamento de personalidade: {alin_val}\nHabilidades: {habilidades[esc_race]}\n")
                    

            except ValueError:
                print("ERRO! Digite apenas números!")

            return raca_val, mov_val, infra_val, alin_val, habilidades[esc_race]
        