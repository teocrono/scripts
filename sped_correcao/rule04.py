## Arruma duplicidade do C491 e C495
## 
## 


def exec(conexao):

    cursor = conexao.cursor()

    print("RULE 04 - Inicializando",end=' ')

    for c in ["C491","C495"]:
        #pega o r0 do C490
        temp = cursor.execute("select r0 from principal where r1 = \"C490\"")
        temp = temp.fetchall()
        rselect = []
        for i in temp:
            rselect.append(i[0])
        temp = cursor.execute("select max(r0) from principal where r1 = \"" + c + "\"")
        temp = temp.fetchone()
        rselect.append(temp[0])

        n2 = rselect.pop(0)
        while len(rselect) > 0:
            print('-',end=' ')
            n1 = n2
            n2 = rselect.pop(0)

            to_delete = " SELECT r0 FROM principal WHERE "
            to_delete = to_delete + " r1 = \"" + c + "\" "
            to_delete = to_delete + " and r2 in (SELECT r2 FROM principal WHERE "
            to_delete = to_delete + "              r1 = \"" + c + "\" AND r0 BETWEEN " + str(n1) + " and " + str(n2) + " "
            to_delete = to_delete + "              GROUP BY r2,r3,r4,r7,r9,r11 HAVING count(*) > 1) "
            to_delete = to_delete + " AND r0 BETWEEN " + str(n1) + " and " + str(n2) + " "
            to_delete = to_delete + " order by r0 "
            to_delete = cursor.execute(to_delete)
            to_delete = to_delete.fetchall()
            to_delete = [i[0] for i in to_delete]

            ## recalcula o valor gerando apenas um item pelo grupo especifico definido no layout sped
            itens = " SELECT r1,r2,r3,r4, "
            itens = itens + " REPLACE(CAST(  SUM(CAST(replace(r5,',','.') AS FLOAT))  AS TEXT),'.',',') r5, "
            itens = itens + " REPLACE(CAST(  SUM(CAST(replace(r6,',','.') AS FLOAT))  AS TEXT),'.',',') r6, "
            itens = itens + " r7,r8,r9, "
            itens = itens + " REPLACE(CAST(  SUM(CAST(replace(r10,',','.') AS FLOAT))  AS TEXT),'.',',') r10, "
            itens = itens + " r11 "
            itens = itens + " FROM "
            itens = itens + "   (SELECT r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11 "
            itens = itens + "       FROM principal where r2 in (SELECT r2 FROM principal WHERE r1 = \"" + c + "\" "
            itens = itens + " 										AND r0 BETWEEN " + str(n1) + " and " + str(n2) + " "
            itens = itens + " 										GROUP BY r2,r3,r4,r7,r9,r11 HAVING count(*) > 1) "
            itens = itens + " 		and r1 = \"" + c + "\" "
            itens = itens + " 		and r0 between " + str(n1) + " and " + str(n1) + " order by r2)  "
            itens = itens + " group by r1,r2,r3,r4,r7,r8,r9,r11 "
            itens = cursor.execute(itens)
            itens = itens.fetchall()

            ## deleta todos os itens r0
            delete = "delete from principal where r0 in (" + ",".join([str(i) for i in to_delete]) + ")"
            cursor.execute(delete)
            conexao.commit()
            ## inserir os novos dados com os ids livres
            for i in range(0,len(itens)):
                data = str(to_delete[i]) + ',"' + "\",\"".join(itens[i]) + '"'
                insert = " INSERT INTO principal(r0,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11) "
                insert = insert + " VALUES( "
                insert = insert + str(to_delete[i]) + ',"' + "\",\"".join(itens[i]) + '"'
                insert = insert + " ) "
                cursor.execute(insert)
                conexao.commit()

    print('-',end=' ')
    print("Finalizado")