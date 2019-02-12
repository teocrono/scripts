import cx_Oracle
import time

def mata():
    con = cx_Oracle.connect("SID/SENHA@DB")
    setattr(con, 'current_schema', 'SCHEMA')
    cur = con.cursor()

    sql = '''
    SELECT * FROM (
        SELECT s.osuser,s.machine,s.sid || ',' || s.serial# sid,s.module,s.program
        FROM v$session s, v$process p
        WHERE p.addr = s.paddr 
            and s.osuser <> 'SYSTEM' and s.username <> 'SYSMAN'
            AND S.USERNAME NOT IN ('IONV_SYNC','DBSNMP','FUSIONT','BR','ION_SYSTEM','WRFIN')
            
            AND S.OSUSER NOT IN ('usuario29','usuario26','usuario17')
            AND S.PROGRAM LIKE 'PC%'
            --AND S.PROGRAM LIKE '%1122%'
        CONNECT BY PRIOR s.sid = s.blocking_session
        START WITH s.blocking_session IS NULL
        order by s.osuser,S.PROGRAM DESC)
    '''

    cur.prepare(sql)
    cur.execute(None, {})

    res = cur.fetchall()
    for i in res:
        sqlMata = ' ALTER SYSTEM KILL SESSION '
        sqlMata = sqlMata + '\'' + i[2] + '\''
        cur.prepare(sqlMata)
        cur.execute(None, {} )
        print('matando - ' + str(i[0]) + ' - ' + str(i[3]))


    cur.close()
    con.close()


def online():
    con = cx_Oracle.connect("SID/SENHA@DB")
    setattr(con, 'current_schema', 'SCHEMA')
    cur = con.cursor()

    sql = '''
    SELECT * FROM (
        SELECT s.osuser,s.machine,s.sid || ',' || s.serial# sid,s.module,s.program
        FROM v$session s, v$process p
        WHERE p.addr = s.paddr 
            and s.osuser <> 'SYSTEM' and s.username <> 'SYSMAN'
            AND S.USERNAME NOT IN ('IONV_SYNC','DBSNMP','FUSIONT','BR','ION_SYSTEM','WRFIN')
            --AND S.OSUSER NOT IN ('usuario29','usuario26','usuario17')
            AND S.PROGRAM LIKE 'PC%'
            --AND S.PROGRAM LIKE '%1122%'
        CONNECT BY PRIOR s.sid = s.blocking_session
        START WITH s.blocking_session IS NULL
        order by s.osuser,S.PROGRAM DESC)
    '''

    cur.prepare(sql)
    cur.execute(None, {})

    res = cur.fetchall()
    for i in res:
        print(str(i[0]) + ' - ' + str(i[3]))

    cur.close()
    con.close()


def e():
    for i in range(1,1001):
        print(i)
        mata()
        time.sleep(5)

def i():
    for i in range(1,1001):
        print(i)
        online()
        time.sleep(5)

senha = input('Digite a senha: ')
if senha == '12358':
    e()
elif senha == '123':
    i()
else:
    print('você não tem autorização')
