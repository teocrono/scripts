## 
## 
## 


def exec(conexao):

    cursor = conexao.cursor()

    print("RULE 18 - Inicializando",end=' ')


    select = "select r0 from principal where r1 = \"C505\" and "
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
        select = "select max(r0) from principal where r1 = \"C500\" AND r0 < " + str(i)
        select = cursor.execute(select)
        ini = select.fetchone()[0]

        select = "select min(r0) from principal where r1 = \"C500\" AND r0 > " + str(i)
        select = cursor.execute(select)
        fim = select.fetchone()[0]

        if fim == None:
            fim = ini + 1000

        update = " UPDATE principal SET "
        update = update + " r14 = ( "
        update = update + " select REPLACE(CAST(  SUM(CAST(replace(r7,',','.') AS FLOAT))  AS TEXT),'.',',') "
        update = update + " FROM principal WHERE r1 = \"C505\" "
        update = update + " and r0 between " + str(ini) + " AND " + str(fim) + " "
        update = update + " GROUP BY r2"
        update = update + " ) "
        update = update + " WHERE 1=1 "
        update = update + " AND r0 = " + str(ini) + " "
        cursor.execute(update)
        conexao.commit()
















    print('-',end=' ')
    print("Finalizado")