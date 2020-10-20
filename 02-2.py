from operator import itemgetter

def conta_aparicao(s):
    aparece = {}
    for c in s:
        if c in aparece:
            aparece[c] = aparece[c] + 1
        else:
            aparece[c] = 1
    return aparece
def main():
    lista=[]
    for i in range(1000):
        s = int(input())
        lista.append(s)

    rep = {}   
    rep =conta_aparicao(lista)
    
    ordem_ano=[]
    ordem_ano = sorted(rep.items(), key=itemgetter(0))    
    
    for i in range(len(ordem_ano)):
        print(f'{ordem_ano[i][0]}: {ordem_ano[i][1]}') 
     
    
if __name__=='__main__':
    main()
