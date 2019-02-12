## arrumando a duplicidade no 191 e 195 e também no 181 e 185
## ocorre quando estão repetidos os campos
## cpf_cnpj - cst - cfop - aliq-pis - quant - cta


def exec(conexao):

    cursor = conexao.cursor()

    print("RULE 14 - Inicializando",end=' ')

    select = " select r0 from principal where r1 = \"C190\" "
    select = cursor.execute(select)
    rselect = select.fetchall()
    rselect = [i[0] for i in rselect]
    if(len(rselect) != 0):
        rselect.append(rselect[len(rselect)-1] + 1000)

        n2 = rselect.pop(0)
        while len(rselect) > 0:
            n1 = n2
            n2 = rselect.pop(0)

            select = "select count(*) from principal where 1=1 "
            select = select + " AND r1 = \"C191\" "
            select = select + " AND r0 between " + str(n1) + " AND " + str(n2) + " "
            select = cursor.execute(select)
            qtd_all = select.fetchone()[0]

            select = " select count(*) from "
            select = select + " (select count(*) from principal where 1=1 "
            select = select + " AND r1 = \"C191\" "
            select = select + " AND r0 between " + str(n1) + " AND " + str(n2) + " "
            select = select + " group by r2,r3,r4,r8,r10,r12) "
            select = cursor.execute(select)
            qtd_group = select.fetchone()[0]

            if qtd_all != qtd_group:
                print('-',end=' ')
                select = " select r0 from principal where 1=1 "
                select = select + " AND r1 = \"C191\" "
                select = select + " AND r0 between " + str(n1) + " AND " + str(n2) + " "
                select = cursor.execute(select)
                to_delete = select.fetchall()
                to_delete = [i[0] for i in to_delete]

                itens = " SELECT r1,r2,r3,r4, "
                itens = itens + " REPLACE(CAST(  SUM(CAST(replace(r5,',','.') AS FLOAT))  AS TEXT),'.',',') r5, "
                itens = itens + " REPLACE(CAST(  SUM(CAST(replace(r6,',','.') AS FLOAT))  AS TEXT),'.',',') r6, "
                itens = itens + " REPLACE(CAST(  SUM(CAST(replace(r7,',','.') AS FLOAT))  AS TEXT),'.',',') r7, "
                itens = itens + " r8,r9,r10, "
                itens = itens + " REPLACE(CAST(  SUM(CAST(replace(r11,',','.') AS FLOAT))  AS TEXT),'.',',') r11, "
                itens = itens + " r12 "
                itens = itens + " FROM principal "
                itens = itens + " WHERE r1 = \"C191\" "
                itens = itens + " AND r0 between " + str(n1) + " AND " + str(n2) + " "
                itens = itens + " GROUP BY r1,r2,r3,r4,r8,r9,r10,r12 "
                itens = cursor.execute(itens)
                itens = itens.fetchall()

                ## deleta todos os itens r0
                delete = "delete from principal where r0 in (" + ",".join([str(i) for i in to_delete]) + ")"
                cursor.execute(delete)
                conexao.commit()
                ## inserir os novos dados com os ids livres
                for i in range(0,len(itens)):
                    data = str(to_delete[i]) + ',"' + "\",\"".join(itens[i]) + '"'
                    insert = " INSERT INTO principal(r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12) "
                    insert = insert + " VALUES( "
                    insert = insert + str(to_delete[i]) + ',"' + "\",\"".join(itens[i]) + '"'
                    insert = insert + " ) "
                    cursor.execute(insert)
                    conexao.commit()


    select = " select r0 from principal where r1 = \"C190\" "
    select = cursor.execute(select)
    rselect = select.fetchall()
    rselect = [i[0] for i in rselect]
    if(len(rselect) != 0):
        rselect.append(rselect[len(rselect)-1] + 1000)

        n2 = rselect.pop(0)
        while len(rselect) > 0:
            print('-',end=' ')
            n1 = n2
            n2 = rselect.pop(0)

            select = "select count(*) from principal where 1=1 "
            select = select + " AND r1 = \"C195\" "
            select = select + " AND r0 between " + str(n1) + " AND " + str(n2) + " "
            select = cursor.execute(select)
            qtd_all = select.fetchone()[0]

            select = " select count(*) from "
            select = select + " (select count(*) from principal where 1=1 "
            select = select + " AND r1 = \"C195\" "
            select = select + " AND r0 between " + str(n1) + " AND " + str(n2) + " "
            select = select + " group by r2,r3,r4,r8,r10,r12) "
            select = cursor.execute(select)
            qtd_group = select.fetchone()[0]

            if qtd_all != qtd_group:
                print('-',end=' ')
                select = " select r0 from principal where 1=1 "
                select = select + " AND r1 = \"C195\" "
                select = select + " AND r0 between " + str(n1) + " AND " + str(n2) + " "
                select = cursor.execute(select)
                to_delete = select.fetchall()
                to_delete = [i[0] for i in to_delete]

                itens = " SELECT r1,r2,r3,r4, "
                itens = itens + " REPLACE(CAST(  SUM(CAST(replace(r5,',','.') AS FLOAT))  AS TEXT),'.',',') r5, "
                itens = itens + " REPLACE(CAST(  SUM(CAST(replace(r6,',','.') AS FLOAT))  AS TEXT),'.',',') r6, "
                itens = itens + " REPLACE(CAST(  SUM(CAST(replace(r7,',','.') AS FLOAT))  AS TEXT),'.',',') r7, "
                itens = itens + " r8,r9,r10, "
                itens = itens + " REPLACE(CAST(  SUM(CAST(replace(r11,',','.') AS FLOAT))  AS TEXT),'.',',') r11, "
                itens = itens + " r12 "
                itens = itens + " FROM principal "
                itens = itens + " WHERE r1 = \"C195\" "
                itens = itens + " AND r0 between " + str(n1) + " AND " + str(n2) + " "
                itens = itens + " GROUP BY r1,r2,r3,r4,r8,r9,r10,r12 "
                itens = cursor.execute(itens)
                itens = itens.fetchall()

                ## deleta todos os itens r0
                delete = "delete from principal where r0 in (" + ",".join([str(i) for i in to_delete]) + ")"
                cursor.execute(delete)
                conexao.commit()
                ## inserir os novos dados com os ids livres
                for i in range(0,len(itens)):
                    data = str(to_delete[i]) + ',"' + "\",\"".join(itens[i]) + '"'
                    insert = " INSERT INTO principal(r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12) "
                    insert = insert + " VALUES( "
                    insert = insert + str(to_delete[i]) + ',"' + "\",\"".join(itens[i]) + '"'
                    insert = insert + " ) "
                    cursor.execute(insert)
                    conexao.commit()



    print("RULE 20 - Inicializando",end=' ')

    select = " select r0 from principal where r1 = \"C180\" "
    select = cursor.execute(select)
    rselect = select.fetchall()
    rselect = [i[0] for i in rselect]
    if(len(rselect) != 0):
        rselect.append(rselect[len(rselect)-1] + 1000)

        n2 = rselect.pop(0)
        while len(rselect) > 0:
            n1 = n2
            n2 = rselect.pop(0)

            select = "select count(*) from principal where 1=1 "
            select = select + " AND r1 = \"C181\" "
            select = select + " AND r0 between " + str(n1) + " AND " + str(n2) + " "
            select = cursor.execute(select)
            qtd_all = select.fetchone()[0]

            select = " select count(*) from "
            select = select + " (select count(*) from principal where 1=1 "
            select = select + " AND r1 = \"C181\" "
            select = select + " AND r0 between " + str(n1) + " AND " + str(n2) + " "
            select = select + " group by r2,r3,r7,r9,r11) "
            select = cursor.execute(select)
            qtd_group = select.fetchone()[0]

            if qtd_all != qtd_group:
                print('-',end=' ')
                select = " select r0 from principal where 1=1 "
                select = select + " AND r1 = \"C181\" "
                select = select + " AND r0 between " + str(n1) + " AND " + str(n2) + " "
                select = cursor.execute(select)
                to_delete = select.fetchall()
                to_delete = [i[0] for i in to_delete]

                itens = " SELECT r1,r2,r3, "
                itens = itens + " REPLACE(CAST(  SUM(CAST(replace(r4,',','.') AS FLOAT))  AS TEXT),'.',',') r4, "
                itens = itens + " REPLACE(CAST(  SUM(CAST(replace(r5,',','.') AS FLOAT))  AS TEXT),'.',',') r5, "
                itens = itens + " REPLACE(CAST(  SUM(CAST(replace(r6,',','.') AS FLOAT))  AS TEXT),'.',',') r6, "
                itens = itens + " r7,r8,r9, "
                itens = itens + " REPLACE(CAST(  SUM(CAST(replace(r10,',','.') AS FLOAT))  AS TEXT),'.',',') r10, "
                itens = itens + " r11 "
                itens = itens + " FROM principal "
                itens = itens + " WHERE r1 = \"C181\" "
                itens = itens + " AND r0 between " + str(n1) + " AND " + str(n2) + " "
                itens = itens + " GROUP BY r1,r2,r3,r7,r8,r9,r11 "
                itens = cursor.execute(itens)
                itens = itens.fetchall()

                ## deleta todos os itens r0
                delete = "delete from principal where r0 in (" + ",".join([str(i) for i in to_delete]) + ")"
                cursor.execute(delete)
                conexao.commit()
                ## inserir os novos dados com os ids livres
                for i in range(0,len(itens)):
                    data = str(to_delete[i]) + ',"' + "\",\"".join(itens[i]) + '"'
                    insert = " INSERT INTO principal(r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11) "
                    insert = insert + " VALUES( "
                    insert = insert + str(to_delete[i]) + ',"' + "\",\"".join(itens[i]) + '"'
                    insert = insert + " ) "
                    cursor.execute(insert)
                    conexao.commit()


    select = " select r0 from principal where r1 = \"C180\" "
    select = cursor.execute(select)
    rselect = select.fetchall()
    rselect = [i[0] for i in rselect]
    if(len(rselect) != 0):
        rselect.append(rselect[len(rselect)-1] + 1000)

        n2 = rselect.pop(0)
        while len(rselect) > 0:
            n1 = n2
            n2 = rselect.pop(0)

            select = "select count(*) from principal where 1=1 "
            select = select + " AND r1 = \"C185\" "
            select = select + " AND r0 between " + str(n1) + " AND " + str(n2) + " "
            select = cursor.execute(select)
            qtd_all = select.fetchone()[0]

            select = " select count(*) from "
            select = select + " (select count(*) from principal where 1=1 "
            select = select + " AND r1 = \"C185\" "
            select = select + " AND r0 between " + str(n1) + " AND " + str(n2) + " "
            select = select + " group by r2,r3,r7,r9,r11) "
            select = cursor.execute(select)
            qtd_group = select.fetchone()[0]

            if qtd_all != qtd_group:
                print('-',end=' ')
                select = " select r0 from principal where 1=1 "
                select = select + " AND r1 = \"C185\" "
                select = select + " AND r0 between " + str(n1) + " AND " + str(n2) + " "
                select = cursor.execute(select)
                to_delete = select.fetchall()
                to_delete = [i[0] for i in to_delete]

                itens = " SELECT r1,r2,r3, "
                itens = itens + " REPLACE(CAST(  SUM(CAST(replace(r4,',','.') AS FLOAT))  AS TEXT),'.',',') r4, "
                itens = itens + " REPLACE(CAST(  SUM(CAST(replace(r5,',','.') AS FLOAT))  AS TEXT),'.',',') r5, "
                itens = itens + " REPLACE(CAST(  SUM(CAST(replace(r6,',','.') AS FLOAT))  AS TEXT),'.',',') r6, "
                itens = itens + " r7,r8,r9, "
                itens = itens + " REPLACE(CAST(  SUM(CAST(replace(r10,',','.') AS FLOAT))  AS TEXT),'.',',') r10, "
                itens = itens + " r11 "
                itens = itens + " FROM principal "
                itens = itens + " WHERE r1 = \"C185\" "
                itens = itens + " AND r0 between " + str(n1) + " AND " + str(n2) + " "
                itens = itens + " GROUP BY r1,r2,r3,r7,r8,r9,r11 "
                itens = cursor.execute(itens)
                itens = itens.fetchall()

                ## deleta todos os itens r0
                delete = "delete from principal where r0 in (" + ",".join([str(i) for i in to_delete]) + ")"
                cursor.execute(delete)
                conexao.commit()
                ## inserir os novos dados com os ids livres
                for i in range(0,len(itens)):
                    data = str(to_delete[i]) + ',"' + "\",\"".join(itens[i]) + '"'
                    insert = " INSERT INTO principal(r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11) "
                    insert = insert + " VALUES( "
                    insert = insert + str(to_delete[i]) + ',"' + "\",\"".join(itens[i]) + '"'
                    insert = insert + " ) "
                    cursor.execute(insert)
                    conexao.commit()





    print('-',end=' ')
    print("Finalizado")