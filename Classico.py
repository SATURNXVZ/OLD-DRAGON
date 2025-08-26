from geral import Personagem, dado

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
    print("\n\n\n------ OLD DRAGON RPG (CLASSICO) ------")
    print("\nVamos criar seu PERSONAGEM!")
    
    nome = input("\nDigite um nome: ")
    classe = input("Digite a classe: ") #CLASSE APENAS COMO DEMONSTRAÇÃO
    
    #sorteia
    print("\nRolando atributos...")
    print("Força:")
    forca_val = dado()
    print("Destreza:")
    des_val = dado()
    print("Constituição:")
    con_val = dado()
    print("Inteligência:")
    inte_val = dado()
    print("Sabedoria:")
    sab_val = dado()
    print("Carisma:")
    car_val = dado()
    
    #Criando personagem
    personagem = Personagem(
        nome=nome,
        classe=classe,
        forca=forca_val,
        des=des_val,
        con=con_val,
        int=inte_val,
        sab=sab_val,
        car=car_val
    )
    
    #printando informações
    print("\n" + "="*50)
    print("PERSONAGEM CRIADO COM SUCESSO!")
    personagem.printf()
    
    return personagem
