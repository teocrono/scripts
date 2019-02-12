## arruma valores inseridos errados de pis no D501
## 
## 


def exec(conexao):

    cursor = conexao.cursor()

    print("RULE 15 - Inicializando",end=' ')

    select = "select r0 from principal where r1 = \"D501\" and  "
    select = select + " (CAST(replace(r6,',','.') AS FLOAT) > 10 or r6 = \"1,6000\") "
    select = cursor.execute(select)
    select = select.fetchall()
    ids = [i[0] for i in select]

    for i in ids:
        print('-',end=' ')
        update = " UPDATE principal SET "
        update = update + " r6 = \"1,6500\", "
        update = update + " r7 = REPLACE(CAST(  ROUND((CAST(replace(r3,',','.') AS FLOAT) * 1.65 / 100),2)  AS TEXT),'.',',') "
        update = update + " WHERE 1=1 "
        update = update + " AND r0 = " + str(i) + " "
        cursor.execute(update)
        conexao.commit()

        ## D500 < i
        select = "select max(r0) from principal where r1 = \"D500\" AND r0 < " + str(i)
        select = cursor.execute(select)
        ini = select.fetchone()[0]

        select = "select min(r0) from principal where r1 = \"D500\" AND r0 > " + str(i)
        select = cursor.execute(select)
        fim = select.fetchone()[0]

        if fim == None:
            fim = ini + 1000

        update = " UPDATE principal SET "
        update = update + " r21 = ( "
        update = update + " select REPLACE(CAST(  SUM(CAST(replace(r7,',','.') AS FLOAT))  AS TEXT),'.',',') "
        update = update + " FROM principal WHERE r1 = \"D501\" "
        update = update + " and r0 between " + str(ini) + " AND " + str(fim) + " "
        update = update + " GROUP BY r2"
        update = update + " ) "
        update = update + " WHERE 1=1 "
        update = update + " AND r0 = " + str(ini) + " "
        cursor.execute(update)
        conexao.commit()



    select = "select r0 from principal where r1 = \"D505\" and "
    select = select + " (CAST(replace(r6,',','.') AS FLOAT) < 2 or CAST(replace(r6,',','.') AS FLOAT) > 10)"
    select = cursor.execute(select)
    select = select.fetchall()
    ids = [i[0] for i in select]

    for i in ids:
        print('-',end=' ')
        update = " UPDATE principal SET "
        update = update + " r6 = \"7,6000\", "
        update = update + " r7 = REPLACE(CAST(  ROUND((CAST(replace(r3,',','.') AS FLOAT) * 7.6 / 100),2)  AS TEXT),'.',',') "
        update = update + " WHERE 1=1 "
        update = update + " AND r0 = " + str(i) + " "
        cursor.execute(update)
        conexao.commit()

        ## D500 < i
        select = "select max(r0) from principal where r1 = \"D500\" AND r0 < " + str(i)
        select = cursor.execute(select)
        ini = select.fetchone()[0]

        select = "select min(r0) from principal where r1 = \"D500\" AND r0 > " + str(i)
        select = cursor.execute(select)
        fim = select.fetchone()[0]

        if fim == None:
            fim = ini + 1000

        update = " UPDATE principal SET "
        update = update + " r21 = ( "
        update = update + " select REPLACE(CAST(  SUM(CAST(replace(r7,',','.') AS FLOAT))  AS TEXT),'.',',') "
        update = update + " FROM principal WHERE r1 = \"D505\" "
        update = update + " and r0 between " + str(ini) + " AND " + str(fim) + " "
        update = update + " GROUP BY r2"
        update = update + " ) "
        update = update + " WHERE 1=1 "
        update = update + " AND r0 = " + str(ini) + " "
        cursor.execute(update)
        conexao.commit()





    print('-',end=' ')
    print("Finalizado")