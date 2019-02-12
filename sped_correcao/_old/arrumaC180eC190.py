## Os campos Código da Nomenclatura Comum do Mercosul e Código EX dos registros C180 e C190 devem ser iguais, para o mesmo item.
## O valor do campo deverá ser igual ao valor do campo Código da Nomenclatura Comum do Mercosul do Registro 0200 (conforme tabelas do estabelecimento ou do estabelecimento matriz)
import takeLimit

def exec(conexao):
    cursor = conexao.cursor()

    for i in ["C180","C190"]:
        update = ""
        update = update + " UPDATE principal set "
        update = update + " r6 = (select distinct p.r8 from principal as p where p.r1 = \"0200\" and p.r2 = principal.r5) "
        update = update + " WHERE "
        update = update + " r1 = \"" + i + "\" "
        cursor.execute(update)
        conexao.commit()
        print("REGISTROS " + i + " ARRUMADO NCM")


## ao concertar acima os valores do NCM, pode ocorrer de ter duplicidade de itens no C010, abaixo 
## estes erros são corrigidos

    ## pega a quantidade de C010 que possui o documento
    temp = cursor.execute("select count(*) as t from principal where r1 = \"C010\"")
    qtdC010 = temp.fetchone()[0]

    ## verifica se tem C190 repetido em cada C010
    for i in range(0,qtdC010-1):
        select = ""
        select = select + " SELECT r2,r5,r6,r7,count(*) c "
        select = select + " FROM principal "
        select = select + " where r1 = \"C190\" "
        select = select + " and r0 between (select r0 as c from principal where r1 = \"C010\" order by r0 limit " + str(i) + ",1) "
        select = select + " and (select r0 as c from principal where r1 = \"C010\" order by r0 limit " + str(i+1) + ",1) "
        select = select + " group by r2,r5,r6,r7 "
        select = select + " having count(*) > 1 "
        select = select + " order by r5 "

        temp = cursor.execute(select)
        temp = temp.fetchall()
        ## se não tiver repetido, continua a olhar nos outros C010
        if len(temp) == 0:
            continue

        ## caso tenha C190 repetido é iterado nesses processos para concertar
        for i2 in temp:
            ##/* pega o r0 de todos os C190 repetidos */
            select = ""
            select = select + " SELECT r0 from principal "
            select = select + " where r1 = \"C190\" "
            select = select + "	and r0 between "
            select = select + "	(select r0 as c from principal where r1 = \"C010\" order by r0 limit 0,1) "
            select = select + "	and "
            select = select + "	(select r0 as c from principal where r1 = \"C010\" order by r0 limit 1,1) "
            select = select + "	and "
            select = select + "	r2 = \"" + i2[0] + "\" and r5 = \"" + i2[1] + "\" and r6 = \"" + i2[2] + "\" "
            
            temp = cursor.execute(select)
            temp = temp.fetchall()
            primeiroID = temp[0][0]

            ## coloca na lista todos os dados do C190, no caso os C191 e C195
            lista = []
            for i3 in temp:
                limit = takeLimit.exec(cursor,i3[0],"C190")
                select = ""
                select = select + " SELECT r0,r1,r2,r3,r4,(ROUND(CAST(replace(r5,',','.') AS FLOAT),2)) r5,r6,r7,r8,r9,r10,r11,r12 "
                select = select + " from principal where r0 between " + str(limit[0] + 1) + " and " + str(limit[1])
                temp2 = cursor.execute(select)
                temp2 = temp2.fetchall()
                lista.append(temp2)
            if len(lista) != 1:
                lista1 = lista[0] + lista[1]
                lista = []
                ids = []
                for i3 in lista1:
                    lista.append(i3[1:])
                    ids.append(i3[0])
                lista = list(set(lista))
                ids.append(temp[1][0])

                ## deleta todos os registros para depois inserir os que não são repetidos
                delete = "delete from principal where r0 in (" + ",".join([str(iz) for iz in ids]) + ")"
                cursor.execute(delete)
                conexao.commit()

                ## insere os itens sem repetição e soma ao mesmo tempo o valor total do item
                valor_total = 0
                lista.sort()
                primeiroIDTemp = primeiroID
                for i3 in lista:
                    valor_total = valor_total + i3[4]
                    primeiroIDTemp = primeiroIDTemp + 1
                    stringt = "\",\"".join([str(iz) for iz in i3])
                    insert = ""
                    insert = insert + " INSERT INTO principal(r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12) "
                    insert = insert + " VALUES("
                    insert = insert + str(primeiroIDTemp) + ",\""
                    insert = insert + stringt.replace(".",",")
                    insert = insert + "\")"
                    cursor.execute(insert)
                    conexao.commit()

                ## atualiza valor total do C190
                update = ""
                update = update + " UPDATE principal SET "
                update = update + " r8 = \"" + str(round(valor_total / 2,2)).replace(".",",") +"\""
                update = update + " where r0 = " + str(primeiroID)
                cursor.execute(update)
                conexao.commit()


        #print(select)







    # update = '''
    #     UPDATE principal set 
    #         r6 = (select distinct p.r8 from principal as p where p.r1 = "0200" and p.r2 = principal.r5)
    #     WHERE 
    #         r1 = "C180" 
    # '''
    # cursor.execute(update)
    # conexao.commit()
    # print('REGISTROS C180 ARRUMADO NCM')

    # update = '''
    #     UPDATE principal set
    #         r6 = (select distinct p.r8 from principal as p where p.r1 = "0200" and p.r2 = principal.r5)
    #     WHERE 
    #         r1 = "C190"
    # '''
    # cursor.execute(update)
    # conexao.commit()
    # print('REGISTROS C190 ARRUMADO NCM')

## arrumando a duplicade de dados ao concertar o NCM





# SELECT '0200',a0200.*,'C180',ac180.*
# FROM
# 	(SELECT r2 codprod, r8 ncm, count(*) qtd FROM principal WHERE r1 = "0200" GROUP BY r2,r8 ORDER BY count(*) DESC) a0200,
# 	(SELECT r5 codprod, r6 ncm, count(*) qtd FROM principal WHERE r1 = "C180" GROUP BY r5,r6 ORDER BY count(*) DESC) ac180
# WHERE
# 	a0200.codprod = ac180.codprod AND a0200.ncm <> ac180.ncm

