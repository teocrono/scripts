## executa regras definidas em um arquivo
import helper

def exec(conexao):

    cursor = conexao.cursor()

    print("Executando Regras",end=' ')
    print('')

    arquivo = open('regras.txt','r')
    regras = arquivo.readlines()
    arquivo.close()

    print('Montando as regras do arquivo')
    while regras:
        if len(regras[0]) == 1:
            regras.pop(0)
            continue

        print('*',end=' ')
        regra = regras.pop(0)[:-1]
        if(regra[0] == '@'):
            continue
        regra = regra.split('***')

        tipo = regra[0].strip()
        tipo = tipo.split('#')

        sett = regra[1].strip()
        sett = sett[2:].split('#')

        where = regra[2].strip()
        where = where[2:].split('#')

        if tipo[0][2] == '1':
            ## monta sql
            update = " UPDATE principal SET "
            update = update + helper.montaSetSql(sett)
            update = update + " WHERE 1=1 "
            update = update + helper.montaWhereSql(where)
            print('-')
            print(update)
            cursor.execute(update)
            conexao.commit()



    print('')
    print("Finalizado")


