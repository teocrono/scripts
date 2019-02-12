## Campo obrigatório quando o CST PIS ou CST COFINS for referente a operação com direito a crédito.
##
## função para arrumar a natureza da base de calculo no D501 quando o CST for 
## igual a 50, neste caso colocar o código como 13
def exec(conexao):    
    cursor = conexao.cursor()
  
    update = '''
        UPDATE principal SET
            r4 = "13"
        WHERE 1=1
            and r1 = "D501" 
            and r2 = "50"
    '''
    cursor.execute(update)
    conexao.commit()
    print('REGISTROS D501 mudado a natureza para 13 quando cst = 50')

    update = '''
        UPDATE principal SET
            r2 = "70"
        WHERE 1=1
            and r1 in ("D501","D505")
            and r2 = "00"
    '''
    cursor.execute(update)
    conexao.commit()
    print('REGISTROS D501 mudado a cst de 00 para 70')


##------------------------------------------------------------------------------------------------------##
    update = " UPDATE principal SET "
    update = update + " r5 = r3, "
    update = update + " r6 = \"1,6500\", "
    update = update + " r7 = REPLACE(CAST(  ROUND((CAST(replace(r3,',','.') AS FLOAT) * 1.65 / 100),2)  AS TEXT),'.',',') "
    update = update + " WHERE 1=1 "
    update = update + " AND r1 = \"D501\" "
    update = update + " AND r6 = \"1,6500\" "
    update = update + " AND CAST(replace(r6,',','.') AS FLOAT) > 10 "
    cursor.execute(update)
    conexao.commit()
    update = " UPDATE principal SET "
    update = update + " r5 = r3, "
    update = update + " r6 = \"7,6000\", "
    update = update + " r7 = REPLACE(CAST(  ROUND((CAST(replace(r3,',','.') AS FLOAT) * 7.6 / 100),2)  AS TEXT),'.',',') "
    update = update + " WHERE 1=1 "
    update = update + " AND r1 = \"D505\" "
    update = update + " AND r6 = \"7,6000\" "
    update = update + " AND CAST(replace(r6,',','.') AS FLOAT) > 10 "
    cursor.execute(update)
    conexao.commit()
    update = " UPDATE principal SET "
    update = update + " r4 = \"03\" "
    update = update + " WHERE 1=1 "
    update = update + " AND r1 in (\"D501\",\"D505\") "
    update = update + " AND r4 = \"00\" "
    cursor.execute(update)
    conexao.commit()
##------------------------------------------------------------------------------------------------------##
    select = " select r0 from principal where r1 = \"D500\" "
    select = cursor.execute(select)
    rselect = select.fetchall()
    rselect = [i[0] for i in rselect]
    if(len(rselect) != 0):
        rselect.append(rselect[len(rselect)-1] + 1000)

        n1 = rselect.pop(0)
        while len(rselect) > 0:
            n2 = rselect.pop(0)
            ##pis e cofins
            update = " UPDATE principal SET "
            update = update + " r21 = (select "
            update = update + " REPLACE(CAST(  ROUND(  SUM(CAST(replace(r7,',','.') AS FLOAT)),2)  AS TEXT),'.',',') "
            update = update + " from principal "
            update = update + " where r1 = \"D501\" "
            update = update + " AND r0 between " + str(n1) + " AND " + str(n2) + "), "
            update = update + " r22 = (select "
            update = update + " REPLACE(CAST(  ROUND(  SUM(CAST(replace(r7,',','.') AS FLOAT)),2)  AS TEXT),'.',',') "
            update = update + " from principal "
            update = update + " where r1 = \"D505\" "
            update = update + " AND r0 between " + str(n1) + " AND " + str(n2) + ") "
            update = update + " WHERE 1=1 "
            update = update + " AND r0 = " + str(n1) + " "
            update = update + " AND r6 = \"00\" "
            cursor.execute(update)
            conexao.commit()

            n1 = n2