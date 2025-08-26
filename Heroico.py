from geral import Personagem, dado, race, escRaca
from Classes import esClasse, classe

def heroico():
    print("\n" + "═" * 80)
    print("------ OLD DRAGON RPG (HERÓICO) ------")
    print("═" * 80)

    print("\nVamos criar seu PERSONAGEM!")
    
    nome = input("\nDigite um nome: ")
    print("\n" + "═" * 80)

    raca_val, mov_val, infra_val, alin_val, hab_val = escRaca()
    class_nome, class_hab = esClasse()

    #classe = input("Digite a classe: ")
    
    atributos = {
        'forca': None,
        'destreza': None,
        'constituicao': None,
        'inteligencia': None,
        'sabedoria': None,
        'carisma': None
    }
    
    atributos_escolhidos = []
    
    resultados = []
    for i in range(7):
        resultado = dado()  # Cada vez pega 3 dados e retorna a soma
        resultados.append(resultado)
        print(f"Rolagem {i+1}: {resultado}")
    
    print(f"\n Resultados: {resultados}")
    
    while len(atributos_escolhidos) < 6:
        print(f"\nResultados disponíveis: {resultados}")
        
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
        
        #valida escolha do atributo
        while True:
            try:
                esc_atributo = int(input("\nEscolha um atributo (1-6): "))
                if esc_atributo < 1 or esc_atributo > 6:
                    print("ERRO! Digite um número entre 1 e 6!")
                    continue
                
                #trata se o usuario digitar atributo que ja foi
                if esc_atributo == 1 and atributos['forca'] is not None:
                    print("Força já foi escolhida!")
                    continue
                elif esc_atributo == 2 and atributos['destreza'] is not None:
                    print("Destreza já foi escolhida!")
                    continue
                elif esc_atributo == 3 and atributos['constituicao'] is not None:
                    print("Constituição já foi escolhida!")
                    continue
                elif esc_atributo == 4 and atributos['inteligencia'] is not None:
                    print("Inteligência já foi escolhida!")
                    continue
                elif esc_atributo == 5 and atributos['sabedoria'] is not None:
                    print("Sabedoria já foi escolhida!")
                    continue
                elif esc_atributo == 6 and atributos['carisma'] is not None:
                    print("Carisma já foi escolhida!")
                    continue
                
                break
                
            except ValueError:
                print("ERRO! Digite apenas números!")
        
        print(f"\nResultados disponíveis: {resultados}")
        while True:
            try:
                esc_resultado = int(input("Escolha qual resultado usar (digite o número): "))
                if esc_resultado not in resultados:
                    print("ERRO! Escolha um resultado da lista!")
                    continue
                break
            except ValueError:
                print("ERRO! Digite apenas números!")
        
        resultados.remove(esc_resultado)
        
        if esc_atributo == 1:
            atributos['forca'] = esc_resultado
            print(f"Força definida como: {esc_resultado}")
        elif esc_atributo == 2:
            atributos['destreza'] = esc_resultado
            print(f"Destreza definida como: {esc_resultado}")
        elif esc_atributo == 3:
            atributos['constituicao'] = esc_resultado
            print(f"Constituição definida como: {esc_resultado}")
        elif esc_atributo == 4:
            atributos['inteligencia'] = esc_resultado
            print(f"Inteligência definida como: {esc_resultado}")
        elif esc_atributo == 5:
            atributos['sabedoria'] = esc_resultado
            print(f"Sabedoria definida como: {esc_resultado}")
        elif esc_atributo == 6:
            atributos['carisma'] = esc_resultado
            print(f"Carisma definida como: {esc_resultado}")
        
        atributos_escolhidos.append(esc_atributo)
    
    personagem = Personagem(
        nome=nome,
        classe=None,
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

    
    print("\n" + "═" * 80)
    print("PERSONAGEM HERÓICO CRIADO COM SUCESSO!")
    personagem.printf()
    
    return personagem