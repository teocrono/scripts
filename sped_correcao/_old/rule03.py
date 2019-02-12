## Arruma o CST dos grupos C181 e C185
## Arruma o CST dos grupos C170
## Arruma o CST dos grupos C491 e C495


def exec(conexao):

    cursor = conexao.cursor()

    print("RULE 03 - Inicializando",end=' ')

    update = " UPDATE principal SET "
    update = update + " r2 = \"49\" "
    update = update + " WHERE r0 in (SELECT r0 FROM principal WHERE "
    update = update + "      r1 in (\"C181\",\"C185\") "
    update = update + "      AND r2 = \"50\") "
    cursor.execute(update)
    conexao.commit()
    print('-',end=' ')
    
    update = " UPDATE principal SET "
    update = update + " r2 = \"07\" "
    update = update + " WHERE r0 in (SELECT r0 FROM principal WHERE "
    update = update + "      r1 in (\"C181\",\"C185\") "
    update = update + "      AND r2 = \"99\" "
    update = update + "      AND r7 = \"0,0000\") "
    cursor.execute(update)
    conexao.commit()
    print('-',end=' ')

    update = " UPDATE principal SET "
    update = update + " r25 = \"50\", "
    update = update + " r31 = \"50\" "
    update = update + " WHERE r0 in (SELECT r0 FROM principal WHERE "
    update = update + "      r1 = \"C170\" "
    update = update + "      AND r11 = \"1303\") "
    cursor.execute(update)
    conexao.commit()
    print('-',end=' ')

    update = " UPDATE principal SET "
    update = update + " r3 = \"01\" "
    update = update + " WHERE r0 in (select r0 from principal WHERE "
    update = update + "      r1 = \"C491\" "
    update = update + "      and r4 in (\"5101\",\"5102\",\"5405\") "
    update = update + "      and r7 = \"1,6500\") "
    cursor.execute(update)
    conexao.commit()
    print('-',end=' ')

    update = " UPDATE principal SET "
    update = update + " r3 = \"07\" "
    update = update + " where r0 in (select r0 from principal where "
    update = update + "      r1 = \"C491\" "
    update = update + "      and r4 in (\"5405\") "
    update = update + "      and r7 = \"0,0000\") "
    cursor.execute(update)
    conexao.commit()
    print('-',end=' ')

    update = " UPDATE principal SET "
    update = update + " r3 = \"01\" "
    update = update + " where r0 in (select r0 from principal where "
    update = update + "      r1 = \"C495\" and "
    update = update + "      r4 in (\"5101\",\"5102\",\"5405\") "
    update = update + "      and r7 = \"7,6000\") "
    cursor.execute(update)
    conexao.commit()
    print('-',end=' ')

    update = " UPDATE principal SET "
    update = update + " r3 = \"07\" "
    update = update + " where r0 in (select r0 from principal where "
    update = update + "      r1 = \"C495\" "
    update = update + "      and r4 in (\"5405\") "
    update = update + "      and r7 = \"0,0000\") "
    cursor.execute(update)
    conexao.commit()
    print('-',end=' ')



    update = " UPDATE principal SET "
    update = update + " r3 = \"01\", "
    update = update + " r7 = \"1,6500\", "
    update = update + " r6 = r5, "
    update = update + " r10 = REPLACE(CAST(  ROUND((CAST(replace(r5,',','.') AS FLOAT) * 1.65 / 100),2)  AS TEXT),'.',',') "
    update = update + " where r1 = \"C491\" "
    update = update + " and r4 = \"5102\" "
    update = update + " and r3 = \"50\" "
    cursor.execute(update)
    conexao.commit()
    print('-',end=' ')
    update = " UPDATE principal SET "
    update = update + " r3 = \"01\", "
    update = update + " r7 = \"7,6000\", "
    update = update + " r6 = r5, "
    update = update + " r10 = REPLACE(CAST(  ROUND((CAST(replace(r5,',','.') AS FLOAT) * 7.6 / 100),2)  AS TEXT),'.',',') "
    update = update + " where r1 = \"C495\" "
    update = update + " and r4 = \"5102\" "
    update = update + " and r3 = \"50\" "
    cursor.execute(update)
    conexao.commit()
    print('-',end=' ')







## colocado no dia 30/08/2017
    update = '''
        UPDATE principal SET
	        r2 = "49"
        WHERE r1 = "C181" 
              AND r2 = "00"
              AND r3 in ("5405","6101","6102")
    '''
    cursor.execute(update)
    conexao.commit()
    update = '''
        UPDATE principal SET
	        r2 = "49"
        WHERE r1 = "C185" 
              AND r2 = "00"
              AND r3 in ("5405","6101","6102")
    '''
    cursor.execute(update)
    conexao.commit()


    update = " UPDATE principal SET "
    update = update + " r3 = \"01\", "
    update = update + " r6 = r5, "
    update = update + " r7 = \"1,6500\", "
    update = update + " r10 = REPLACE(CAST(  ROUND((CAST(replace(r5,',','.') AS FLOAT) * 1.65 / 100),2)  AS TEXT),'.',',') "
    update = update + " WHERE 1=1 "
    update = update + " AND r1 = \"C491\" "
    update = update + " AND r3 = \"00\" "
    update = update + " AND r4 = \"5102\" "
    cursor.execute(update)
    conexao.commit()

    update = " UPDATE principal SET "
    update = update + " r3 = \"01\", "
    update = update + " r6 = r5, "
    update = update + " r7 = \"7,6000\", "
    update = update + " r10 = REPLACE(CAST(  ROUND((CAST(replace(r5,',','.') AS FLOAT) * 7.6 / 100),2)  AS TEXT),'.',',') "
    update = update + " WHERE 1=1 "
    update = update + " AND r1 = \"C495\" "
    update = update + " AND r3 = \"00\" "
    update = update + " AND r4 = \"5102\" "
    cursor.execute(update)
    conexao.commit()


    print("Finalizado")