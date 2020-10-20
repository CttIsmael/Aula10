def lancamento_dado():
    dado = {}
    cont =0
    f1 = f2 = f3 = f4 = f5 =f6 =0
    while True:
        face = int(input())
        if face == 0:
            break
        else:
            cont +=1
            if face == 1:
                f1+=1
            elif face == 2:
                f2 +=1
            elif face ==3:
                f3 +=1
            elif face == 4:
                f4 +=1
            elif face ==5:
                f5 +=1
            elif face == 6:
                f6 +=1

    dado[1]= f1
    dado[2]= f2
    dado[3]= f3
    dado[4]= f4
    dado[5]= f5
    dado[6]= f6

    return cont, dado

def main():
    lance, dado = lancamento_dado()   
    print(f'O dado foi lançado {lance} vezes.')
    for k, v in dado.items():
        print(f'A face {k} saiu {v} vezes.')

if __name__=='__main__':
    main()
