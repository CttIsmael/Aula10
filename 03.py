def cadastro_people():
    maiores={}
    menores={}
    
    for i in range(20):
        nome = input().strip()
        idade = int(input())
        cpf = input().strip()

        maiores[cpf]= nome, idade
    
    for i in maiores:
        nome, idade =maiores[i]
        if idade< 18:
            menores[i] = nome, idade
    for chave in menores:
        if chave in menores.keys():
            if chave in maiores.keys():
                del maiores[chave]
    
    print("========== MAIORES DE 18 ANOS ==========")
    for i in maiores:
        nome, idade = maiores[i]
        print(f'{nome};{idade};{i}')

    print("========== MENORES DE 18 ANOS ==========")
    for i in menores:
        nome, idade = menores[i]
        print(f'{nome};{idade};{i}')
   

def main():
    cadastro_people()

if __name__ == '__main__':
    main()
