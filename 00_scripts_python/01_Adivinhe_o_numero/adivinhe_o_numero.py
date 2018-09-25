from random import randint
numero = int(randint(1, 9))
palpite = 0
tentativas = 0

print("Chute um número inteiro de 1 a 9.")
while palpite != numero:
    palpite = int(input("Seu palpite: "))
    tentativas += 1
    if palpite == numero:
        print ("Acertou em {} tentativas!!!" .format(tentativas))
    elif palpite < numero:
        print("Chute um valor MAIOR!")
    else:
        print("Chute um valor MENOR")
print("Fim do jogo")
