from geral import Personagem, dado

def heroico():
    print("\n" + "═" * 80)
    print("------ OLD DRAGON RPG (HERÓICO) ------")
    print("═" * 80)

    print("\nVamos criar seu PERSONAGEM!")
    
    nome = input("\nDigite um nome: ")
    classe = input("Digite a classe: ")
    
    # Inicializando atributos
    atributos = {
        'forca': None,
        'destreza': None,
        'constituicao': None,
        'inteligencia': None,
        'sabedoria': None,
        'carisma': None
    }
    
    atributos_escolhidos = []
    
    print("\nRolando 7 vezes 3d6 (modo heróico)...")
    
    # Rola a função dado() 7 vezes (cada uma rola 3d6 e soma)
    resultados = []
    for i in range(7):
        resultado = dado()  # Cada chamada rola 3d6 e retorna a soma
        resultados.append(resultado)
        print(f"Rolagem {i+1}: {resultado}")
    
    print(f"\n🎲 Resultados: {resultados}")
    
    # Loop para os 6 atributos
    while len(atributos_escolhidos) < 6:
        # Mostrar resultados disponíveis
        print(f"\nResultados disponíveis: {resultados}")
        
        # Mostrar opções de atributos disponíveis
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
        
        # Validar escolha do atributo
        while True:
            try:
                esc_atributo = int(input("\nEscolha um atributo (1-6): "))
                if esc_atributo < 1 or esc_atributo > 6:
                    print("ERRO! Digite um número entre 1 e 6!")
                    continue
                
                # Verificar se o atributo já foi escolhido
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
        
        # Escolher qual resultado usar para este atributo
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
        
        # Remover o resultado escolhido da lista
        resultados.remove(esc_resultado)
        
        # Atribuir valor ao atributo escolhido
        if esc_atributo == 1:
            atributos['forca'] = esc_resultado
            print(f"✅ Força definida como: {esc_resultado}")
        elif esc_atributo == 2:
            atributos['destreza'] = esc_resultado
            print(f"✅ Destreza definida como: {esc_resultado}")
        elif esc_atributo == 3:
            atributos['constituicao'] = esc_resultado
            print(f"✅ Constituição definida como: {esc_resultado}")
        elif esc_atributo == 4:
            atributos['inteligencia'] = esc_resultado
            print(f"✅ Inteligência definida como: {esc_resultado}")
        elif esc_atributo == 5:
            atributos['sabedoria'] = esc_resultado
            print(f"✅ Sabedoria definida como: {esc_resultado}")
        elif esc_atributo == 6:
            atributos['carisma'] = esc_resultado
            print(f"✅ Carisma definida como: {esc_resultado}")
        
        atributos_escolhidos.append(esc_atributo)
    
    # Criando personagem
    personagem = Personagem(
        nome=nome,
        classe=classe,
        forca=atributos['forca'],
        des=atributos['destreza'],
        con=atributos['constituicao'],
        int=atributos['inteligencia'],
        sab=atributos['sabedoria'],
        car=atributos['carisma']
    )
    
    # Mostrando ficha
    print("\n" + "═" * 80)
    print("🎉 PERSONAGEM HERÓICO CRIADO COM SUCESSO!")
    personagem.printf()
    
    return personagem