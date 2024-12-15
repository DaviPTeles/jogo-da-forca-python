def forca(a):
    if (a==5):
        print("_______ ")
        print("|     | ")
        print("|     O ")
        print("|       ")
        print("|       ")
        print("|       ")
        print("|       ")
    elif(a==4):
        print("_______ ")
        print("|     | ")
        print("|     O ")
        print("|     | ")
        print("|     | ")
        print("|       ")
        print("|       ")
    elif(a==3):
        print("_______ ")
        print("|     | ")
        print("|     O ")
        print("|    /| ")
        print("|     | ")
        print("|       ")
        print("|       ")
    elif(a==2):
        print("_______ ")
        print("|     | ")
        print("|     O ")
        print("|    /|\ ")
        print("|     | ")
        print("|       ")
        print("|       ")
    elif(a==1):
        print("_______ ")
        print("|     | ")
        print("|     O ")
        print("|    /|\ ")
        print("|     | ")
        print("|    /  ")
        print("|       ")
    elif(a==0):
        print("_______ ")
        print("|     | ")
        print("|     O ")
        print("|    /|\ ")
        print("|     | ")
        print("|    / \ ")
        print("|       ")


print('Bem vindo ao Jogo da Forca')

palavra = str(input('Digite a palavra:'))
palavra = palavra.replace(" ", "")
palavra = palavra.lower()
palavra = list(palavra)
palavra_length = len(palavra)
teste = palavra[1]
contador = 0
vida = 6
tentativas = []
for underline in palavra:
        tentativas.append("_")
underlines = " ".join(tentativas)
print(underlines)
while contador<palavra_length and vida>0:
    print(f'Vida: {vida}')
    print('')
    forca(vida)
    tentativa = str(input('Qual a letra?'))
    if tentativa!=palavra[contador]:
        print("você errou")
        vida -= 1
    else:
        print("você acertou")
        tentativas[contador] = tentativa
        resultado = " ".join(tentativas)
        print(resultado)
        contador += 1
        
if contador == palavra_length:
    print("Parabéns, você conseguiu!")

else:
    forca(vida)
    print("Você falhou pela ultima vez!")
