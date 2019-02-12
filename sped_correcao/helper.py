## funções para auxilio

def soma2strfloat(num1,num2):
    num1 = float(num1.replace(",","."))
    num2 = float(num2.replace(",","."))
    return str(round(num1 + num2,2)).replace(".",",")

def mult2strfloat(num1,num2):
    num1 = float(num1.replace(",","."))
    num2 = float(num2.replace(",","."))
    return str(round(num1 * num2,2)).replace(".",",")
 

def takeLimit(cursor,line,grupo):
    select = ""
    select = select + "	SELECT r0 "
    select = select + " FROM principal "
    select = select + " WHERE r0 >= " + str(line) + " " 
    select = select + " and r1 = \"" + grupo + "\"  order by r0 "
    
    temp = cursor.execute(select)
    temp = temp.fetchall()
    temp = [i[0] for i in temp]

    if len(temp) >= 2:
        return [temp[0] + 1,temp[1] - 1]
    else:
        return [temp[0] + 1,temp[0]+100]

def montaSetSql(dados):
    texto = ''
    for i in dados:
        temp = i.split('=')
        if len(temp) > 1:
            texto = texto + ' ' + temp[0]
            if temp[1][0] == 't':
                texto = texto + ' = ' + '\"' + temp[1][1:] + '\",'
            elif temp[1][0] == 'r':
                texto = texto + ' = ' + temp[1][1:] + ' ,'
            elif temp[1][0] == 'v':
                temp1 = temp[1][1:].split('v')
                texto = texto + ' = ' +  " REPLACE(CAST(  ROUND(( CAST(replace("
                texto = texto + temp1[0] + ",',','.') AS FLOAT) * CAST(replace("
                if temp1[1][0] == 'r':
                    texto = texto + temp1[1][1:] + ",',','.') AS FLOAT) / 100),2)  AS TEXT),'.',','),"
                else:
                    texto = texto + "\"" + temp1[1] + "\"" + ",',','.') AS FLOAT) / 100),2)  AS TEXT),'.',','),"
    return texto[:-1]

def montaWhereSql(dados):
    texto = ''
    for i in dados:
        temp = i.split('=')
        if len(temp) > 1:
            texto = texto + ' AND ' + temp[0]
            if temp[1][0] == 't':
                if temp[1][1] == 'd':
                    texto = texto + ' <> ' + '\"' + temp[1][2:] + '\"'
                elif temp[1][1] == 'v':
                    texto = texto + ' = ' + '""' + ' '
                else:
                    texto = texto + ' = ' + '\"' + temp[1][1:] + '\"'
            elif temp[1][0] == 'r':
                if temp[1][1] == 'd':
                    texto = texto + ' <> ' + temp[1][2:] + ' '
                else:
                    texto = texto + ' = ' + temp[1][1:] + ' '
                
            elif temp[1][0] == 'i':
                temp1 = temp[1][1:].split('i')
                texto = texto + ' in ' + '(\"' + '","'.join(temp1) + '\") '
            elif temp[1][0] == 'n':
                texto = texto + ' = ' + temp[1][1:] + ' '
    return texto