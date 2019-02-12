# atualiza os valores do C100

def exec(conexao):

    cursor = conexao.cursor()

    print("RULE 23 - Inicializando",end=' ')

    select = "SELECT r0 FROM principal WHERE r1 = \"C100\" "
    select = cursor.execute(select)
    select = select.fetchall()
    ids = [i[0] for i in select]

    for i in ids:
        ini = i

        select = "SELECT min(r0) FROM principal WHERE r1 = \"C100\" AND r0 > " + str(i)
        select = cursor.execute(select)
        fim = select.fetchone()[0]

        if fim == None:
            fim = ini + 1000

        select = " select REPLACE(CAST(  ROUND( SUM(CAST(replace(r30,',','.') AS FLOAT)) ,2)  AS TEXT),'.',',') "
        select = select + " FROM principal WHERE r1 = \"C170\" "
        select = select + " and r0 between " + str(ini) + " AND " + str(fim) + " "
        select = select + " GROUP BY r1"
        select = cursor.execute(select)
        r26 = select.fetchone()
        r26 = '' if (r26 == None) else r26[0]

        select = " select REPLACE(CAST(  ROUND( SUM(CAST(replace(r36,',','.') AS FLOAT)) ,2)  AS TEXT),'.',',') "
        select = select + " FROM principal WHERE r1 = \"C170\" "
        select = select + " and r0 between " + str(ini) + " AND " + str(fim) + " "
        select = select + " GROUP BY r1"
        select = cursor.execute(select)
        r27 = select.fetchone()
        r27 = '' if (r27 == None) else r27[0]

        update = " UPDATE principal SET "
        update = update + " r26 = \"" + r26 + "\", "
        update = update + " r27 = \"" + r27 + "\" "
        update = update + " WHERE 1=1 "
        update = update + " AND r0 = " + str(ini) + " "
        cursor.execute(update)
        conexao.commit()

    print('-',end=' ')
    print("Finalizado")
