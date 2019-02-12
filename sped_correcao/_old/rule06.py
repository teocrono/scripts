## arruma pis percentual de 1,66 para 1,65 no c191 e c181
## arruma cofins percentual de 7,3 
## arruma cofins percentual de xx para 1,6500 


def exec(conexao):

    cursor = conexao.cursor()

    print("RULE 06 - Inicializando",end=' ')

    select = " select r0 from principal where r1 = \"C170\" and r33 in(\"2,0000\") "
    select = cursor.execute(select)
    rselect = select.fetchall()
    rselect = [i[0] for i in rselect]
    for i in rselect:
        print('-',end=' ')
        update = " UPDATE principal SET "
        update = update + " r33 = \"0,0000\", "
        update = update + " r36 = \"0,00\" "
        update = update + " WHERE r0 = " + str(i) + " "
        cursor.execute(update)
        conexao.commit()
        
        update = " UPDATE principal SET "
        update = update + " r27 = \"0,00\" "
        update = update + " WHERE r0 = (select max(r0) from principal where "
        update = update + "                r1 = \"C100\" and r0 between " + str(i - 100) + " and " + str(i) + ") "
        cursor.execute(update)
        conexao.commit()

    print("Finalizado")