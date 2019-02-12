## gera novo arquivo sped a partir do banco de dados
def exec(filename,cursor):

    arquivo = open("out/" + filename + '_r.txt', 'w')

    for row in cursor.execute('SELECT * FROM principal order by r0'):
        line = [i for i in row if i is not None]
        line = '|' + '|'.join(line[1:]) + '|' + '\n'
        arquivo.write(line)

    arquivo.close()