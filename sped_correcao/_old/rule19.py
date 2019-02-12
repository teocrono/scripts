## 
## 
## 


def exec(conexao):

    cursor = conexao.cursor()

    print("RULE 19 - Inicializando",end=' ')




#######################feito no dia 29/08####################################################
    select = "select r0 from principal where r1 in (\"C181\",\"C185\") and r3 in "
    select = select + " (\"5151\",\"5152\",\"5409\",\"5929\",\"5915\",\"6915\",\"5408\",\"5901\") "
    select = cursor.execute(select)
    select = select.fetchall()
    ids = [i[0] for i in select]

    for i in ids:
        print('|',end=' ')
        update = " UPDATE principal SET "
        update = update + " r2 = \"49\", "
        update = update + " r6 = \"0,00\", "
        update = update + " r7 = \"0,0000\", "
        update = update + " r10 = \"0,00\" "
        update = update + " WHERE 1=1 "
        update = update + " AND r0 = " + str(i) + " "
        cursor.execute(update)
        conexao.commit()

    select = "select r0 from principal where r1 in (\"C191\",\"C195\") and r4 in "
    select = select + " (\"1151\",\"1152\",\"1409\",\"1556\",\"1551\",\"2406\",\"1406\",\"2551\",\"2556\", "
    select = select + "\"1922\",\"2922\",\"2911\",\"1407\",\"1552\",\"1908\",\"1916\",\"2407\",\"2908\") "
    select = cursor.execute(select)
    select = select.fetchall()
    ids = [i[0] for i in select]

    for i in ids:
        print('|',end=' ')
        update = " UPDATE principal SET "
        update = update + " r3 = \"99\", "
        update = update + " r7 = \"0,00\", "
        update = update + " r8 = \"0,0000\", "
        update = update + " r11 = \"0,00\" "
        update = update + " WHERE 1=1 "
        update = update + " AND r0 = " + str(i) + " "
        cursor.execute(update)
        conexao.commit()





    print('-',end=' ')
    print("Finalizado")