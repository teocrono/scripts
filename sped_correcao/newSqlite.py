## Le arquivo sped original e envia os dados para o banco de dados sqlite
## com o mesmo nome do arquivo do sped com a extensão db
def exec(filename,criarDB,conexao):
    cursor = conexao.cursor()

    itens = ['r1','r2','r3','r4','r5','r6','r7','r8','r9','r10',
             'r11','r12','r13','r14','r15','r16','r17','r18','r19','r20',
             'r21','r22','r23','r24','r25','r26','r27','r28','r29','r30',
             'r31','r32','r33','r34','r35','r36','r37','r38','r39','r40',
             'r41','r42','r43','r44','r45','r46','r47','r48','r49','r50']
    
    if not criarDB: # Create table
        cursor.execute('''CREATE TABLE principal 
            (r0 int, r1 text,r2 text,r3 text,r4 text,r5 text,r6 text,r7 text,r8 text,r9 text,r10 text,
             r11 text,r12 text,r13 text,r14 text,r15 text,r16 text,r17 text,r18 text,r19 text,r20 text,
             r21 text,r22 text,r23 text,r24 text,r25 text,r26 text,r27 text,r28 text,r29 text,r30 text,
             r31 text,r32 text,r33 text,r34 text,r35 text,r36 text,r37 text,r38 text,r39 text,r40 text,
             r41 text,r42 text,r43 text,r44 text,r45 text,r46 text,r47 text,r48 text,r49 text,r50 text)''')
    else:
        cursor.execute('''DELETE FROM principal''')
    
    conexao.commit()

    #abre o arquivo sped a ser analisado
    arquivo = open("in/" + filename + '.txt', 'r')
    lista = arquivo.readlines()
    arquivo.close()

    ## envia todos os dados para o sqlite
    contador = 1
    for i in lista:
        listai = i.split('|')[1:-1]
        qtd = len(listai)
        text_insert = ""
        for i2 in listai:
            temp = i2.replace("'","''")
            text_insert = text_insert + "','" + temp 
        text_insert = "'" + str(contador) + "'," + text_insert[2:] + "'"
        contador = contador + 1

        text_values = ""
        for i2 in range(0,qtd):
            text_values = text_values + '\',\'' + itens[i2]
        text_values = "'r0'," + text_values[2:] + '\''

        insert = "INSERT INTO principal(" + text_values + ") VALUES (" + text_insert + ")"
        cursor.execute(insert)

    conexao.commit()
