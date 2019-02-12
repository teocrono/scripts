## arruma D101 e D105
## 
## 


def exec(conexao):

    cursor = conexao.cursor()

    print("RULE 05 - Inicializando",end=' ')

    update = " update principal set "
    update = update + " r4 = \"50\", "
    update = update + " r7 = \"1,6500\", "
    update = update + " r8 = REPLACE(CAST(  ROUND((CAST(replace(r3,',','.') AS FLOAT) * 1.65 / 100),2)  AS TEXT),'.',',') "
    update = update + " where r1 = \"D101\" and r4 = \"00\" "
    cursor.execute(update)
    conexao.commit()
    print('-',end=' ')

    update = " update principal set "
    update = update + " r4 = \"50\", "
    update = update + " r7 = \"7,6000\", "
    update = update + " r8 = REPLACE(CAST(  ROUND((CAST(replace(r3,',','.') AS FLOAT) * 7.6 / 100),2)  AS TEXT),'.',',') "
    update = update + " WHERE r1 = \"D105\" and r4 in (\"00\",\"50\") "
    cursor.execute(update)
    conexao.commit()
    print('-',end=' ')
    
    print("Finalizado")