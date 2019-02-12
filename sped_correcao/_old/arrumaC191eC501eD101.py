## Para operações com direito a crédito, devem ser informadas alíquotas básicas ou alíquotas 
## constantes nas tabelas Tabela 4.3.10 - Produtos Sujeitos à Incidência Monofásica da Contribuição
def exec(conexao):    
    cursor = conexao.cursor()

    update = '''
        WITH old AS (
        SELECT r0, REPLACE(CAST(  (ROUND(CAST(replace(r7,',','.') AS FLOAT) * 1.65 / 100,2))  AS TEXT),'.',',') AS valor
        FROM principal WHERE r1 = "C191" AND r3 = "50" AND r4 = "2102" AND r8 <> "1,6500")
        UPDATE principal SET
            r8 = "1,6500",
            r11 = (SELECT valor FROM old WHERE old.r0 = principal.r0),
            r3 = "50"
        WHERE r1 = "C191" AND r3 = "50" AND r4 = "2102" AND r8 <> "1,6500"
    '''
    cursor.execute(update)
    conexao.commit()
    print('REGISTROS C191 mudado a aliquota do pis e atualizado o valor')

    update = '''
        WITH old AS (
        SELECT r0 as id, REPLACE(CAST(  (ROUND(CAST(replace(r5,',','.') AS FLOAT) * 1.65 / 100,2))  AS TEXT),'.',',') AS valor
        FROM principal WHERE r1 = "C501" and r2 = "50" and r4 = "04" and r6 <> "1,6500")
        UPDATE principal SET
            r6 = "1,6500",
            r7 = (SELECT valor FROM old WHERE old.id = principal.r0)
        WHERE r1 = "C501" AND r2 = "50" AND r4 = "04" AND r6 <> "1,6500" 
    '''
    cursor.execute(update)
    conexao.commit()
    print('REGISTROS C501 mudado a aliquota do pis e atualizado o valor')

    update = '''
        WITH old AS (
        SELECT r0 as id, REPLACE(CAST(  (ROUND(CAST(replace(r6,',','.') AS FLOAT) * 1.65 / 100,2))  AS TEXT),'.',',') AS valor
        FROM principal WHERE r1 = "D101" and r4 = "50" and r5 = "07" and r7 <> "1,6500")
        UPDATE principal SET
            r7 = "1,6500",
            r8 = (SELECT valor FROM old WHERE old.id = principal.r0)
        WHERE r1 = "D101" AND r4 = "50" AND r5 = "07" AND r7 <> "1,6500" 
    '''
    cursor.execute(update)
    conexao.commit()
    print('REGISTROS D101 mudado a aliquota do pis e atualizado o valor')





