## arruma valor do pis e cofins do C100
## 
## 

def exec(conexao):

    cursor = conexao.cursor()

    print("RULE 07 - Inicializando",end=' ')

    select = " select r0 from principal where r1 = \"C100\" "
    select = cursor.execute(select)
    rselect = select.fetchall()
    rselect = [i[0] for i in rselect]
    rselect.append(rselect[len(rselect)-1] + 1000)

    n2 = rselect.pop(0)
    while len(rselect) > 0:
        print('-',end=' ')
        n1 = n2
        n2 = rselect.pop(0)
        ##pis e cofins
        update = " UPDATE principal SET "
        update = update + " r26 = (select "
        update = update + "          REPLACE(CAST(  ROUND(  SUM(CAST(replace(r30,',','.') AS FLOAT)),2)  AS TEXT),'.',',') "
        update = update + "          FROM principal "
        update = update + "          where r1 = \"C170\" "
        update = update + "            AND r0 between " + str(n1) + " AND " + str(n2) + " "
        update = update + "            and r25 not in (\"05\",\"75\")), "
        update = update + " r27 = (select "
        update = update + "          REPLACE(CAST(  ROUND(  SUM(CAST(replace(r36,',','.') AS FLOAT)),2)  AS TEXT),'.',',') "
        update = update + "          FROM principal "
        update = update + "          where r1 = \"C170\" "
        update = update + "            AND r0 between " + str(n1) + " AND " + str(n2) + " "
        update = update + "            and r31 not in (\"05\",\"75\")) "
        update = update + " WHERE "
        update = update + "     r0 = " + str(n1) + " "
        update = update + "     AND r2 = \"0\" "
        update = update + "     AND r3 = \"1\" "
        update = update + "     AND r5 = \"01\" "
        update = update + "     AND r6 = \"00\" "
        cursor.execute(update)
        conexao.commit()

    print('-',end=' ')
    print("Finalizado")