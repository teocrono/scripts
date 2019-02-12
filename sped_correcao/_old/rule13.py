## 
## 
## 


def exec(conexao):

    cursor = conexao.cursor()

    print("RULE 13 - Inicializando",end=' ')

    select = " SELECT r0 FROM principal WHERE r1 in (\"C501\") AND r2 = \"00\" AND r4 = \"04\" "
    select = cursor.execute(select)
    select = select.fetchall()
    c501s = [i[0] for i in select]
    
    for i in c501s:
        print('-',end=' ')
        update = " UPDATE principal SET "
        update = update + " r2 = \"50\", "
        update = update + " r6 = \"1,6500\", "
        update = update + " r5 = r3, "
        update = update + " r7 = REPLACE(CAST(  ROUND((CAST(replace(r3,',','.') AS FLOAT) * 1.65 / 100),2)  AS TEXT),'.',',') "
        update = update + " WHERE 1=1 "
        update = update + " AND r0 = " + str(i) + " "
        cursor.execute(update)
        conexao.commit()

        select = " SELECT max(r0) FROM principal WHERE r1 in (\"C500\") AND r0 < " + str(i) + " "
        select = cursor.execute(select)
        r0 = select.fetchone()[0]

        ##verifica se não é null o ultimo C500
        select = " SELECT min(r0)-1 FROM principal where r1 in (\"C500\") AND r0 > " + str(r0) + " "
        select = cursor.execute(select)
        r01 = select.fetchone()[0]
        r01 = r01 if r01 != None else r0 + 100

        update = " UPDATE principal SET "
        update = update + " r13 = "
        update = update + " (SELECT REPLACE(CAST(  ROUND(  SUM(CAST(replace(r7,',','.') AS FLOAT)),2)  AS TEXT),'.',',')  "
        update = update + "        FROM principal WHERE "
        update = update + "        r1 = \"C501\" "
        update = update + "        AND r0 BETWEEN " + str(r0) + " AND " + str(r01) + " "
        update = update + " ) "
        update = update + " WHERE 1=1 "
        update = update + " AND r0 = " + str(r0) + " "
        cursor.execute(update)
        conexao.commit()
        




    select = " SELECT r0 FROM principal WHERE r1 in (\"C505\") AND r2 = \"00\" AND r4 = \"04\" "
    select = cursor.execute(select)
    select = select.fetchall()
    c501s = [i[0] for i in select]
    
    for i in c501s:
        print('-',end=' ')
        update = " UPDATE principal SET "
        update = update + " r2 = \"50\", "
        update = update + " r6 = \"7,6000\", "
        update = update + " r5 = r3, "
        update = update + " r7 = REPLACE(CAST(  ROUND((CAST(replace(r3,',','.') AS FLOAT) * 7.6 / 100),2)  AS TEXT),'.',',') "
        update = update + " WHERE 1=1 "
        update = update + " AND r0 = " + str(i) + " "
        cursor.execute(update)
        conexao.commit()

        select = " SELECT max(r0) FROM principal WHERE r1 in (\"C500\") AND r0 < " + str(i) + " "
        select = cursor.execute(select)
        r0 = select.fetchone()[0]

        ##verifica se não é null o ultimo C500
        select = " SELECT min(r0)-1 FROM principal where r1 in (\"C500\") AND r0 > " + str(r0) + " "
        select = cursor.execute(select)
        r01 = select.fetchone()[0]
        r01 = r01 if r01 != None else r0 + 100

        update = " UPDATE principal SET "
        update = update + " r13 = "
        update = update + " (SELECT REPLACE(CAST(  ROUND(  SUM(CAST(replace(r7,',','.') AS FLOAT)),2)  AS TEXT),'.',',')  "
        update = update + "        FROM principal WHERE "
        update = update + "        r1 = \"C505\" "
        update = update + "        AND r0 BETWEEN " + str(r0) + " AND " + str(r01) + " "
        update = update + " ) "
        update = update + " WHERE 1=1 "
        update = update + " AND r0 = " + str(r0) + " "
        cursor.execute(update)
        conexao.commit()
        


    print("Finalizado")