
def exec(conexao):
    cursor = conexao.cursor()

    update = '''
        WITH value AS (
            SELECT SUM(CAST(replace(r7,',','.') AS FLOAT)) as valor 
            FROM principal WHERE r1 = "C195" and r3 = "50"
        )
        UPDATE principal SET
            r4 = (SELECT REPLACE(CAST(valor AS TEXT),".",",") FROM value),
            r6 = (SELECT REPLACE(CAST(valor AS TEXT),".",",") FROM value),
            r7 = (SELECT REPLACE(CAST(valor AS TEXT),".",",") FROM value)
        WHERE r1 = "M505" and r2 = "01"
    '''
    cursor.execute(update)
    conexao.commit()

    update = '''
        WITH value AS (
            SELECT SUM(CAST(replace(r3,',','.') AS FLOAT)) as valor 
            FROM principal WHERE r1 = "C505" and r2 = "50"
        )
        UPDATE principal SET
            r4 = (SELECT REPLACE(CAST(valor AS TEXT),".",",") FROM value),
            r6 = (SELECT REPLACE(CAST(valor AS TEXT),".",",") FROM value),
            r7 = (SELECT REPLACE(CAST(valor AS TEXT),".",",") FROM value)
        WHERE r1 = "M505" and r2 = "04"
    '''
    cursor.execute(update)
    conexao.commit()

    update = '''
        WITH value AS (
            SELECT SUM(CAST(replace(r5,',','.') AS FLOAT)) as valor 
            FROM principal WHERE r1 = "D505" and r2 = "50"
        )
        UPDATE principal SET
            r4 = (SELECT REPLACE(CAST(valor AS TEXT),".",",") FROM value),
            r6 = (SELECT REPLACE(CAST(valor AS TEXT),".",",") FROM value),
            r7 = (SELECT REPLACE(CAST(valor AS TEXT),".",",") FROM value)
        WHERE r1 = "M505" and r2 = "01"
    '''
    cursor.execute(update)
    conexao.commit()

    update = '''
        WITH value AS (
            SELECT SUM(CAST(replace(r6,',','.') AS FLOAT)) as valor 
            FROM principal WHERE r1 = "D105" and r4 = "50" and r5="03"
        )
        UPDATE principal SET
            r4 = (SELECT REPLACE(CAST(valor AS TEXT),".",",") FROM value),
            r6 = (SELECT REPLACE(CAST(valor AS TEXT),".",",") FROM value),
            r7 = (SELECT REPLACE(CAST(valor AS TEXT),".",",") FROM value)
        WHERE r1 = "M505" and r2 = "03"
    '''
    cursor.execute(update)
    conexao.commit()

    update = '''
        WITH value AS (
            SELECT SUM(CAST(replace(r6,',','.') AS FLOAT)) as valor 
            FROM principal WHERE r1 = "D105" and r4 = "50" and r5="07"
        )
        UPDATE principal SET
            r4 = (SELECT REPLACE(CAST(valor AS TEXT),".",",") FROM value),
            r6 = (SELECT REPLACE(CAST(valor AS TEXT),".",",") FROM value),
            r7 = (SELECT REPLACE(CAST(valor AS TEXT),".",",") FROM value)
        WHERE r1 = "M505" and r2 = "03"
    '''
    cursor.execute(update)
    conexao.commit()
