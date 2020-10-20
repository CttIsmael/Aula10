def conta_vogal():
    dicionario_vogal ={}
    texto  = str(input()).strip()
    a =e = i= o= u = 0

    for letra in range(len(texto)):
        if texto[letra].lower() in 'aáãà':
            a+=1
        elif texto[letra].lower() in'eéê':
            e+=1
        elif texto[letra].lower() in 'ií':
            i+=1
        elif texto[letra].lower() in 'oóõõ':
            o+=1
        elif texto[letra].lower() in 'uú':
            u+=1

    dicionario_vogal['A']=a
    dicionario_vogal['E']=e
    dicionario_vogal['I']=i
    dicionario_vogal['O']=o
    dicionario_vogal['U']=u

    for v,vl in dicionario_vogal.items():
            print(f'{v}: {vl}')

def main():
    conta_vogal()
    
if __name__=='__main__':
    main()
