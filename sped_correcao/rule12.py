## arruma o cst no grupo C191 quando for pessoa fisica
## 
## 


def exec(conexao):

    cursor = conexao.cursor()

    print("RULE 12 - Inicializando",end=' ')

    # update = " UPDATE principal SET "
    # update = update + " r3 = \"49\" "
    # update = update + " WHERE 1=1 "
    # update = update + " and r1 = \"C191\" "
    # update = update + " and r4 in (\"1102\") "
    # update = update + " and length(r2) = 11 "
    # cursor.execute(update)
    # conexao.commit()
    # print('-',end=' ')

    # update = " UPDATE principal SET "
    # update = update + " r3 = \"49\" "
    # update = update + " WHERE 1=1 "
    # update = update + " and r1 = \"C195\" "
    # update = update + " and r4 in (\"1102\") "
    # update = update + " and length(r2) = 11 "
    # cursor.execute(update)
    # conexao.commit()
    # print('-',end=' ')

    update = " UPDATE principal SET "
    update = update + " r6 = (select max(r2) from principal where r1 = \"C195\" and  length(r2) = 11) "
    update = update + " WHERE 1=1 "
    update = update + " and r3 = \"CONSUMIDOR FINAL\" "
    cursor.execute(update)
    conexao.commit()
    print('-',end=' ')

    print("Finalizado")