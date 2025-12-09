print("-" * 30)
print("JO-KEN-PÔ".center(30))
print("-" * 30)

from random import randint
from time import sleep

while True:
    itens = ["Pedra","Papel","Tesoura"]
    computador = randint(0,2)

    print("""> Escolha:
-------------------
 [0] Pedra
 [1] Papel
 [2] Tesoura
-------------------""")

    jogador = int(input("> Sua escolha: "))
    if jogador < 0 or jogador > 2:
        print(">>> ❌ Comando Inválido! Tente novamente.")
        print("-------------------")
        continue

    else:
        print("JO")
        sleep(0.5)
        print("KEN")
        sleep(0.5)
        print("PO!!!")

    print("-" * 30)
    print(f"Computador jogou: {itens[computador]}")
    print(f"Você jogou: {itens[jogador]}")
    print("-" * 30)

    if computador == 0:
        if jogador == 0:
            print("⚖️ Houve um EMPATE! ⚖️")

        elif jogador == 1:
            print("🎉 PARABÉNS, VOCÊ VENCEU!!! 🎉")

        elif jogador == 2:
            print("🖥️ Computador VENCEU! 🖥️")

    elif computador == 1:
        if jogador == 0:
            print("🖥️ Computador VENCEU! 🖥️")

        elif jogador == 1:
            print("⚖️ Houve um EMPATE! ⚖️")

        elif jogador == 2:
            print("🎉 PARABÉNS, VOCÊ VENCEU!!! 🎉")

    elif computador == 2:  
        if jogador == 0:
            print("🎉 PARABÉNS, VOCÊ VENCEU!!! 🎉")
        elif jogador == 1:
            print("🖥️ Computador VENCEU! 🖥️")
        elif jogador == 2:
            print("⚖️ Houve um EMPATE! ⚖️")

    continuar = " "
    while continuar not in "SN":
        print("-" * 30)
        continuar = str(input("> Deseja continuar ? [S/N]: ")).strip().upper()
        if continuar not in "SN":
            print(">> ❌ Letra inválida. Tente S ou N.")

    if continuar == "N":
        print("-" * 30)
        print("> Programa Finalizado. ✅")
        print("> Obrigado por jogar! 😄")
        break












