from geral import Personagem


def classe(self, nome_class, habilidades):
    self.classe = nome_class
    self.habilidades_classe = habilidades

def esClasse():  
    habilidades = {
        1: "Aparar, Maestria em arma, Ataque Extra, Todas as Armas, Armaduras",
        2: "Magias Divinas, Afastar Mortos, Cura, Armas Impactantes, Todas as Armaduras, Todos os Itens Mágicos",
        3: "Ataque Furtivo, Ouvir Ruidos, Talentos de Ladrão, Armas Pequenas/Médias, Armaduras Leves",
        4: "Magias Arcanas, Ler Magias, Detectar Magias, Armas Leves, Todos os itens Mágicos"
}
    while True:
            try:
                esc_classe = int(input("Escolha sua CLASSE!\n\n1- Guerreiro\n2- Clérigo \n3-Ladrão \n4- Mago\n\nSua escolha: "))

                if esc_classe < 1 or esc_classe > 4:
                    print("ERRO! Digite um número entre 1 e 4!")
                    continue

                #tratamento para classes
                if esc_classe == 1: #Guerreiro
                    classe_val = "Guerreiro"
                    print(f"\nGuerreiro\nHabilidades: \n{habilidades[esc_classe]}\n")
                    
                elif esc_classe == 2: #Clerigp
                    classe_val = "Clérigo"
                    print(f"\nClérigo\nHabilidades: \n{habilidades[esc_classe]}\n")
                    
                elif esc_classe == 3: #Ladrão
                    classe_val = "Ladrão"
                    print(f"\nLadrão\nHabilidades: \n{habilidades[esc_classe]}\n")
                    
                elif esc_classe == 4: #mago
                    classe_val = "Mago"
                    print(f"\nMago\nHabilidades: \n{habilidades[esc_classe]}\n")

            except ValueError:
                print("ERRO! Digite apenas números!")

            return classe_val, habilidades[esc_classe]