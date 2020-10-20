def media(dicionario):
    media =0  
    while True:
        chave = input().strip()
        if chave =='':
            break
        if chave in dicionario.keys():
            for nome, n1, n2 in dicionario.values():
                nome, n1, n2 = dicionario[chave]
                media = (n1+n2)/2
        print(f'{nome}: {media:.1f}')    

def main():
    dic_notas= {}
    while True:
        matricula = input().strip()
        if matricula == '':
            break
        nome = input().strip()
        nota1 = float(input())
        nota2 = float(input())

        dic_notas[matricula] = nome,nota1,nota2

    media(dic_notas)

if __name__=='__main__':
    main()
