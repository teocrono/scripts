import helper

def exec(conexao):
    cursor = conexao.cursor()

    ## pega todos os registros do M100 e o segundo r0
    temp = cursor.execute("SELECT * FROM principal WHERE r1 = \"M100\"")
    temp = temp.fetchall()
    if len(temp) == 1:
        return "nada a arrumar no M100"
    m_principal = temp[0]
    r0_1 = temp[1][0]

    ## pega os registros M105 que estão fora do lugar
    temp = cursor.execute("SELECT r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10 FROM principal WHERE r1 = \"M105\" and r0 > " + str(r0_1))
    m105s = temp.fetchall()

    ## deleta todos os registros desnecessários
    delete = "delete from principal where r0 between " + str(r0_1) + " and " + str(m105s[len(m105s)-1][0])
    cursor.execute(delete)
    conexao.commit()

    ## verefica se existe o registro para saber se vai atualizar ou cadastrar os dados do M105
    for i in m105s:
        select = " select * from principal where r1 = \"M105\" and r2 = \"" + i[2] + "\" and r0 < \"" + str(r0_1) + "\""
        temp = cursor.execute(select)
        temp = temp.fetchall()
        
        ## verifica se existe, se for maior que 0 existe e vai atualizar o registro
        if len(temp) > 0:
            ## atualizar o r4
            r4 = helper.soma2strfloat(temp[0][4],i[4])
            r5 = helper.soma2strfloat(temp[0][5],i[5])
            r6 = helper.soma2strfloat(temp[0][6],i[6])
            r7 = helper.soma2strfloat(temp[0][7],i[7])

            update = " UPDATE principal SET "
            update = update + " r4 = \"" + r4 + "\","
            update = update + " r5 = \"" + r5 + "\","
            update = update + " r6 = \"" + r6 + "\","
            update = update + " r7 = \"" + r7 + "\""
            update = update + " WHERE r0 = \"" + str(temp[0][0]) + "\""
            cursor.execute(update)
            conexao.commit()
        else:
            i2 = [str(i2) for i2 in i]
            i2 = '"' + '","'.join(i2) + '"'

            insert = " INSERT INTO principal(r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10)"
            insert = insert + " VALUES( "
            insert = insert + i2
            insert = insert + " ) "
            cursor.execute(insert)
            conexao.commit()

    ## atualiza o M100 principal
    ## primeiro seleciona os seus dados
    update = " WITH temp AS ( "
    update = update + " select REPLACE(CAST(  SUM(CAST(replace(r4,',','.') AS FLOAT))  AS TEXT),'.',',') AS valor "
    update = update + " from principal where r1 = \"M105\" "
    update = update + " ) "
    update = update + " update principal set "
    update = update + " r2 = \"101\", "
    update = update + " r4 = (select valor from temp), "
    update = update + " r5 = \"1,6500\", "
    update = update + " r8 = (select REPLACE(CAST(  ROUND((CAST(replace(valor,',','.') AS FLOAT) * 1.65 / 100),2)  AS TEXT),'.',',') from temp), "
    update = update + " r12 = (select REPLACE(CAST(  ROUND((CAST(replace(valor,',','.') AS FLOAT) * 1.65 / 100),2)  AS TEXT),'.',',') from temp), "
    update = update + " r14 = (select REPLACE(CAST(  ROUND((CAST(replace(valor,',','.') AS FLOAT) * 1.65 / 100),2)  AS TEXT),'.',',') from temp) "
    update = update + " where r0 = \"" + str(m_principal[0]) + "\""
    cursor.execute(update)
    conexao.commit()
    print("arrumado registro M100")