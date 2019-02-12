## arruma o cst do C181 e C185
## identificado nos arquivos de 2012
import helper

def exec(conexao):
    cursor = conexao.cursor()

    update = '''
        UPDATE principal SET
	        r2 = "49"
        where r0 in (select r0 from principal where r1 in ("C181","C185") and r2 = "50")
    '''
    cursor.execute(update)
    conexao.commit()
    update = '''
        UPDATE principal SET
	        r2 = "07"
        where r0 in (select r0 from principal where r1 in ("C181","C185") and r2 = "99" and r7 = "0,0000")
    '''
    cursor.execute(update)
    conexao.commit()
    print("atualizado cst dos registros C181 e C185")

    update = '''
        UPDATE principal SET
	        r25 = "50",
            r31 = "50"
        where r0 in (select r0 from principal where r1 = "C170" and r11 = "1303")
    '''
    cursor.execute(update)
    conexao.commit()
    print("atualizado cst dos registros C170")

    update = '''
        UPDATE principal SET
	        r3 = "01"
        where r0 in (select r0 from principal where r1 = "C491" and r4 in ("5101","5102","5405") and r7 = "1,6500")
    '''
    cursor.execute(update)
    conexao.commit()
    update = '''
        UPDATE principal SET
	        r3 = "07"
        where r0 in (select r0 from principal where r1 = "C491" and r4 in ("5405") and r7 = "0,0000")
    '''
    cursor.execute(update)
    conexao.commit()

    update = '''
        UPDATE principal SET
	        r3 = "01"
        where r0 in (select r0 from principal where r1 = "C495" and r4 in ("5101","5102","5405") and r7 = "7,6000")
    '''
    cursor.execute(update)
    conexao.commit()
    update = '''
        UPDATE principal SET
	        r3 = "07"
        where r0 in (select r0 from principal where r1 = "C495" and r4 in ("5405") and r7 = "0,0000")
    '''
    cursor.execute(update)
    conexao.commit()
    print("atualizado cst dos registros C491 e C495")

##------------------------------------------------------------------------------------------------------##
    ## arruma duplicidade do C491 e C495
    for c in ["C491","C495"]:
        #pega o r0 do C490
        temp = cursor.execute("select r0 from principal where r1 = \"C490\"")
        temp = temp.fetchall()
        c490s = []
        for i in temp:
            c490s.append(i[0])
        temp = cursor.execute("select max(r0) + 1 from principal where r1 = \"" + c + "\"")
        temp = temp.fetchone()
        c490s.append(temp[0])
        ## arrumar os duplicados dentro de cada grupo do C490
        for i in range(0,len(c490s) - 1):
            ## r0 para deletar
            to_delete = " select r0 from principal where r2 in "
            to_delete = to_delete + " (select r2 from principal where r1 = \"" + c + "\" group by r2,r3,r4,r7,r9,r11 having count(*) > 1) "
            to_delete = to_delete + " and r1 = \"" + c + "\" and r0 between " + str(c490s[i]) + " and " + str(c490s[i+1]) + " order by r0 "
            to_delete = cursor.execute(to_delete)
            to_delete = to_delete.fetchall()
            to_delete = [i[0] for i in to_delete]
            ## recalcula o valor gerando apenas um item pelo grupo especifico definido no layout sped
            itens = " select r1,r2,r3,r4, "
            itens = itens + "    REPLACE(CAST(  SUM(CAST(replace(r5,',','.') AS FLOAT))  AS TEXT),'.',',') r5, "
            itens = itens + "    REPLACE(CAST(  SUM(CAST(replace(r6,',','.') AS FLOAT))  AS TEXT),'.',',') r6, "
            itens = itens + "    r7,r8,r9, "
            itens = itens + "    REPLACE(CAST(  SUM(CAST(replace(r10,',','.') AS FLOAT))  AS TEXT),'.',',') r10, "
            itens = itens + "    r11 from "
            itens = itens + " (select r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11 from principal where r2 in "
            itens = itens + " (select r2 from principal where r1 = \"" + c + "\" group by r2,r3,r4,r7,r9,r11 having count(*) > 1) "
            itens = itens + " and r1 = \"" + c + "\" and r0 between 17466 and 20366 order by r2) "
            itens = itens + " group by r1,r2,r3,r4,r7,r8,r9,r11 "
            itens = cursor.execute(itens)
            itens = itens.fetchall()
            ## deleta todos os itens r0
            delete = "delete from principal where r0 in (" + ",".join([str(i) for i in to_delete]) + ")"
            cursor.execute(delete)
            conexao.commit()
            ## inserir os novos dados com os ids livres
            for i2 in range(0,len(itens)):
                data = str(to_delete[i2]) + ',"' + "\",\"".join(itens[i2]) + '"'
                insert = " INSERT INTO principal(r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11)"
                insert = insert + " VALUES( "
                insert = insert + str(to_delete[i2]) + ',"' + "\",\"".join(itens[i2]) + '"'
                insert = insert + " ) "
                cursor.execute(insert)
                conexao.commit()

    ## arruma D101 e D105
    update = " update principal set "
    update = update + " r4 = \"50\", "
    update = update + " r7 = \"1,6500\", "
    update = update + " r8 = REPLACE(CAST(  ROUND((CAST(replace(r3,',','.') AS FLOAT) * 1.65 / 100),2)  AS TEXT),'.',',') "
    update = update + " where r1 = \"D101\" and r4 = \"00\" "
    cursor.execute(update)
    conexao.commit()
    update = " update principal set "
    update = update + " r4 = \"50\", "
    update = update + " r7 = \"7,6000\", "
    update = update + " r8 = REPLACE(CAST(  ROUND((CAST(replace(r3,',','.') AS FLOAT) * 7.6 / 100),2)  AS TEXT),'.',',') "
    update = update + " WHERE r1 = \"D105\" and r4 in (\"00\",\"50\") "
    cursor.execute(update)
    conexao.commit()

## << olhar depois >>
# ## atualiza C170 quando o campo cst está vazio, o que é proibido
# update = " update principal set "
# update = update + " r25 = \"50\", "
# #update = update + " r26 = r7, "
# #update = update + " r27 = \"1,6500\", "
# #update = update + " r30 = REPLACE(CAST(  ROUND((CAST(replace(r7,',','.') AS FLOAT) * 1.65 / 100),2)  AS TEXT),'.',','), "
# update = update + " r31 = \"50\" "
# #update = update + " r32 = r7, "
# #update = update + " r33 = \"7,6000\", "
# #update = update + " r36 = REPLACE(CAST(  ROUND((CAST(replace(r7,',','.') AS FLOAT) * 7.6 / 100),2)  AS TEXT),'.',',') "
# update = update + " WHERE r1 = \"C170\" and r25 = \"\" "
# cursor.execute(update)
# #conexao.commit()

##------------------------------------------------------------------------------------------------------##
    ## arrumando quantidade de registros pis/cofins no C491 e C495 do C490
    ## primeiro verefica e arruma no lado do cofins

    #pega o r0 do C490
    temp = cursor.execute("select r0 from principal where r1 = \"C490\"")
    temp = temp.fetchall()
    c490s = []
    for i in temp:
        c490s.append(i[0])
    temp = cursor.execute("select max(r0) + 1 from principal where r1 = \"C495\"")
    temp = temp.fetchone()
    c490s.append(temp[0])
    ## arrumar os duplicados dentro de cada grupo do C490
    for i in range(0,len(c490s) - 1):
        ## pega todos os registros dentro do C491 dentro do C490 que não estão no C495
        select = " SELECT p1.r1,p1.r2,p1.r3,p1.r4,p1.r5,p1.r6,p1.r7,p1.r8,p1.r9,p1.r10,p1.r11 "
        select = select + " FROM "
        select = select + " (select r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11 from principal where r1 = \"C491\") p1 "
        select = select + " LEFT JOIN "
        select = select + " (select r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11 from principal where r1 = \"C495\") p2 "
        select = select + " ON (p1.r2 = p2.r2 and p1.r3 = p2.r3 and p1.r4 = p2.r4) "
        select = select + " WHERE p2.r2 is null "
        notin_c495 = cursor.execute(select)
        notin_c495 = notin_c495.fetchall()
        ## atualiza os valores dos ids para que seja possível inserir novos itens
        update = " update principal set "
        update = update + " r0 = r0 + " + str(len(notin_c495) + 5) + " "
        update = update + " where r0 >= " + str(c490s[i+1])
        cursor.execute(update)
        conexao.commit()
        ## insere os registros que estão faltando no cofins C495
        contador = c490s[i+1]
        for i2 in notin_c495:
            insert = " INSERT INTO principal(r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11)"
            insert = insert + " VALUES( "
            insert = insert + str(contador) + ","
            insert = insert + "\"C495\","
            insert = insert + "\"" + i2[1] + "\","
            insert = insert + "\"" + i2[2] + "\","
            insert = insert + "\"" + i2[3] + "\","
            insert = insert + "\"" + i2[4] + "\","
            insert = insert + "\"" + i2[5] + "\","
            insert = insert + "\"7,6000\","
            insert = insert + "\"" + i2[7] + "\","
            insert = insert + "\"" + i2[8] + "\","
            insert = insert + "\"" + helper.soma2strfloat(i2[9],"7,6000") + "\","
            insert = insert + "\"" + i2[10] + "\""
            insert = insert + " ) "
            cursor.execute(insert)
            conexao.commit()
            contador = contador + 1

##------------------------------------------------------------------------------------------------------##
    ##arruma pis percentual de 1,66 para 1,65 no c191 e c181
    update = " update principal set "
    update = update + " r8 = \"1,6500\", "
    update = update + " r11 = REPLACE(CAST(  ROUND((CAST(replace(r7,',','.') AS FLOAT) * 1.65 / 100),2)  AS TEXT),'.',',') "
    update = update + " where r1 in (\"C181\",\"C191\") and r8 = \"1,6600\" "
    cursor.execute(update)
    conexao.commit()

##------------------------------------------------------------------------------------------------------##
    ##arruma cofins percentual de 7,3 
    update = " update principal set "
    update = update + " r33 = \"7,6000\", "
    update = update + " r36 = REPLACE(CAST(  ROUND((CAST(replace(r32,',','.') AS FLOAT) * 7.6 / 100),2)  AS TEXT),'.',',') "
    update = update + " where r1 in (\"C170\") and r33 in (\"7,3000\",\"7,2000\",\"7,6000\") "
    cursor.execute(update)
    conexao.commit()
    ##arruma cofins percentual de xx para 1,6500 
    update = " update principal set "
    update = update + " r27 = \"1,6500\", "
    update = update + " r30 = REPLACE(CAST(  ROUND((CAST(replace(r26,',','.') AS FLOAT) * 1.65 / 100),2)  AS TEXT),'.',',') "
    update = update + " where r1 in (\"C170\") and r27 in (\"1,6500\") "
    cursor.execute(update)
    conexao.commit()

##------------------------------------------------------------------------------------------------------##
    select = " select r0 from principal where r1 = \"C100\" "
    select = cursor.execute(select)
    rselect = select.fetchall()
    rselect = [i[0] for i in rselect]
    rselect.append(rselect[len(rselect)-1] + 1000)

    n1 = rselect.pop(0)
    while len(rselect) > 0:
        n2 = rselect.pop(0)
        ##pis e cofins
        update = " UPDATE principal SET "
        update = update + " r26 = (select "
        update = update + " REPLACE(CAST(  ROUND(  SUM(CAST(replace(r30,',','.') AS FLOAT)),2)  AS TEXT),'.',',') "
        update = update + " from principal "
        update = update + " where r1 = \"C170\" "
        update = update + " AND r0 between " + str(n1) + " AND " + str(n2) + " "
        update = update + " and r25 not in (\"05\",\"75\")), "
        update = update + " r27 = (select "
        update = update + " REPLACE(CAST(  ROUND(  SUM(CAST(replace(r36,',','.') AS FLOAT)),2)  AS TEXT),'.',',') "
        update = update + " from principal "
        update = update + " where r1 = \"C170\" "
        update = update + " AND r0 between " + str(n1) + " AND " + str(n2) + " "
        update = update + " and r31 not in (\"05\",\"75\")) "
        update = update + " WHERE "
        update = update + " r0 = " + str(n1) + " "
        update = update + " AND r2 = \"0\" "
        update = update + " AND r3 = \"1\" "
        update = update + " AND r5 = \"01\" "
        update = update + " AND r6 = \"00\" "
        cursor.execute(update)
        conexao.commit()

        n1 = n2

