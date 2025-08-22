from Classico import classico 
from Aventureiro import aventureiro  
from Heroico import heroico          

acess = False

print("\n" + "═" * 80)
print("---------------OLD DRAGON RPG---------------")
print("═" * 80)

while not acess:
    try:
        esc = int(input("\nESCOLHA UM MODO DE JOGO!\n1- Clássico\n2- Aventureiro\n3- Heróico\nSua escolha: "))
         
        if 1 <= esc <= 3:
            acess = True
        else:
            print("\nERRO! Digite um número entre 1 e 3!")
    except ValueError:
        print("\nERRO! Digite apenas números!")

if esc == 1:
    classico()
elif esc == 2:
    aventureiro()
elif esc == 3:
    heroico()

