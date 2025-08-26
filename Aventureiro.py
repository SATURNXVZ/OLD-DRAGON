from geral import Personagem, dado, escRaca, race
from Classes import esClasse, classe

def aventureiro(): 
    print("\n" + "═" * 80)
    print("---------------OLD DRAGON RPG (AVENTUREIRO)---------------")
    print("═" * 80)
    print("\nVamos criar seu PERSONAGEM!")
    
    nome = input("\nDigite um nome: ")
    print("\n" + "═" * 80)
    
    raca_val, mov_val, infra_val, alin_val, hab_val = escRaca()
    class_nome, class_hab = esClasse()
    
    # Inicializa
    atributos = {
        'forca': None,
        'destreza': None,
        'constituicao': None,
        'inteligencia': None,
        'sabedoria': None,
        'carisma': None
    }
    
    atributos_escolhidos = []
    
    print("\n" + "═" * 80)
    
    while len(atributos_escolhidos) < 6:
        soma = dado()
        print(f"\n Você tirou: {soma}")
        
        # Mostra opção disponíveis
        print("\nAtributos disponíveis:")
        opcoes = []
        if atributos['forca'] is None:
            opcoes.append("1- Força")
        if atributos['destreza'] is None:
            opcoes.append("2- Destreza")
        if atributos['constituicao'] is None:
            opcoes.append("3- Constituição")
        if atributos['inteligencia'] is None:
            opcoes.append("4- Inteligência")
        if atributos['sabedoria'] is None:
            opcoes.append("5- Sabedoria")
        if atributos['carisma'] is None:
            opcoes.append("6- Carisma")
        
        for opcao in opcoes:
            print(f"  {opcao}")
        
        # Validar escolha
        while True:
            try:
                esc = int(input("\nEscolha um atributo (1-6): "))
                if esc < 1 or esc > 6:
                    print("ERRO! Digite um número entre 1 e 6!")
                    continue
                
                # Verifica se o atributo já foi esclhido
                if esc == 1 and atributos['forca'] is not None:
                    print("Força já foi escolhida!")
                    continue
                elif esc == 2 and atributos['destreza'] is not None:
                    print("Destreza já foi escolhida!")
                    continue
                elif esc == 3 and atributos['constituicao'] is not None:
                    print("Constituição já foi escolhida!")
                    continue
                elif esc == 4 and atributos['inteligencia'] is not None:
                    print("Inteligência já foi escolhida!")
                    continue
                elif esc == 5 and atributos['sabedoria'] is not None:
                    print("Sabedoria já foi escolhida!")
                    continue
                elif esc == 6 and atributos['carisma'] is not None:
                    print("Carisma já foi escolhida!")
                    continue
                
                break
                
            except ValueError:
                print("ERRO! Digite apenas números!")
        
        # Atribui valor
        if esc == 1:
            atributos['forca'] = soma
            print(f" Força definida como: {soma}")
        elif esc == 2:
            atributos['destreza'] = soma
            print(f"Destreza definida como: {soma}")
        elif esc == 3:
            atributos['constituicao'] = soma
            print(f"Constituição definida como: {soma}")
        elif esc == 4:
            atributos['inteligencia'] = soma
            print(f"Inteligência definida como: {soma}")
        elif esc == 5:
            atributos['sabedoria'] = soma
            print(f"Sabedoria definida como: {soma}")
        elif esc == 6:
            atributos['carisma'] = soma
            print(f"Carisma definida como: {soma}")
        
        atributos_escolhidos.append(esc)
    
    # Criando personagem
    personagem = Personagem(
        nome=nome,
        classe= None,
        race = None,
        forca=atributos['forca'],
        des=atributos['destreza'],
        con=atributos['constituicao'],
        int=atributos['inteligencia'],
        sab=atributos['sabedoria'],
        car=atributos['carisma']
    )
    
    race(personagem, raca_val, mov_val, infra_val, alin_val, hab_val)
    classe(personagem, class_nome, class_hab)


    # Mostrando ficha
    print("\n" + "═" * 80)
    print(" PERSONAGEM CRIADO COM SUCESSO!")
    personagem.printf()
    
    return personagem