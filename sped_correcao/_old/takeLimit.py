## função para pegar os limites de um determinado grupo

def exec(cursor,line,grupo):
    select = ""
    select = select + "	SELECT r0 "
    select = select + " FROM principal "
    select = select + " where r0 between " + str(line) + " and " + str(line + 100) + " and r1 = \"" + grupo + "\"  order by r0 "
    
    temp = cursor.execute(select)
    temp = temp.fetchall()

    if len(temp) < 2:
        return False
    
    return [temp[0][0],temp[1][0] - 1]

