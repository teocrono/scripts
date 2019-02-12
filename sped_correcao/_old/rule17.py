## 
## 
## 


def exec(conexao):

    cursor = conexao.cursor()

    print("RULE 17 - Inicializando",end=' ')

    # update = '''
    #     UPDATE principal SET
	#         r25 = "49",
    #         r31 = "49"
    #     where r1 = "C170" and r25 = "50" and r31 = "50" and r12 = "10009" 
    #           and r10 in ("060","041")
    #           and r11 in ("5409","5152")
    # '''
    # cursor.execute(update)
    # conexao.commit()


    update = '''
        UPDATE principal SET
	        r27 = "1,6500",
            r30 = REPLACE(CAST(  ROUND((CAST(replace(r26,',','.') AS FLOAT) * 1.65 / 100),2)  AS TEXT),'.',',') 
        WHERE r1 = "C170" 
              AND CAST(replace(r27,',','.') AS FLOAT) < 1.64 and CAST(replace(r27,',','.') AS FLOAT) > 0.1
    '''
    cursor.execute(update)
    conexao.commit()





    # update = '''
    #     UPDATE principal SET
	#         r3 = "70",
    #         r7 = "0,00",
    #         r8 = "0,0000",
    #         r11 = "0,00"
    #     WHERE r1 = "C191" 
    #           AND length(r2) = 11
    #           AND r4 = "1102"
    #           AND r3 = "49"
    # '''
    # cursor.execute(update)
    # conexao.commit()

    # update = '''
    #     UPDATE principal SET
	#         r3 = "70",
    #         r7 = "0,00",
    #         r8 = "0,0000",
    #         r11 = "0,00"
    #     WHERE r1 = "C195" 
    #           AND length(r2) = 11
    #           AND r4 = "1102"
    #           AND r3 = "49"
    # '''
    # cursor.execute(update)
    # conexao.commit()

    print('-',end=' ')
    print("Finalizado")