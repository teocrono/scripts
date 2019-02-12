# tem que possuir a mesma quantidade de pis e cofins
import helper

def exec(conexao):

    cursor = conexao.cursor()

    print("RULE 24 - Inicializando",end=' ')

    select = """
        select count(*) from principal where r1 = "C491" and r0 not in 
        (select p1.r0 
        from principal p1 
        inner join principal p2 
        ON p1.r2 = p2.r2 and p1.r3 = p2.r3 and p1.r4 = p2.r4 and p1.r1 = "C491" and p2.r1 = "C495")
    """
    select = cursor.execute(select)
    qtC491 = select.fetchone()[0]

    select = """
        select count(*) from principal where r1 = "C495" and r0 not in 
        (select p2.r0 
        from principal p1 
        inner join principal p2 
        ON p1.r2 = p2.r2 and p1.r3 = p2.r3 and p1.r4 = p2.r4 and p1.r1 = "C491" and p2.r1 = "C495")
    """
    select = cursor.execute(select)
    qtC495 = select.fetchone()[0]

    ##funciona se houver apenas um registro C490
    select = """
        select count(*) from principal where r1 = "C490"
    """
    select = cursor.execute(select)
    qtC490 = select.fetchone()[0]

    if qtC490 == 1:
        if qtC491 == 0 and qtC495 > 0:
            ## pega o max do C491
            select = """
                select max(r0) from principal where r1 = "C491"
            """
            select = cursor.execute(select)
            maxC491 = select.fetchone()[0]
            
            ## atualiza o r0 acima do max do C495
            update = " UPDATE principal SET "
            update = update + " r0 = r0 + " + str(qtC495 + 10)
            update = update + " WHERE 1=1 "
            update = update + " AND r0 > " + str(maxC491) + " "
            cursor.execute(update)
            conexao.commit()

            ## insere os registros no C495 com a aliquota correta
            select = """
                select r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11 from principal where r1 = "C495" and r0 not in 
                (select p2.r0 
                from principal p1 
                inner join principal p2 
                ON p1.r2 = p2.r2 and p1.r3 = p2.r3 and p1.r4 = p2.r4 and p1.r1 = "C491" and p2.r1 = "C495")
            """
            select = cursor.execute(select)
            select = select.fetchall()
            num = maxC491
            for i in select:
                num = num + 1
                i2 = ['C491',i[2],i[3],i[4],i[5],i[6],'1,6500',i[8],i[9],helper.mult2strfloat(i[6],'1,6500'),i[11]]
                insert = " INSERT INTO principal(r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11)"
                insert = insert + " VALUES( "
                insert = insert + str(num) + ','
                insert = insert + '"' + '","'.join(i2) + '"'
                insert = insert + " ) "
                cursor.execute(insert)
                conexao.commit()
        elif qtC491 > 0 and qtC495 == 0:
            ## pega o max do C495
            select = """
                select max(r0) from principal where r1 = "C495"
            """
            select = cursor.execute(select)
            maxC495 = select.fetchone()[0]
            
            ## atualiza o r0 acima do max do C495
            update = " UPDATE principal SET "
            update = update + " r0 = r0 + " + str(qtC491 + 10)
            update = update + " WHERE 1=1 "
            update = update + " AND r0 > " + str(maxC495) + " "
            cursor.execute(update)
            conexao.commit()

            ## insere os registros no C495 com a aliquota correta
            select = """
                select r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11 from principal where r1 = "C491" and r0 not in 
                (select p1.r0 
                from principal p1 
                inner join principal p2 
                ON p1.r2 = p2.r2 and p1.r3 = p2.r3 and p1.r4 = p2.r4 and p1.r1 = "C491" and p2.r1 = "C495")
            """
            select = cursor.execute(select)
            select = select.fetchall()
            num = maxC495
            for i in select:
                num = num + 1
                i2 = ['C495',i[2],i[3],i[4],i[5],i[6],'7,6000',i[8],i[9],helper.mult2strfloat(i[6],'7,6000'),i[11]]
                insert = " INSERT INTO principal(r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11)"
                insert = insert + " VALUES( "
                insert = insert + str(num) + ','
                insert = insert + '"' + '","'.join(i2) + '"'
                insert = insert + " ) "
                cursor.execute(insert)
                conexao.commit()



    print('-',end=' ')
    print("Finalizado")
