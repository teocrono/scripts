## 
## 
## 


def exec(conexao):

    cursor = conexao.cursor()

    print("RULE 16 - Inicializando",end=' ')

    update = " UPDATE principal SET "
    update = update + " r25 = \"50\", "
    update = update + " r31 = \"50\" "
    update = update + " WHERE 1=1 "
    update = update + " AND r1 = \"C170\" "
    update = update + " AND r3 = \"99999999\" "
    cursor.execute(update)
    conexao.commit()

    print('-',end=' ')
    print("Finalizado")