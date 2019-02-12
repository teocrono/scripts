## Para cada registro filho referente ao PIS deve existir outro registro filho 
## referente a COFINS com CST referente ao PIS/PASEP igual ao CST referente à COFINS, 
## e Valor da base de cálculo do PIS/PASEP igual ao Valor da base de cálculo da COFINS.

 
def exec(conexao):

    cursor = conexao.cursor()

    print("RULE 10 - Inicializando",end=' ')

    update = '''
        WITH old AS (
        select r0 AS id,
        REPLACE(CAST(  (ROUND(CAST(replace(r3,',','.') AS FLOAT) * CAST(replace(r7,',','.') AS FLOAT) / 100,2))  AS TEXT),'.',',') AS valor
        from principal where r1 = "D101" and r3 <> r6)
        UPDATE principal SET
            r6 = r3,
            r8 = (SELECT valor FROM old WHERE old.id = principal.r0)
        WHERE r1 = "D101" and r3 <> r6
    '''
    cursor.execute(update)
    conexao.commit()
    print('REGISTROS D101 mudado o valor de calculo do pis e o resultado')

    update = '''
        WITH old AS (
        select r0 AS id,
        REPLACE(CAST(  (ROUND(CAST(replace(r3,',','.') AS FLOAT) * CAST(replace(r7,',','.') AS FLOAT) / 100,2))  AS TEXT),'.',',') AS valor
        from principal where r1 = "D105" and r3 <> r6)
        UPDATE principal SET
            r6 = r3,
            r8 = (SELECT valor FROM old WHERE old.id = principal.r0)
        WHERE r1 = "D105" and r3 <> r6
    '''
    cursor.execute(update)
    conexao.commit()
    print('REGISTROS D105 mudado o valor de calculo do pis e o resultado')

    update = '''
        UPDATE principal SET
            r6 = r3,
            r7 = "7,6000",
            r8 = REPLACE(CAST(  (ROUND(CAST(replace(r3,',','.') AS FLOAT) * 7.6 / 100,2))  AS TEXT),'.',',')
        WHERE r1 = "D105" and r7 = "7,6500"
    '''
    cursor.execute(update)
    conexao.commit()

    print('-',end=' ')
    print("Finalizado")