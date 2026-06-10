senha_correta = 77

print("AVISO DE SISTEMA\n")
print("Você foi trancado na sala de servidores do CEUB!")
print("Para abrir a porta, acerte a senha numérica de 1 a 100\n")
print("====================\n")

palpite = 0
tentativas = 0

while palpite != senha_correta:
    palpite = int(input("Digite seu palpite: "))
    tentativas = tentativas + 1
    
    if palpite == senha_correta:
        print("VOCÊ ACERTOU A SENHA E A PORTA SE ABRIU!!")
        print("Total de tentavas:", tentativas)
    elif palpite > senha_correta:
        print("ACESSO NEGADO! O numero digitado é muito ALTO.\n")
    else:
        print("ACESSO NEGADO! O numero digitado é muito BAIXO.\n")





