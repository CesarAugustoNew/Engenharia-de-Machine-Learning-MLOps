# palavra = "python"
# acertos = ""
# erradas = ""
# erros = 0
# max_erros = 6

# while erros < max_erros:
#     mostrar = ""
#     venceu = True
#     for letra in palavra:
#         if letra in acertos:
#             mostrar += letra + " "
#         else:
#             mostrar += "_ "
#             venceu = False

#     print()
#     print("Palavra:", mostrar)
#     print("Erradas:", erradas)
#     print("Tentativas restantes:", max_erros - erros)

#     if venceu:
#         print("Parabéns, você venceu!")
#         break

#     letra = input("Digite uma letra: ").lower().strip()

#     if len(letra) != 1 or not letra.isalpha():
#         print("Digite apenas UMA letra.")
#     elif letra in acertos or letra in erradas:
#         print("Você já tentou essa letra!")
#     elif letra in palavra:
#         acertos += letra
#     else:
#         erradas += letra
#         erros += 1

# if erros == max_erros:
#     print("Você perdeu! A palavra era:", palavra)

# for i in range(0, 10):
#   print (i)


# nome = 'cesar augusto da silva'
# for i in nome:
#   print(i)

# for i in range (16):
#   print(15 - i)


# for i in range (9):
#   print(27 + i)


