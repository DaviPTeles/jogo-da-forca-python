
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

def carregar():
    contador = 0
    while contador<50:
        print('============================')
        contador+=1

print('============================')
print('Bem vindo ao Jogo da Forca')
print('============================')

palavra = str(input('Digite a palavra:'))
carregar()
palavra = palavra.replace(" ", "")
palavra = palavra.lower()
palavra = list(palavra)
contador = 0
vida = 6
tentativas = []
usados = []
for underline in palavra:
        tentativas.append("_")
underlines = " ".join(tentativas)

while vida>0:
    verificacao = "_" in tentativas
    if verificacao==False:
        print("Parabéns, você conseguiu!")
        break
    tentativa = str(input("Digite uma letra: "))
    if tentativa not in usados:
        repeticao = palavra.count(tentativa)
        indices = []
        verificacao = tentativa in palavra
        if verificacao==False:
            vida-=1
        for indice, linha in enumerate(palavra):
            if linha == tentativa:
                indices.append(indice)
                contador = 0
                indices_length = len(indices)
                for linha in indices:
                    tentativas[linha] = tentativa
                    underlines = " ".join(tentativas)
        usados.append(tentativa)
        print('============================')
        print(f'Vida: {vida}')
        print('============================')
        forca(vida) 
        print('')   
        print(f"Estado: {underlines}") 
        print(f"Usados: {usados}") 
    else:
        print('Você já usou esta letra, tente outra!')

if (vida==0):
    print("Você falhou pela ultima vez!")