def hexadecimal():
    hexCaracteres = "0123456789abcdef" #variavel com todos os caracteres hexadecimais
    hex = "" #variavel para armazenar o valor do numero hexadecimal
    numDec = int(input("digite um numero: ")) #pede ao usuario para inserir o valor que será convertido

    while numDec > 0: #enquanto o numero inserido for maior que zero, o programa vai ficar dentro do loop
        divisaoResto = numDec % 16 #assim como na conversão que fazemos na mão, o programa vai dividir o numero decimal por 16 até dar 0
        hex = hexCaracteres[divisaoResto] + hex #adiciona o trecho correspondente da variavel hexCaracteres na variavel que armazena o numero hexadecimal
        numDec //= 16 #divide o numero decimal para calcular o proximo digito hexadecimal

    if numDec == "":
        hex = "0"

    return hex
def binario():
    numDec = int(input("digite um numero: "))
    binario = ""
    while numDec > 0:
        divisaoResto = numDec % 2 #divide por 2 e armazena o resto da divisão
        binario = str(divisaoResto) + binario #armazena e adiciona o resto das divisões
        numDec //= 2 #divide por 2 e volta pra condição while

    if binario == "":
        binario = "0"
    return binario
def octadecimal():
    numDec = int(input("digite um numero: "))
    octal = ""
    while numDec > 0:
        divisaoResto = numDec % 8
        octal = str(divisaoResto) + octal
        numDec //= 8

    if octal == "":
        octal = "0"
    return octal

#converter
def converter():
    while True:
        print("Escolha uma base para converter:\n")
        base = input("1 - Hexadecimal\n2 - Binário\n3 - Octadecimal\n4 - Voltar para o menu\n")
        if base == "1":
            print("hexadecimal: ",hexadecimal())
        elif base == "2":
            print("binario", binario())
        elif base == "3":
            print("octadecimal", octadecimal())
        elif base == "4":
            break
        else:
            print("Comando Inválido!\n")
def dadosProjeto():
    print("aluno: luizinho\n(pula linha")

def main():
    print("Seja bem vindo. Escolha uma das opções abaixo:")
    while True:
        resp=(input("1 - Converter\n2 - Dados do projeto\n3 - Sair\n"))
        if resp == "1":
            converter()
        elif resp == "2":
            dadosProjeto()
        elif resp == "3":
            print("Fim de programa!")
            break
        else:
            print("Comando Inválido!")
            main()
main()
