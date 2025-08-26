from geral import Personagem, dado, race, escRaca
from Classes import classe, esClasse

"""
ATRIBUTOS:
FOR = FORÇA;  
DES = DESTREZA;
CON = CONSTITUIÇÃO;
INT = INTELIGÊNCIA;
SAB = SABEDORIA; 
CAR = CARISMA;
"""

def classico():
    print("\n" + "═" * 80)
    print("---------------OLD DRAGON RPG (CLÁSSICO)---------------")
    print("═" * 80)
    print("\nVamos criar seu PERSONAGEM!")
    
    nome = input("\nDigite um nome: ")
    print("\n" + "═" * 80)
    raca_val, mov_val, infra_val, alin_val, hab_val = escRaca()
    class_nome, class_hab = esClasse()

    #classe = raca = input("Escolha sua Raça\n1- Humano\n2- Elfo \n3- Anão\n4- Halfling\n5- Gnomo\n7- Meio-Elfo\nSua escolha: ") 
    
    
    #rola o dado
    forca_val = dado()
    des_val = dado()
    con_val = dado()
    inte_val = dado()
    sab_val = dado()
    car_val = dado()

    #Criando personagem
    personagem = Personagem(
        nome=nome,
        classe= None,
        race = None,
        forca=forca_val,
        des=des_val,
        con=con_val,
        int=inte_val,
        sab=sab_val,
        car=car_val
    )
    
    race(personagem, raca_val, mov_val, infra_val, alin_val, hab_val)
    classe(personagem, class_nome, class_hab)

    #printando informações
    print("\n" + "="*50)
    print("PERSONAGEM CRIADO COM SUCESSO!")
    personagem.printf()
    
    return personagem