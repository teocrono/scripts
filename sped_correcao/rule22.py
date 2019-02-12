# atualiza os valores do D500

def exec(conexao):

    cursor = conexao.cursor()

    print("RULE 21 - Inicializando",end=' ')

    select = "SELECT r0 FROM principal WHERE r1 = \"D500\" "
    select = cursor.execute(select)
    select = select.fetchall()
    ids = [i[0] for i in select]

    for i in ids:
        ini = i

        select = "SELECT min(r0) FROM principal WHERE r1 = \"D500\" AND r0 > " + str(i)
        select = cursor.execute(select)
        fim = select.fetchone()[0]

        if fim == None:
            fim = ini + 1000

        update = " UPDATE principal SET "
        update = update + " r21 = ( "
        update = update + " select REPLACE(CAST(  SUM(CAST(replace(r7,',','.') AS FLOAT))  AS TEXT),'.',',') "
        update = update + " FROM principal WHERE r1 = \"D501\" "
        update = update + " and r0 between " + str(ini) + " AND " + str(fim) + " "
        update = update + " GROUP BY r1"
        update = update + " ), "
        update = update + " r22 = ( "
        update = update + " select REPLACE(CAST(  SUM(CAST(replace(r7,',','.') AS FLOAT))  AS TEXT),'.',',') "
        update = update + " FROM principal WHERE r1 = \"D505\" "
        update = update + " and r0 between " + str(ini) + " AND " + str(fim) + " "
        update = update + " GROUP BY r1"
        update = update + " ) "
        update = update + " WHERE 1=1 "
        update = update + " AND r0 = " + str(ini) + " "
        cursor.execute(update)
        conexao.commit()


