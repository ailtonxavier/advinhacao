from random import randint

def jogar():

  print("########################################")
  print("### Bem vindo no jogo de Advinhação! ###")
  print("########################################")

  print("\nTente advinhar o número secreto entre 1 e 100...\n")

  numero_secreto = randint(1,100) # define um número aleatório entre 1 e 100.
  total_de_tentativas = 0
  pontos = 1000
  rodada = 1

  nivel = 0
  while nivel != "1" or "2" or "3": # loop até a entrada ser válida

    nivel = input(f"Qual nível de dificuldade?\n(1) Fácil (2) Médio (3) Difícil\nDefina um nível: ").strip()

    if nivel == "1":
      total_de_tentativas = 10
      print("Você selecionou o nível Fácil.\n")
      break
    elif nivel == "2":
      total_de_tentativas = 5
      print("Você selecionou o nível Médio.\n")
      break
    elif nivel == "3":
      total_de_tentativas = 3
      print("Você selecionou o nível Difícil.\n")
      break
    else:
      print("Digite um número válido!\n")

  chute = 0

  for rodada in range(1, total_de_tentativas + 1):

    chute = 0
    
    print(f"Tentativa {rodada} de {total_de_tentativas}.")

    try:
      chute = int(input("Digite um número entre 1 e 100: ").strip())
      print(f"Você digitou {chute}\n")

    except ValueError:
      print("Você precisa digitar um número válido!\n")

    if chute < 1 or chute > 100:
      print("Você deve digitar um número entre 1 e 100")
      continue

    acertou = chute == numero_secreto
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto

    if acertou: # chute igual ao número secreto.
      print(f"Você acertou e fez {pontos} pontos!")
      break
    
    else:
      if chute_maior: # chute maior que número secreto.
        print("Seu chute foi maior que o número secreto")

      elif chute_menor: # chute menor que número secreto.
        print("Seu chute foi menor que o número secreto")
      
      pontos_perdidos = abs(numero_secreto - chute)
      pontos = pontos - pontos_perdidos
  
  print("Fim do jogo")

if(__name__ == "__main__"): # executa funções fora do main, no caso o jogos.py
  jogar()