## Para operações de saída, o CST deve ser preenchido com os valores de 01 a 49 ou 99.
## 
## 

def exec(conexao):

    cursor = conexao.cursor()

    print("RULE 08 - Inicializando",end=' ')

    update = " UPDATE principal SET "
    update = update + " r2 = \"49\" "
    update = update + " WHERE 1=1 "
    update = update + "     and r1 = \"C181\" "
    update = update + "     and r2 in (\"00\",\"99\") "
    update = update + "     and r3 in (\"5152\",\"5102\") "
    cursor.execute(update)
    conexao.commit()
    print('-',end=' ')

    update = " UPDATE principal SET "
    update = update + " r2 = \"49\" "
    update = update + " WHERE 1=1 "
    update = update + "     and r1 = \"C185\" "
    update = update + "     and r2 in (\"00\",\"99\") "
    update = update + "     and r3 in (\"5152\",\"5102\") "
    cursor.execute(update)
    conexao.commit()
    print('-',end=' ')

    print("Finalizado")