from unicodedata import normalize
def remover_acento(txt):
    s = normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')
    return s     

def conta_ocorrencias(s):
    ocorrencias = {}
    for c in s:
        if c in ocorrencias:
                ocorrencias[c] = ocorrencias[c] + 1
        else:
                ocorrencias[c] = 1
    return ocorrencias

def remove_esp(qntdd):
    espaco= {}
    for k,v in qntdd.items():
        if k in (' '',''!''.'';''('')'':''/''-''_''<''>'):
            espaco[k]=v
        
    for crt in espaco:
        if crt in espaco.keys():
            if crt in qntdd.keys():
                del qntdd[crt]        
    return qntdd
            
def main():
    txt = input().upper().strip()
    s_txt =remover_acento(txt)
    qntdd = conta_ocorrencias(s_txt)
    
    print(remove_esp(qntdd))
    
if __name__=='__main__':
    main()
