##programa principal 

import sqlite3
import os
import newSPED
import newSqlite
import rules
import rule01
import rule02
import rule04
import rule12
import rule14
import rule21
import rule22
import rule23
import rule24
import rule25

import arrumaM100eM105
import atualiza9001



for z in os.listdir("in"):
    filename = z.split('.')[0]
    print(filename)

    ## dados iniciais
    #filename = 'LIVROCONTRMATRIZ12013retificado'
    isDB = os.path.isfile("temp/" + filename + '.db')
    conn = sqlite3.connect("temp/" + filename + '.db')
    cursor = conn.cursor()

    ## cria database a partir do sped original
    newSqlite.exec(filename,isDB,conn)
    rule01.exec(conn)
    rules.exec(conn)
    rule02.exec(conn)
    rule12.exec(conn)
    rule04.exec(conn)
    rule14.exec(conn)
    rule21.exec(conn)
    rule22.exec(conn)
    rule23.exec(conn)
    rule24.exec(conn)
    rule25.exec(conn)

    arrumaM100eM105.exec(conn)
    atualiza9001.exec(conn)

    ## gera novo arquivo
    newSPED.exec(filename,conn.cursor())


conn.close()
print('FIM')