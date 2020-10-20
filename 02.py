def agenda(n):
    agenda = {}    

    for i in range(n):

        nome = input().strip()
        cidade = input().strip()
        estado = input().strip()
        fone = input().strip()

        agenda[i] = nome, cidade, estado, fone      
        
    for nome, cidade, estado, fone in agenda.values():
        esta = f'{cidade}({estado})'
        print("{:24} {:29} {}".format(nome, esta, fone))

    
    
def main():
    n = int(input())
    agenda(n)

if __name__=='__main__':
    main()
